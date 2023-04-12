import unittest
from cambio_de_base import decimal2binario, binario2decimal, decimal2octal,octal2decimal, decimal2hexa, hexa2decimal, binario2octal, binario2hexa

class TestNumeracion(unittest.TestCase):
    
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(92),'1011100')
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('1110110'),118)
    def test_decimal2octal(self):
        self.assertEqual(decimal2octal(55),'67')
    def test_octal2decimal(self):
        self.assertEqual(octal2decimal('132'),90)
    def test_decimal2hexa(self):
        self.assertEqual(decimal2hexa(154),'9A')
    def test_hexa2decimal(self):
        self.assertEqual(hexa2decimal('1C7'),455)
    def test_binario2octal(self):
        self.assertEqual(binario2octal('1001101'),115)
    def test_binario2hexa(self):
        self.assertEqual(binario2hexa('1110110'),'76')


if __name__=="__main__":
    unittest.main()

