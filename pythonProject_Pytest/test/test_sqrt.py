#import unittest

from src.Level_2.sqrt import fun_sqrt, fun_square


# class testsqrt(unittest.TestCase): #required when unittest module is used.
# def test_sqrt(self):  #required when unittest module is used.
def test_sqrt():
    #self.assertEqual(fun_sqrt(4),2)
    #self.assertEqual(fun_sqrt(16),4)
    assert  fun_sqrt(4)==2
    assert  fun_sqrt(25) ==5

def test_square():
    # self.assertEqual(fun_square(5),25)
    # self.assertEqual(fun_square(25),624)
    assert fun_square(6) ==36