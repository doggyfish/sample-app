@'
# OpenHands sample application

A small python project for testing OpenHands

The greeting.py module contains a greet(name) function.
Use Python standard-library unittest for tests
'@ | Set-Content -LiteralPath '
	(Join-Path $labSample "README.md") -Encoding UTF8