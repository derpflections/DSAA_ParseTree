# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
ParseInsert.py


'''
from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.Variable import Variable
import re

class ParseInserter:
    def __init__(self, hashTable):
        self.__Hash = hashTable

    def checkForAlpha(self, exp, alpha, depth=10):
        if depth == 0:
            return  # Stopping criteria: depth limit reached
 
        if self.checkValidity(exp, alpha):
            raise ValueError("Invalid expression")
        
        if self.checkBrackets(exp):
            raise ValueError("Invalid expression")

        # Split the expression into the left hand side and right hand side
        temp_rhs = exp.split('=')[1].replace('(', '').replace(')', '').strip()
        temp_lhs = exp.split('=')[0].strip()
        
        # If the expression is a number without any operators
        if temp_rhs.isnumeric():
            # Add 00 to the number to make it a valid expression
            # Add 00 so that it doesnt clash with anything that actually has +0
            exp = temp_lhs + '=' + '(' + temp_rhs + '+00' + ')' 

        # if expression has a variable in it, replace the variable with its value
        if any(key in exp for key in self.__Hash.__getkeys__()):
            replaced_exp = exp
            for key in self.__Hash.__getkeys__():
                if key in replaced_exp.split("=")[1]:
                    # Using regular expressions to replace exact matches of the variable name
                    replaced_exp = re.sub(
                        r"\b{}\b".format(key),
                        str(self.__Hash.__getitem__(key).getEval()),
                        replaced_exp,
                    )
                    # print("Replaced exp:", replaced_exp)
            # if the replaced expression still has a variable in it after replacing, set evaluation to None
            if any(c.isalpha() for c in replaced_exp.split("=")[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            # otherwise, evaluate the expression
            else:
                parser = ParseTree(replaced_exp)
                tree = parser.buildParseTree(replaced_exp)
                evaluation = parser.evaluate(tree)
                # remove +0 from the expression
                exp = exp.replace("+00", "")
                self.__Hash[alpha] = Variable(exp, evaluation)

        # if the expression has no variables or have new variables run this
        else:
            # if variable is new, set evaluation to None
            if any(c.isalpha() for c in exp.split("=")[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            # otherwise, evaluate the expression
            else:
                parser = ParseTree(exp)
                tree = parser.buildParseTree(exp)
                evaluation = parser.evaluate(tree)
                # remove +0 from the expression
                exp = exp.replace("+00", "")
                self.__Hash[alpha] = Variable(exp, evaluation)

        # Check if any other variable depends on the current one
        for key in self.__Hash.__getkeys__():
            if key != alpha and alpha in self.__Hash[key].getExp():
                self.checkForAlpha(self.__Hash[key].getExp(), key, depth - 1)

        # print("Updated hash table:", self.__Hash)

    def checkValidity(self, exp, alpha):
        if not alpha.isalpha() or exp.find("=") == -1 or exp.replace(" ", "").replace("=", "").isalnum():
                return True      
        return False
    
    def checkBrackets(self, exp):
        exp = exp.split("=")[1]
        exp = exp.strip()
        if exp.count("(") != exp.count(")"):
            return True
        elif exp == '()':
            return True
        elif "(" not in exp or ")" not in exp:
            return True
        return False
    
        
        
            
