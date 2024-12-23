# Importar los módulos necesarios
import unittest
from io import StringIO
import sys

# Importar la clase Calculadora
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de Calculadora antes de cada prueba
        self.calc = Calculadora(texto="Resultado: ")

    def test_factorizacion(self):
        # Prueba para un número con factorización prima
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.factorizacion(30)
        sys.stdout = sys.__stdout__
        self.assertIn("2 x 3 x 5", salida_capturada.getvalue())

    def test_porcentaje(self):
        # Prueba para el cálculo de porcentaje
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.porcentaje(25, 200)
        sys.stdout = sys.__stdout__
        self.assertIn("12.5", salida_capturada.getvalue())

    def test_sumar(self):
        # Prueba de suma con varios números
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.sumar([1, 2, 3, 4])
        sys.stdout = sys.__stdout__
        self.assertIn("10", salida_capturada.getvalue())

    def test_restar(self):
        # Prueba de resta con varios números
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.restar([10, 5, 2])
        sys.stdout = sys.__stdout__
        self.assertIn("3", salida_capturada.getvalue())

    def test_multiplicar(self):
        # Prueba de multiplicación con varios números
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.multiplicar([2, 3, 4])
        sys.stdout = sys.__stdout__
        self.assertIn("24", salida_capturada.getvalue())

    def test_dividir(self):
        # Prueba de división con dos números
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.dividir([10, 2])
        sys.stdout = sys.__stdout__
        self.assertIn("5.0", salida_capturada.getvalue())

    def test_raiz_cuadrada(self):
        # Prueba para el cálculo de la raíz cuadrada
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.raizCuadrada(16)
        sys.stdout = sys.__stdout__
        self.assertIn("4.0", salida_capturada.getvalue())

    def test_raiz_cubica(self):
        # Prueba para el cálculo de la raíz cúbica
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.raizCubica(27)
        sys.stdout = sys.__stdout__
        self.assertIn("3.0", salida_capturada.getvalue())

    def test_potencia(self):
        # Prueba de cálculo de potencia
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.potencia(2, 3)
        sys.stdout = sys.__stdout__
        self.assertIn("8", salida_capturada.getvalue())

    def test_mcm(self):
        # Prueba para el cálculo del MCM
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.mcm(6, 8)
        sys.stdout = sys.__stdout__
        self.assertIn("24", salida_capturada.getvalue())

    def test_mcd(self):
        # Prueba para el cálculo del MCD
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.mcd(36, 60)
        sys.stdout = sys.__stdout__
        self.assertIn("12", salida_capturada.getvalue())

    def test_resto_division(self):
        # Prueba para el resto de la división
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.restoDivision(10, 3)
        sys.stdout = sys.__stdout__
        self.assertIn("1", salida_capturada.getvalue())

    def test_entrada_invalida(self):
        # Prueba para entrada no válida en las funciones
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.calc.sumar([1, "a", 3])  # Provocará un ValueError
        sys.stdout = sys.__stdout__
        self.assertIn("Error: Entrada no válida", salida_capturada.getvalue())

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
