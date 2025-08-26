import unittest
from utils import slugify

class TestSlugify(unittest.TestCase):
    def test_slugify_basic(self):
        test_cases = {
            "Hello World!": "hello-world",
            "  Leading and trailing spaces  ": "leading-and-trailing-spaces",
            "Multiple   spaces": "multiple-spaces",
            "Special #$&* Characters": "special-characters",
            "Accented éàü characters": "accented-eau-characters",
            "Mixed CASE Input": "mixed-case-input",
            "----Dashes---and---underscores___": "dashes-and-underscores",
            "123 Numbers 456": "123-numbers-456",
            "": "",
            "     ": "",
            "!!!@@@###$$$%%%^^^&&&***((()))": "",
        }
        
        for input_str, expected_output in test_cases.items():
            self.assertEqual(slugify(input_str), expected_output)

    def test_slugify_edge_cases(self):
        test_cases = {
            "🚀 Emoji test": "emoji-test",
            "中文测试": "",
            "Mixed 中文 and English": "mixed-and-english"
        }

        for input_str, expected_output in test_cases.items():
            self.assertEqual(slugify(input_str), expected_output)

    def test_slugify_long_string(self):
        input_str = "This is a very long string " * 10
        expected_output = "this-is-a-very-long-string-" * 10
        expected_output = expected_output.rstrip('-')
        self.assertEqual(slugify(input_str), expected_output)


if __name__ == '__main__':
    unittest.main()