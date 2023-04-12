<div align="center">

# is-base-64

![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![pypi](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)

[![List and Test](https://github.com/juunini/is-base-64-py/actions/workflows/lint-and-test.yaml/badge.svg)](https://github.com/juunini/is-base-64-py/actions/workflows/lint-and-test.yaml)
[![codecov](https://codecov.io/gh/juunini/is-base-64-py/branch/main/graph/badge.svg?token=TDGNG0KJMM)](https://codecov.io/gh/juunini/is-base-64-py)

</div>

## Installation

```bash
pip install is-base-64-py
```

## Usage

```python
from is_base_64 import is_base_64

is_base_64('aGVsbG8gd29ybGQ=') # True
is_base_64('this is not a base64 string') # False
```
