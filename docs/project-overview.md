# Project overview

## Purpose

This is a small Python project for testing OpenHands, as described in
[the README](../README.md). The [`greeting.py`](../greeting.py) module exposes
`greet(name)`, which strips surrounding whitespace and returns `hello, <name>!`.
Empty or whitespace-only names become `stranger`; internal spaces are preserved.

## Install

Use Python 3. The project uses only the Python standard library and has no
third-party dependencies, package manifest, or installation command. Work from
the repository root; no `pip install` step is needed.

## Run

There is no application CLI or server entry point. To call the existing function
from the repository root:

```sh
python -c "from greeting import greet; print(greet('Alice'))"
```

Expected output: `hello, Alice!`.

## Test

The README specifies standard-library `unittest`. Run the existing tests from
the repository root:

```sh
python -m unittest -v
```

[`test_greeting.py`](../test_greeting.py) contains six tests covering normal
names, surrounding whitespace, empty names, whitespace-only names, and preserved
internal spaces. It can also be run directly with `python test_greeting.py`.
