# Data Structures & Algorithms in Python

## Environment
- python >= 3.7
- `pip install -r requirements.txt`

## Testing
Run all tests
```
python -m unittest discover -v tests
```
Run specific module
```
python -m unittest discover tests -v -p <module_name>
# e.g.
python -m unittest discover tests -v -p test_avl_tree.py
```
