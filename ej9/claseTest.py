import unittest
from clasePalindromo import Palindromo


class TestPalabras(unittest.TestCase):
    def testMenem(self):
        p = Palindromo('menem')
        self.assertTrue(p.esPalindromo())

    def testAnna(self):
        p = Palindromo('ANNA')
        self.assertTrue(p.esPalindromo())

    def testAmorroma(self):
        p = Palindromo('amorroma')
        self.assertTrue(p.esPalindromo())

    def testFalso(self):
        p = Palindromo('falso')
        self.assertFalse(p.esPalindromo())

if __name__ == '__main__':
    unittest.main()
