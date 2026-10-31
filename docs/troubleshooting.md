# Installation and startup troubleshooting

This guide covers installation and startup only. The repository provides
`greeting.py`, which defines `greet(name)`, and `test_greeting.py`, which uses
Python's standard-library `unittest`. It does not provide an installer,
dependency manifest, command-line interface, or application server.

## Python is not found

Check that a Python 3 interpreter is available:

```sh
python3 --version
```

If the command is not found, install Python 3 and make sure its executable is
on your PATH, then reopen your terminal. If your system names the interpreter
`python` or uses the Windows launcher `py -3`, verify that it selects Python 3
and substitute it for `python3` in the commands below. The repository does not
declare a minimum supported Python version.

No third-party packages are needed for this module or its tests. There is no
`requirements.txt` or packaging configuration to install from; do not use
`pip install -r requirements.txt` or `pip install .` as setup steps.

## Python cannot find the module or test file

Run the commands from the repository root, the directory containing both
`greeting.py` and `test_greeting.py`. For example, after cloning into a directory
named `sample-app`:

```sh
cd sample-app
python3 -B -m unittest -v test_greeting
```

A `ModuleNotFoundError` for `greeting` or `test_greeting`, or a file-not-found
error when invoking a file, can mean that you are in the wrong directory or
have an incomplete checkout. Confirm that both source files are present and
retry from that directory. No package installation is required for these local
imports.

The test command explicitly selects the repository's test module. A successful
setup should run six tests and end with `OK`; a run reporting zero tests does
not verify this checkout. The `-B` option avoids writing bytecode cache files.

## Running greeting.py produces no output

This is expected: `greeting.py` defines a function but has no startup code that
calls it or prints a result. There is no server to start or port to open.
To check that Python can import and call the module, run from the repository
root:

```sh
python3 -B -c "from greeting import greet; print(greet('Alice'))"
```

Expected output:

```text
hello, Alice!
```

The README contains PowerShell file-writing fragments. They are not application
startup commands; use the Python commands above to verify setup instead.
