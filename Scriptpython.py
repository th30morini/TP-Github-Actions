import unittest

class SimpleMath:

    @staticmethod
    def addition(a, b):
        return a + b

    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(2, 3)
        self.assertEqual(result, 5)

        result = SimpleMath.addition(-1, 1)
        self.assertEqual(result, 0)

        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0)

    def test_soustraction(self):
        result = SimpleMath.soustraction(2, 1)
        self.assertEqual(result, 1)

        result = SimpleMath.soustraction(8, 2)
        self.assertEqual(result, 6)

        result = SimpleMath.soustraction(3, 5)
        self.assertEqual(result, -2)


# Pour lancer le test
if __name__ == '__main__':
    unittest.main()
