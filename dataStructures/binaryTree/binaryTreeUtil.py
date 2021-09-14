# Binary Tree Util module


class TreeNode():
    """
        Creates Nodes for binary tree
    """

    data = None
    left = None
    right = None

    def __init__(self, data: int = 0, left = None, right = None) -> None:
        """
            initializes the Node object
        """

        self.data = data
        self.left = left
        self.right = right

    
    def __str__(self) -> str:
        return f"Data: {self.data}"


# Binary Tree Util Functions

