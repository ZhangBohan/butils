# Butils

## How to upload to pypi


```shell
rm dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
```
