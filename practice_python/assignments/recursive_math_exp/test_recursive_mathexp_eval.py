import unittest

from tasks.recursive_mathexp_eval import evaluate_mathexp

class TestRecursiveMathExpEval(unittest.TestCase):
    def test1(self):
        self.assertEqual(evaluate_mathexp("2+3*4"), 14)
    def test2(self):
        self.assertEqual(evaluate_mathexp("2+3*4 ^ 2"), 50)
        
        
if __name__ == "__main__":
    unittest.main()