import unittest

from greeting import greet


class GreetTests(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Alice"), "hello, Alice!")

    def test_surrounding_spaces(self):
        self.assertEqual(greet("  Alice  "), "hello, Alice!")

    def test_surrounding_tabs_and_newlines(self):
        self.assertEqual(greet("\tAlice\n"), "hello, Alice!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "hello, stranger!")

    def test_whitespace_only_name(self):
        self.assertEqual(greet(" \t\n "), "hello, stranger!")

    def test_internal_spaces_are_preserved(self):
        self.assertEqual(greet("  Mary  Jane  "), "hello, Mary  Jane!")


if __name__ == "__main__":
    unittest.main()
