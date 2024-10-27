import unittest
from src.xenon_hash import XenonHash

class TestXenonHash(unittest.TestCase):
    def setUp(self):
        self.hasher = XenonHash()

    def test_empty_string(self):
        result = self.hasher.hash("")
        self.assertEqual(len(result), 128)  # 512 bits = 128 hex chars

    def test_basic_string(self):
        result = self.hasher.hash("Hello, World!")
        self.assertEqual(len(result), 128)

    def test_long_string(self):
        long_input = "a" * 1000
        result = self.hasher.hash(long_input)
        self.assertEqual(len(result), 128)

    def test_special_characters(self):
        result = self.hasher.hash("!@#$%^&*()")
        self.assertEqual(len(result), 128)

if __name__ == '__main__':
    unittest.main()