import unittest

from translator import englishToFrench, frenchToEnglish

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish("Hello"), "Bonjour")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "love")
    def testnull(self):
        self.assertEqual(frenchToEnglish(""), "")

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish("Hello"), "Bonjour")
        self.assertNotEqual(frenchToEnglish("0"), "0")
    def testnull(self):
        self.assertEqual(englishToFrench(""), "")


unittest.main()