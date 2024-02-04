class Variable:
    def __init__(self, exp, eval):
        self.__exp = exp
        self.__eval = eval

    def getExp(self):
        return self.__exp
    
    def getEval(self):
        return self.__eval

    def __str__(self):
        # use :> right-aligning the values within a specified width
        # use :< left-aligning the values within a specified width
        # or use str.format() method
        output = f"{self.__exp}=> {self.__eval}"
        return output