import pytest

from python import dataStructures
from .MidOfList import getMiddleElement, listToLinkedlist, validateArray
from python.CustomExceptions.arrayExceptions import arrayInvalidSize
from python.dataStructures import linkedList
from python.dataStructures.linkedList.linkedListUtil import LinkedList, Node


class TestLinkedlist:
    """
        test class for the linkedlist function
    """

    def test_one(self):
        start = listToLinkedlist()
        assert getMiddleElement(start) == 30
    
    def test_two(self):

        with pytest.raises(ValueError):
            validateArray([10, 20, 30, 40])
    
    def test_three(self):
        
        with pytest.raises(ValueError):
            validateArray([])
    
    # def test_four(self):
    #     assert isinstance(listToLinkedlist([10, 20]), Node)
    
    def test_five(self):
        start = listToLinkedlist([10, 20, 60, 40])
        assert  getMiddleElement(start) == 60
