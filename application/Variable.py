class Variable:
    def __init__(self, exp, eval):
        self.exp = exp
        self.eval = eval

    def getExp(self):
        return self.exp
    
    def getEval(self):
        return self.eval

    def __str__(self):
        # use :> right-aligning the values within a specified width
        # use :< left-aligning the values within a specified width
        # or use str.format() method
        output = f"{self.exp}=> {self.eval}"
        return output