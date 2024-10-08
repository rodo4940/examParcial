import unittest

def mcd(a, b):
    """Calcula el máximo común divisor de dos números usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return abs(a)

def mcd_de_cuatro(a, b, c, d):
    """Calcula el máximo común divisor de cuatro números."""
    return mcd(mcd(a, b), mcd(c, d))

class TestMCD(unittest.TestCase):
    def test_mcd_dos_numeros(self):
        esperado = 6
        actual = mcd(48, 18)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

        esperado = 14
        actual = mcd(56, 98)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

        esperado = 1
        actual = mcd(101, 10)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

    def test_mcd_de_cuatro(self):
        esperado = 6
        actual = mcd_de_cuatro(48, 18, 30, 12)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

        esperado = 14
        actual = mcd_de_cuatro(56, 98, 14, 28)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

        esperado = 1
        actual = mcd_de_cuatro(101, 10, 5, 20)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

        esperado = 2
        actual = mcd_de_cuatro(2, 4, 6, 8)
        self.assertEqual(actual, esperado, f"Esperado: {esperado}, Actual: {actual}")

if __name__ == '__main__':
    unittest.main()
