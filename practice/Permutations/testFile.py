import pytest
from permutations import getPermutations, getSafePermutations
from Knapsack_01 import knapsack01


class TestPermutations:

    def test_one(self):

        assert getPermutations("ABC") == [
            'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

    def test_two(self):

        assert getSafePermutations(
            "ABC") == ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']

    def test_three(self):

        assert getSafePermutations("ABB") == ['ABB', 'BAB', 'BBA']

    def test_four(self):

        assert getSafePermutations("ab") == getPermutations("ab")

    def test_five(self):

        assert len(getSafePermutations("abbb")) < len(getPermutations("abbb"))


class TestKnapsack:

    def test_one(self):

        assert knapsack01([100, 50, 150], [10, 20, 30], 3, 50) == 250

    def test_two(self):

        assert knapsack01([20, 5, 10, 40, 15, 25], [
            1, 2, 3, 8, 7, 4], 6, 10) == 60
