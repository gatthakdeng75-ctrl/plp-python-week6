# Week 6 Assignment - Safe Functions

This assignment practices using try/except to handle errors safely in Python.

## Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary lookups.
- `unbreakable.py` - Demonstrates how to keep asking for valid input without crashing.
- `README.md` - Describes the files and explains how error handling works.

## Why can't an if check catch "abc" on its own?

An `if` check cannot catch "abc" as a number because converting "abc" with `int()` causes a `ValueError` before the program can continue to a normal numeric check. Using `try` and `except ValueError` allows the program to safely handle the invalid input.