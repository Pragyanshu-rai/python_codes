import pytest
from permutations import getPermutations, getSafePermutations


class TestClass:

    def test_one(self):
        
        assert getPermutations("ABC") == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

    def test_two(self):

        assert getSafePermutations("ABC") == ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']

    def test_three(self):

        assert getSafePermutations("ABB") == ['ABB', 'BAB', 'BBA']
    
    def test_four(self):

        assert getSafePermutations("ab") == getPermutations("ab")
    
    def test_five(self):

        assert len(getSafePermutations("abbb")) < len(getPermutations("abbb"))