import pytest
from mazePaths import countAllPaths


class TestMazePaths:
    
    def test_one(self):
        assert countAllPaths(2, 0, 0) == 2
    
    def test_two(self):
        assert countAllPaths(3, 0, 0) == 6
    
