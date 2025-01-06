import calk
import unittest

class CalkTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calk.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calk.sub(3, 2), 1)


    def test_mul(self):
        self.assertEqual(calk.mul(2, 3), 6)


    def test_div(self):
        self.assertEqual(calk.div(3, 2), 1.5)



if __name__ == '__main__':
    unittest.main()