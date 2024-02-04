from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.Variable import Variable


class ParseInserter():
    def __init__(self, hashTable):
        self.__Hash = hashTable

    def checkForAlpha(self, exp, alpha):
        if any(key in exp for key in self.__Hash.__getkeys__()):
            replaced_exp = exp
            for key in self.__Hash.__getkeys__():
                if key in replaced_exp.split('=')[1]:
                    value = self.__Hash.__getitem__(key).getEval()
                    replaced_exp = replaced_exp.replace(key, str(value))
                    # print(replaced_exp)

            if any(c.isalpha() for c in replaced_exp.split('=')[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)

            else:
                try:
                    parser = ParseTree(replaced_exp)
                    tree = parser.buildParseTree(replaced_exp)
                    evaluation = parser.evaluate(tree)
                    self.__Hash[alpha] = Variable(exp, evaluation)
                    return False
                except AttributeError:
                    print("Invalid input. Please provide a valid assignment statement.")
                    return True

        else: 
            # first run of the program shouldn't have any variables on the right hand side
            if any(c.isalpha() for c in exp.split('=')[1]):
                evaluation = None
                self.__Hash[alpha] = Variable(exp, evaluation)
            else:
                parser = ParseTree(exp)
                tree = parser.buildParseTree(exp)
                evaluation = parser.evaluate(tree)
                self.__Hash[alpha] = Variable(exp, evaluation)
    
    def checkValidity(self, alpha):
        if alpha.isalpha() == False:
            return True
        else:
            return False
