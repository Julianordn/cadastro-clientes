import unittest
from utils import validar_nome, validar_email, validar_telefone

class TestValidacoes(unittest.TestCase):

    def test_validar_nome(self):
        self.assertTrue(validar_nome("Juliano"))
        self.assertFalse(validar_nome(""))
        self.assertFalse(validar_nome("   "))

    def test_validar_email(self):
        self.assertTrue(validar_email("teste@email.com"))
        self.assertFalse(validar_email("testeemail.com"))
        self.assertFalse(validar_email("teste@com"))

    def test_validar_telefone(self):
        self.assertTrue(validar_telefone("11999998888"))
        self.assertFalse(validar_telefone("1234"))
        self.assertFalse(validar_telefone("abc123456"))

if __name__ == '__main__':
    unittest.main()
