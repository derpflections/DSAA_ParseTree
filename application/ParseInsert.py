from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.Variable import Variable

import re


class ParseInserter():
    def __init__(self, hashTable):
        self.__Hash = hashTable

    def checkForAlpha(self, exp, alpha):
        if self.checkValidity(alpha):
            raise ValueError("Invalid variable name")
        if any(key in exp for key in self.__Hash.__getkeys__()):
            replaced_exp = exp
            for key in self.__Hash.__getkeys__():
                if key in replaced_exp.split('=')[1]:
                    # Using regular expressions to replace exact matches of the variable name
                    replaced_exp = re.sub(r'\b{}\b'.format(key), str(self.__Hash.__getitem__(key).getEval()), replaced_exp)
            if any(c.isalpha() for c in replaced_exp.split('=')[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            else:
                parser = ParseTree(replaced_exp)
                tree = parser.buildParseTree(replaced_exp)
                evaluation = parser.evaluate(tree)
                self.__Hash[alpha] = Variable(exp, evaluation)

        else: 
            if any(c.isalpha() for c in exp.split('=')[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            else:
                    parser = ParseTree(exp)
                    tree = parser.buildParseTree(exp)
                    evaluation = parser.evaluate(tree)
                    self.__Hash[alpha] = Variable(exp, evaluation)
      
        # print("Updated hash table:", self.__Hash)

    def checkValidity(self, alpha):
        if not alpha.isalpha():
            return True
        return False
