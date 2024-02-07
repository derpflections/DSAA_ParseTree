# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
ParseTree.py
This module defines the ParseTree class for building and evaluating expressions from a string format. 
The ParseTree class utilizes a binary tree structure to organize and compute the values of mathematical 
expressions. It supports basic arithmetic operations (+, -, *, /) and exponentiation.

The ParseTree class is capable of parsing expressions with variables, handling parentheses for operation 
precedence, and performing arithmetic evaluations.

Classes:
    ParseTree: Represents a parse tree for arithmetic expressions.

Dependencies:
    - re: Used for tokenizing the string expression.
    - BinaryTree: A class representing the structure and operations of a binary tree.
    - Stack: A class used for maintaining the current position within the tree during parsing.
'''

import re
from application.BinaryTree import BinaryTree
from application.Stack import Stack

class ParseTree:
    def __init__(self, exp):
        """
        Initialize the ParseTree object with an arithmetic expression.

        Parameters:
        - exp (str): The arithmetic expression to be parsed and evaluated.
        """
        self.exp = exp  # Store the expression for later parsing.

    def buildParseTree(self, exp):
        """
        Constructs a binary parse tree from the given arithmetic expression.

        Parameters:
        - exp (str): The arithmetic expression to be converted into a parse tree.

        Returns:
        - BinaryTree: The root node of the constructed binary parse tree.
        """
        # Split the expression at '=', focusing on the right-hand side (RHS) for parsing.
        exp = exp.split("=")[1].strip()

        # Replace '**' with '^' to handle exponentiation, since '**' is not directly tokenizable.
        exp = exp.replace("**", "^")

        # Tokenize the expression into operands, operators, and parentheses.
        tokens = re.findall(r"\(|\)|\d+\.?\d*|\+|\-|\*|\/|\^|[A-Za-z]+", exp)

        # Initialize a stack to manage the tree nodes during construction.
        stack = Stack()
        # Create the root of the binary tree with a placeholder value.
        tree = BinaryTree("?")
        stack.push(tree)
        currentTree = tree  # Set the current working node to the root.

        for t in tokens:
            # RULE 0: If the token is a variable, set the current node's key and return to the parent node.
            if t.isalpha():
                currentTree.setKey(t)
                parent = stack.pop()
                currentTree = parent
                continue

            # RULE 1: If the token is '(', add a new node as the left child and move down to it.
            if t == "(":
                currentTree.insertLeft("?")
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()

            # RULE 2: If the token is an operator, set the current node's key to the operator,
            # add a new node as the right child, and move down to it.
            elif t in ["+", "-", "*", "/", "^"]:
                if t == "^":  # Adjust exponentiation back to Python's '**'.
                    t = "**"
                currentTree.setKey(t)
                currentTree.insertRight("?")
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            # RULE 3: If the token is a number, set the current node's key to the number and return to the parent node.
            elif t not in ["+", "-", "*", "/", ")"]:
                currentTree.setKey(float(t) if "." in t else int(t))
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If the token is ')', ascend to the parent node.
            elif t == ")":
                currentTree = stack.pop()

            # Handle any unrecognized tokens as errors.
            else:
                raise ValueError

        return tree  # Return the root of the completed parse tree.

    def evaluate(self, tree):
        """
        Evaluates the arithmetic expression represented by the binary parse tree.

        Parameters:
        - tree (BinaryTree): The root node of the binary parse tree.

        Returns:
        - The evaluated result of the arithmetic expression.

        Raises:
        - ValueError: If division by zero is attempted.
        """
        # Recursively evaluate the expression by traversing the tree.
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()

        # If both child nodes are present, perform the operation indicated by the current node's key.
        if leftTree and rightTree:
            if op == "+":
                return self.evaluate(leftTree) + self.evaluate(rightTree)
            elif op == "-":
                return self.evaluate(leftTree) - self.evaluate(rightTree)
            elif op == "*":
                return self.evaluate(leftTree) * self.evaluate(rightTree)
            elif op == "/":
                rightEval = self.evaluate(rightTree)
                if rightEval == 0:
                    raise ValueError("Division by zero is undefined")
                return self.evaluate(leftTree) / rightEval
            elif op == "**":
                return self.evaluate(leftTree) ** self.evaluate(rightTree)

        # If the node is a leaf (no children), return its key (value or variable).
        else:
            return tree.getKey()