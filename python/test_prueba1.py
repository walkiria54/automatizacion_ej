from unittest import TestCase

from prueba1 import es_impar, es_impar_bool,  mayuscular, num_palabras


class Test(TestCase):
    def test_es_impar(self):
        resultado = es_impar(5)

    # sin comprobacion porq el metodo no devuelve nada

    def test_es_impar_bool(self):
        resultado = es_impar(-1)
        self.assertTrue(resultado)

    def test_es_impar_bool(self):
        # self.fail()
        lista = (1, 2, 3, 4, 5, 6, 7)
        for numero in lista:
            rsultado = es_impar_bool(numero)
        self.assertTrue(rsultado)


    def test_mayuscular(self):
        resultado=mayuscular('Hola esto convierte en mayusculas')
        self.assertEqual(resultado,'HOLA ESTO CONVIERTE EN MAYUSCULAS')


    def test_num_palabras(self):
        resultado=num_palabras('esto cuenta 4 palabras')
        self.assertEqual(resultado,4)
    def test_num_palabras2(self):
        resultado=num_palabras('esto cuenta 5 palabras ole')
        self.assertEqual(resultado,5)

    def test_num_palabras0(self):
        resultado = num_palabras('')
        self.assertEqual(resultado, 0)