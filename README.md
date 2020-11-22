# testing

## Run a simple test
```bash
$> python -m unittest <module>.<class>.<test_name>
```
example:
```bash
$> python -m unittest test_my_module.TestMyClass.test_this_is_a_test_case
```

## Make the enviroment to work

[install **virtualenv**](https://virtualenv.pypa.io/en/stable/installation.html)

```bash
$> virtualenv <enviroment_name> -p <python path>
```
example

```bash
$> virtualenv venv -p /usr/bin/python3
```

run virtual enviroment
```bash
$> source ./venv/bin/activate
```
