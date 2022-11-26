import unittest

from translator import englishToFrench, frenchToEnglish

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        #self.assertEqual(frenchToEnglish('Hello'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour le monde!'), 'Hello world!')
        self.assertNotEqual(frenchToEnglish("Bonjour"), "love")
    def testnull(self):
        self.assertEqual(frenchToEnglish(" "), " ")

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        #self.assertEqual(frenchToEnglish("Hello"), "Bonjour")
        self.assertEqual(englishToFrench('Hello World!'), 'Bonjour le monde !') 
        self.assertNotEqual(frenchToEnglish("Love"), "Bonjour")
    def testnull(self):
        self.assertEqual(englishToFrench(" "), " ")


unittest.main()