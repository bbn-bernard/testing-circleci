import unittest
import example as ex

class TestSimpleNumber(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(4, ex.SimpleNumber(1).add(3))
        self.assertEqual(6, ex.SimpleNumber(2).multiply(3))
        
        self.assertAlmostEqual(0.06, ex.SimpleNumber(0.2).multiply(0.3))
        
    def test_from_str(self):
        self.assertEqual(4, ex.SimpleNumber('1').add(3))
        
        self.assertEqual(4, ex.SimpleNumber('1').add('3'))
        
        self.assertAlmostEqual(0.06, ex.SimpleNumber('0.2').multiply('0.3'))


if __name__ == '__main__':
    unittest.main()