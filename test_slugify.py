import unittest

from slugify import slugify


class TestSlugify(unittest.TestCase):
    def test_collapses_separators(self):
        self.assertEqual(slugify("a  b"), "a-b")

    def test_lowercases(self):
        self.assertEqual(slugify("Hello"), "hello")


if __name__ == "__main__":
    unittest.main()
