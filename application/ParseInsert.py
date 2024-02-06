# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
ParseInsert.py


'''

# from application.ParseTree import ParseTree
# from application.HashTable import HashTable
# from application.Variable import Variable

# import re


# class ParseInserter():
#     def __init__(self, hashTable):
#         self.__Hash = hashTable

#     def checkForAlpha(self, exp, alpha):
#         if self.checkValidity(exp, alpha):
#             raise ValueError("Invalid variable name")
#         if any(key in exp for key in self.__Hash.__getkeys__()):
#             replaced_exp = exp
#             for key in self.__Hash.__getkeys__():
#                 if key in replaced_exp.split('=')[1]:
#                     # Using regular expressions to replace exact matches of the variable name
#                     replaced_exp = re.sub(r'\b{}\b'.format(key), str(self.__Hash.__getitem__(key).getEval()), replaced_exp)
#             if any(c.isalpha() for c in replaced_exp.split('=')[1]):
#                 evaluation = None
#                 self.__Hash[alpha] = Variable(exp, evaluation)
#             else:
#                 parser = ParseTree(replaced_exp)
#                 tree = parser.buildParseTree(replaced_exp)
#                 evaluation = parser.evaluate(tree)
#                 self.__Hash[alpha] = Variable(exp, evaluation)

#         else:
#             if any(c.isalpha() for c in exp.split('=')[1]):
#                 evaluation = None
#                 self.__Hash[alpha] = Variable(exp, evaluation)
#             else:
#                     parser = ParseTree(exp)
#                     tree = parser.buildParseTree(exp)
#                     evaluation = parser.evaluate(tree)
#                     self.__Hash[alpha] = Variable(exp, evaluation)

#         print("Updated hash table:", self.__Hash)

#     def checkValidity(self, exp, alpha):
#         if not alpha.isalpha():
#             if exp.find('=') == -1:
#                 return True
#         return False

from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.Variable import Variable

import re


# class ParseInserter:
#     def __init__(self, hashTable):
#         self.__Hash = hashTable

#     def checkForAlpha(self, exp, alpha):
#         if self.checkValidity(exp, alpha):
#             raise ValueError("Invalid variable name")
#         if any(key in exp for key in self.__Hash.__getkeys__()):
#             replaced_exp = exp
#             for key in self.__Hash.__getkeys__():
#                 if key in replaced_exp.split("=")[1]:
#                     # Using regular expressions to replace exact matches of the variable name
#                     replaced_exp = re.sub(
#                         r"\b{}\b".format(key),
#                         str(self.__Hash.__getitem__(key).getEval()),
#                         replaced_exp,
#                     )
#             if any(c.isalpha() for c in replaced_exp.split("=")[1]):
#                 evaluation = None
#                 self.__Hash[alpha] = Variable(exp, evaluation)
#             else:
#                 parser = ParseTree(replaced_exp)
#                 tree = parser.buildParseTree(replaced_exp)
#                 evaluation = parser.evaluate(tree)
#                 self.__Hash[alpha] = Variable(exp, evaluation)

#             # Check if any other variable depends on the current one
#             for key in self.__Hash.__getkeys__():
#                 if key != alpha and alpha in self.__Hash[key].getExp():
#                     self.checkForAlpha(self.__Hash[key].getExp(), key)

#         else:
#             if any(c.isalpha() for c in exp.split("=")[1]):
#                 evaluation = None
#                 self.__Hash[alpha] = Variable(exp, evaluation)
#             else:
#                 parser = ParseTree(exp)
#                 tree = parser.buildParseTree(exp)
#                 evaluation = parser.evaluate(tree)
#                 self.__Hash[alpha] = Variable(exp, evaluation)

#         # print("Updated hash table:", self.__Hash)

#     def checkValidity(self, exp, alpha):
#         if not alpha.isalpha():
#             if exp.find("=") == -1:
#                 return True
#         return False

import re

class ParseInserter:
    def __init__(self, hashTable):
        self.__Hash = hashTable

    def checkForAlpha(self, exp, alpha, depth=10):
        if depth == 0:
            return  # Stopping criteria: depth limit reached
        
        if self.checkValidity(exp, alpha):
            raise ValueError("Invalid expression")

        temp_rhs = exp.split('=')[1].replace('(', '').replace(')', '')
        temp_lhs = exp.split('=')[0].strip()
        
        # If the expression is a number without any operators
        if temp_rhs.isnumeric():
            # Add 00 to the number to make it a valid expression
            # Add 00 so that it doesnt clash with anything that actually has +0
            exp = temp_lhs + '=' + '(' + temp_rhs + '+00' + ')' 


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

            if any(c.isalpha() for c in replaced_exp.split("=")[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            else:
                parser = ParseTree(replaced_exp)
                tree = parser.buildParseTree(replaced_exp)
                evaluation = parser.evaluate(tree)
                # remove +0 from the expression
                exp = exp.replace("+00", "")
                self.__Hash[alpha] = Variable(exp, evaluation)

            # Check if any other variable depends on the current one
            for key in self.__Hash.__getkeys__():
                if key != alpha and alpha in self.__Hash[key].getExp():
                    self.checkForAlpha(self.__Hash[key].getExp(), key, depth - 1)

        else:
            if any(c.isalpha() for c in exp.split("=")[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            else:
                parser = ParseTree(exp)
                tree = parser.buildParseTree(exp)
                evaluation = parser.evaluate(tree)
                # remove +0 from the expression
                exp = exp.replace("+00", "")
                self.__Hash[alpha] = Variable(exp, evaluation)

        # print("Updated hash table:", self.__Hash)

    def checkValidity(self, exp, alpha):
        exp = exp.split("=")[1]
        if exp.count("(") != exp.count(")"):
            raise ValueError("Invalid expression")
        elif exp == '()':
            raise ValueError("Invalid expression")
        if not alpha.isalpha():
            if exp.find("=") == -1:
                return True
        return False
    
        
        
            
