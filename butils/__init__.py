import functools
import json

import logging
logger = logging.getLogger()


def safe_method(f):
    """
    this method will not raise exception

    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.exception(e)

    return wrapper


class retry(object):
    """
    retry method on exception
    """
    def __init__(self, max_retries=3, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.exceptions = exceptions

    def __call__(self, f, *args, **kwargs):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retries + 1):
                try:
                    result = f(*args, **kwargs)
                except self.exceptions:
                    continue
                else:
                    return result
        return wrapper


def get_json_property(data: object, property_str: str) -> object:

    """

    :param data: data, can be string or dict
    :param property_str: property_str, like a.b or a.l[0].d
    :return: target data property
    """
    if isinstance(data, str):
        data = json.loads(data)

    if not isinstance(data, dict):
        raise ValueError('data type must be string or dict')

    for property_item in property_str.split('.'):
        if property_item.endswith(']'):
            index = int(property_item[property_item.index('[') + 1:-1])
            property_item = property_item[:property_item.index('[')]
            result = data.get(property_item)[index]
        else:
            result = data.get(property_item)

        if result is None:
            return

        data = result
    return data


class Struct:
    """
    The recursive class for building and representing objects with.
    """

    def __init__(self, obj):
        for k, v in obj.iteritems():
            if isinstance(v, dict):
                setattr(self, k, Struct(v))
            else:
                setattr(self, k, v)

    def __getitem__(self, val):
        return self.__dict__[val]

    def __repr__(self):
        return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
                                      (k, v) in self.__dict__.iteritems()))
