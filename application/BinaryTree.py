# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
BinaryTree.py
'''


class BinaryTree:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
    
    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftChild

    def getRightTree(self):
        return self.rightChild
    
    def insertLeft(self, key):
        if self.leftChild == None:
            self.leftChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftChild = t
            t.leftChild = self.leftChild

    def insertRight(self, key):
        if self.rightChild == None:
            self.rightChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightChild = t
            t.rightChild = self.rightChild

    def printPreorder(self, level): 
        print( str(level*'-') + str(self.key))
        if self.leftChild!= None:
            self.leftChild.printPreorder(level+1)
        if self.rightChild!= None:
            self.rightChild.printPreorder(level+1) 

    def deleteTree(self):
        self.key = None
        self.leftChild = None
        self.rightChild = None
    
    