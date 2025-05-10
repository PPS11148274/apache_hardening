import unittest
from calculadora import realizar_operacion

class TestCalculadora(unittest.TestCase):
    
    def test_suma_numeros(self):
        self.assertEqual(realizar_operacion('1', 5, 3), 8)
        self.assertEqual(realizar_operacion('+', 5, 3), 8)
        self.assertEqual(realizar_operacion('1', -1, 1), 0)
        self.assertEqual(realizar_operacion('+', 2.5, 3.5), 6.0)
    
    def test_resta_numeros(self):
        self.assertEqual(realizar_operacion('2', 5, 3), 2)
        self.assertEqual(realizar_operacion('-', 5, 3), 2)
        self.assertEqual(realizar_operacion('2', -1, 1), -2)
        self.assertEqual(realizar_operacion('-', 2.5, 1.5), 1.0)
    
    def test_multiplicacion_numeros(self):
        self.assertEqual(realizar_operacion('3', 5, 3), 15)
        self.assertEqual(realizar_operacion('*', 5, 3), 15)
        self.assertEqual(realizar_operacion('3', -1, 1), -1)
        self.assertEqual(realizar_operacion('*', 2.5, 4), 10.0)
    
    def test_division_numeros(self):
        self.assertEqual(realizar_operacion('4', 6, 3), 2)
        self.assertEqual(realizar_operacion('/', 6, 3), 2)
        self.assertEqual(realizar_operacion('4', -1, 1), -1)
        self.assertAlmostEqual(realizar_operacion('/', 1, 3), 0.333333, places=6)
    
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            realizar_operacion('4', 5, 0)
        with self.assertRaises(ValueError):
            realizar_operacion('/', 5, 0)
    
    def test_operacion_invalida(self):
        with self.assertRaises(ValueError):
            realizar_operacion('5', 2, 3)
        with self.assertRaises(ValueError):
            realizar_operacion('%', 2, 3)

if __name__ == '__main__':
    unittest.main()
