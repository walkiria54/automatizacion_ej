from unittest import TestCase

from ejelogin import hacer_login


class Test(TestCase):
    RUTA_IMAGENES= '/home/usuario/Imágenes'
    def test_hacer_login_mal(self):
        resultado=hacer_login('kk', '1111', 'maltodo',Test.RUTA_IMAGENES)
        self.assertEqual(resultado, 'ACCESS DENIED!')
    def test_hacer_login_mal2(self):
        resultado=hacer_login('admin', '33333','malpass',Test.RUTA_IMAGENES)
        self.assertEqual(resultado, 'ACCESS DENIED!')
    def test_hacer_login_mal3(self):
        resultado=hacer_login('xxxx', '12345','malusu',Test.RUTA_IMAGENES)
        self.assertEqual(resultado, 'ACCESS DENIED!')
    def test_hacer_login_mal3(self):
        resultado=hacer_login('', '','malvacio',Test.RUTA_IMAGENES)
        self.assertEqual(resultado, 'ACCESS DENIED!')

    def test_hacer_login_ok(self):
        resultado=hacer_login('admin', '12345','ok',Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"WELCOME :)" )