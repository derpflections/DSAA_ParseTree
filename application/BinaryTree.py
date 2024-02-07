# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

class BinaryTree: #done by Wei Qi
    """
    A class representing a binary tree node.

    Attributes:
        key (any): The value stored in the node.
        leftTree (BinaryTree): The left child of the node.
        rightTree (BinaryTree): The right child of the node.
    """

    def __init__(self, key, leftTree=None, rightTree=None):
        """
        Initialize a binary tree node with a given key and optional children.
        
        Args:
            key (any): The value to store in the node.
            leftTree (BinaryTree, optional): The left child node. Defaults to None.
            rightTree (BinaryTree, optional): The right child node. Defaults to None.
        """
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey(self, key):
        """
        Sets the key of the node.
        
        Args:
            key (any): The new value for the node's key.
        """
        self.key = key

    def getKey(self):
        """
        Gets the key of the node.
        
        Returns:
            any: The value of the node's key.
        """
        return self.key

    def getLeftTree(self):
        """
        Gets the left child of the node.
        
        Returns:
            BinaryTree: The left child node.
        """
        return self.leftTree

    def getRightTree(self):
        """
        Gets the right child of the node.
        
        Returns:
            BinaryTree: The right child node.
        """
        return self.rightTree

    def insertLeft(self, key):
        """
        Inserts a new node with the given key as the left child of the current node.
        
        Args:
            key (any): The value to store in the new left child node.
        """
        if self.leftTree is None:
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftTree, t.leftTree = t, self.leftTree

    def insertRight(self, key):
        """
        Inserts a new node with the given key as the right child of the current node.
        
        Args:
            key (any): The value to store in the new right child node.
        """
        if self.rightTree is None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightTree, t.rightTree = t, self.rightTree

    def printInorder(self, level=0):
        """
        Prints the binary tree in an inorder traversal, which visits left, root, and then right nodes.
        
        Args:
            level (int, optional): The current level of the tree for indentation. Defaults to  0.
        """
        if self.rightTree is not None:
            self.rightTree.printInorder(level +  1)

        print(str(level * ".") + str(self.key))
        
        if self.leftTree is not None:
            self.leftTree.printInorder(level +  1)


