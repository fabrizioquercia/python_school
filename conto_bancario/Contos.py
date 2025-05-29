import unittest

class Conto:
    __saldo_default = 1000
    def __init__(self, nome, saldo):
        self.nome = nome
        if saldo > 0:
            self.saldo = saldo
        else:
            self.saldo = self.__saldo_default

class MioTest(unittest.TestCase):
    def setUp(self):
        self.conto1 = Conto("Conto1", 1000)

    def test_saldo(self):
        self.assertEqual( self.conto1.saldo, 1000 )






unittest.main()