from unittest import TestCase
from com.breno.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_subtracao(self):
        self.assertEqual(self.operacoes.subtracao([10, 5]), 5, "Deveria ser 5")