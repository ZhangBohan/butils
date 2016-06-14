# coding=utf-8


def snake_case_to_camel_case(snake_str):
    components = snake_str.split('_')

    return components[0] + "".join(x.title() for x in components[1:])


def camel_case_to_snake_case(camel_str):
    char_list = []
    for char in camel_str:
        if char.isupper():
            char_list.append('_')
            char_list.append(char.lower())
        else:
            char_list.append(char)

    return ''.join(char_list)


def dict_key_to_snake_case_key(data):
    new_data = {}
    for key, value in data.items():
        new_data[camel_case_to_snake_case(key)] = value

    return new_data


def dict_key_to_camel_case_key(data):
    new_data = {}
    for key, value in data.items():
        new_data[snake_case_to_camel_case(key)] = value

    return new_data
