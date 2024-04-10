import unittest

def es_primo(numero):

    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

class TestEsPrimo(unittest.TestCase):

    def test_primos(self):
    
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(11))

    def test_no_primos(self):

        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(8))
        self.assertFalse(es_primo(9))

    def test_numeros_negativos(self):
        
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-2))
        self.assertFalse(es_primo(-3))

    unittest.main()