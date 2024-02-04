# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
ParseTree.py
'''

import re
from application.BinaryTree import BinaryTree
from application.Stack import Stack
from application.Variable import Variable

# from application.Variable import Variable
# from BinaryTree import BinaryTree
# from Stack import Stack

class ParseTree:
    def __init__(self, exp):
        self.exp = exp

    def buildParseTree(self, exp):
        # since ** is not supported in python, we replace it with ^ first
        exp = exp.replace("**", "^")
        tokens = re.findall(r"\(|\)|\d+\.?\d*|\+|\-|\*|\/|\^", exp)

        stack = Stack()
        tree = BinaryTree("?")
        stack.push(tree)
        currentTree = tree
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == "(":
                currentTree.insertLeft("?")
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ["+", "-", "*", "/", "^"]:
                if t == "^":
                    # replace ^ with **
                    t = "**"
                currentTree.setKey(t)
                currentTree.insertRight("?")
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t not in ["+", "-", "*", "/", ")"]:
                if "." in t:
                    currentTree.setKey(float(t))
                else:
                    currentTree.setKey(int(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If token is ')' go to parent of current node
            elif t == ")":
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
  

    def evaluate(self, tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()

        if leftTree != None and rightTree != None:

            if op == "+":
                return self.evaluate(leftTree) + self.evaluate(rightTree)
            elif op == "-":
                return self.evaluate(leftTree) - self.evaluate(rightTree)
            elif op == "*":
                return self.evaluate(leftTree) * self.evaluate(rightTree)
            elif op == "/":
                # check for division by zero
                if self.evaluate(rightTree) != 0:
                    return self.evaluate(leftTree) / self.evaluate(rightTree)
                else:
                    raise ValueError("Division by zero is undefined")
            elif op == "**":
                return self.evaluate(leftTree) ** self.evaluate(rightTree)

        else:
            return tree.getKey()
      

# main program
# if __name__ == "__main__":
#     exp = input("Enter the assignment statement you want to modify:\nFor example, a=(1+2)\n")
#     parser = ParseTree(exp)
#     tree = parser.buildParseTree(exp)
#     tree.printInorder(0)
#     evaluation = parser.evaluate(tree)
#     print(evaluation) # remove this line when you are done with the program
#     input("Press enter to continue...")