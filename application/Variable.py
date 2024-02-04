# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
Variable.py
'''

class Variable:
    def __init__(self, exp, eval):
        self.__exp = exp
        self.__eval = eval

    def getExp(self):
        return self.__exp
    
    def getEval(self):
        return self.__eval

    def __str__(self):
        output = f"{self.exp}=> {self.eval}"
        return output