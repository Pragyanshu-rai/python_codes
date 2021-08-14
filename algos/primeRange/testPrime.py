from random import randint
from unittest import TestCase
import unittest
from simpleAlgo import primeRange as simplePR
from optimalAlgo import primeRange as optimalPR


class testPrime(TestCase):

    def testPR(self):
        for times in range(100):
            upper = randint(5, 99999)
            self.assertEqual(simplePR(upper=upper), optimalPR(upper=upper))


# runs if this file is executed directly insted of being imported
if __name__ == "__main__":
    unittest.main()
