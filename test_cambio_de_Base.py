import unittest
from cambio_de_base import decimal2binario, binario2decimal, decimal2octal,octal2decimal, decimal2hexa, hexa2decimal, binario2octal, binario2hexa, octal2binario,octal2hexa,hexa2binario, hexa2octal

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
        self.assertEqual(decimal2hexa(118),'76')
    def test_hexa2decimal(self):
        self.assertEqual(hexa2decimal('1C7'),455)
    def test_binario2octal(self):
        self.assertEqual(binario2octal('1001101'),115)
    def test_binario2hexa(self):
        self.assertEqual(binario2hexa('1110110'),'76')
    def test_octal2binario(self):
        self.assertEqual(octal2binario(44),'100100')
    def test_octal2hexa(self):
        self.assertEqual(octal2hexa(56),'2E')
    def test_hexa2binario(self):
        self.assertEqual(hexa2binario('567'),'10101100111')
    def test_hexa2octal(self):
        self.assertEqual(hexa2octal('24D'),'1115')



if __name__=="__main__":
    unittest.main()

