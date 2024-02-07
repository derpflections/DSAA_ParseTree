# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
This module defines the Variable class which is used to represent a variable within an assignment.
Each variable has an associated expression and an evaluated result. 
'''

class Variable:
    # Initializer or constructor method for the Variable class
    def __init__(self, exp, eval):
        """
        Initializes a new instance of the Variable class.
        
        :param exp: The expression assigned to the variable as a string.
        :param eval: The evaluated result of the expression.
        """
        # Private instance attributes to store the expression and its evaluated result
        self.__exp = exp
        self.__eval = eval

    # Getter method to access the private expression attribute
    def getExp(self):
        """
        Retrieves the expression associated with the variable.
        
        :return: The expression as a string.
        """
        return self.__exp
    
    # Getter method to access the private evaluated result attribute
    def getEval(self):
        """
        Retrieves the evaluated result of the variable's expression.
        
        :return: The evaluated result.
        """
        return self.__eval

    # Special method to provide a string representation of the Variable instance
    def __str__(self):
        """
        Provides a string representation of the Variable instance, showing the expression and its evaluated result.
        
        :return: A string in the format "expression => evaluated result".
        """
        # Formats the output string to show the expression and its evaluation
        output = f"{self.__exp} => {self.__eval}"
        return output
