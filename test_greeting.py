import unittest

from greeting import greet


class GreetTests(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Alice"), "hello, Alice!")

    def test_explicit_lowercase(self):
        self.assertEqual(greet("Alice", uppercase=False), "hello, Alice!")

    def test_uppercase(self):
        self.assertEqual(greet("Alice", uppercase=True), "HELLO, ALICE!")

    def test_uppercase_trims_whitespace(self):
        self.assertEqual(greet(" \tAlice\n ", uppercase=True), "HELLO, ALICE!")

    def test_uppercase_blank_names(self):
        for name in ("", " \t\n "):
            with self.subTest(name=name):
                self.assertEqual(greet(name, uppercase=True), "HELLO, STRANGER!")

    def test_uppercase_preserves_internal_spaces(self):
        self.assertEqual(greet("  Mary  Jane  ", uppercase=True), "HELLO, MARY  JANE!")

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
