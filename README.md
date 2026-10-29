# OpenHands sample application

A small Python project for testing OpenHands.

## Usage

The `greeting.py` module provides `greet(name, uppercase=False)`. Names are
trimmed, and empty or whitespace-only names use `stranger`. Set `uppercase=True`
to uppercase the entire greeting; existing calls keep their original behavior.

```python
from greeting import greet

greet("Alice")                         # "hello, Alice!"
greet("Alice", uppercase=False)        # "hello, Alice!"
greet("Alice", uppercase=True)         # "HELLO, ALICE!"
greet("  Alice  ", uppercase=True)     # "HELLO, ALICE!"
greet(" ", uppercase=True)             # "HELLO, STRANGER!"
```

## Tests

Run the tests with Python's standard-library unittest:

```sh
python -m unittest -v
```
