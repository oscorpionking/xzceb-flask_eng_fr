import unittest

from translator import english_to_french, french_to_english

class Testfrench_to_english(unittest.TestCase): 
    def test1(self):
        #self.assertEqual(french_to_english('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour le monde!'), 'Hello world!')
        self.assertNotEqual(french_to_english("Bonjour"), "love")
    def testnull(self):
        self.assertEqual(french_to_english(" "), " ")

class Testenglish_to_french(unittest.TestCase): 
    def test1(self):
        #self.assertEqual(frenchToEnglish("Hello"), "Bonjour")
        self.assertEqual(english_to_french('Hello World!'), 'Bonjour le monde !') 
        self.assertNotEqual(english_to_french("Love"), "Bonjour")
    def testnull(self):
        self.assertEqual(english_to_french(" "), " ")


unittest.main()