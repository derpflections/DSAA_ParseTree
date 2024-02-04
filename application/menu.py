# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
menu.py


'''

# from BinaryTree import BinaryTree
# from Stack import Stack
from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.Variable import Variable
from application.FileReader import fileReader
from application.AssignmentEvaluator import AssignmentEvaluator

def checkForAlpha(self, exp, alpha):
    exp = exp.strip()
    exp = exp.replace(" ", "")

    if any(key in exp for key in self.Hash.__getkeys__()):
        replaced_exp = exp
                    
        for key in self.Hash.__getkeys__():
            if key in replaced_exp.split('=')[1].strip():
                value = self.Hash.__getitem__(key).getEval()
                replaced_exp = replaced_exp.replace(key, str(value))
                # print(replaced_exp)
                    
        if any(c.isalpha() for c in replaced_exp.split('=')[1].strip()):
            evaluation = None
            self.Hash[alpha] = Variable(exp, evaluation)

        else:    
            parser = ParseTree(replaced_exp)
            tree = parser.buildParseTree(replaced_exp)
            evaluation = parser.evaluate(tree)
            self.Hash[alpha] = Variable(exp, evaluation)

    else: 
        parser = ParseTree(exp)
        tree = parser.buildParseTree(exp)
        evaluation = parser.evaluate(tree)
        self.Hash[alpha] = Variable(exp, evaluation)
    
class MainMenu:
    def __init__(self, options = None):
        self.border_length = 71
        self.border = '*' * self.border_length
        self.options = options
        self.Hash = HashTable(26)
    
    def display_welcome_screen(self):
        print("\n\n")
        # generates welcome screen for users upon entry
        print(self.border)
        print("* ST1507 DSAA: Welcome to: Evaluating & Sorting Assignment Statements".ljust(self.border_length - 1) + "*")
        print("*" + "-" * (self.border_length - 2) + "*")

        print("*".ljust(self.border_length - 1) + "*")
        print("*    - Done by: Teo Wei Qi (2201902) & Lee Hong Yi (2223010)".ljust(self.border_length - 1) + "*")
        print("*    - Class: DAAA/2B/07".ljust(self.border_length - 1) + "*")
        print("*".ljust(self.border_length - 1) + "*")
        print(self.border)
        print("\n\n")

    def display_main_menu(self):
        # prints main menu, and handles user input when attempting to access the program's function.
        invalid_input = True
        while invalid_input:
            selection = 0   
            print("\nPlease select your choice (" + ', '.join(f"'{i}'" for i in range(1, len(self.options) + 1)) + "):")
            for i in range(len(self.options)):
                print(f"\t{i + 1}. {self.options[i]}")
            selection = input("Enter choice: ")
            try:
                if int(selection) in range (1, len(self.options) + 1):
                    invalid_input = False
                else:
                    print(f"Please enter a valid option!\n")
            except ValueError:
                    print(f"Please enter a valid option!\n")
        return selection
    
    def program_navigation(self, selection, exit_int):
        if int(selection) == exit_int:
            # exit_int is set by main.py, depending on the length of the options array there.
            print(f"\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter")
            exit()

        elif int(selection) == 1:
            while True:
                exp = input("Enter the assignment statement you want to modify:\nFor example, a=(1+2)\n")
                if not exp.strip():
                    print("Invalid input. Please provide a valid assignment statement.")
                    continue
                
                alpha = exp.split('=')[0].strip()
                # print(alpha)

                checkForAlpha(self, exp, alpha)

                # print(evaluation) # remove this line when you are done with the program
                input("\nPress enter to continue...")
                break  # Exit the loop after valid input is provided


        elif int(selection) == 2:
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end='')

            # Check if any value in the hashtable is None
            for id in self.Hash.__getkeys__():
                # print(f"{self.Hash[id].getExp()}")
                checkForAlpha(self, self.Hash[id].getExp(), id)

            for id in self.Hash.__getkeys__():
                checkForAlpha(self, self.Hash[id].getExp(), id)

                if self.Hash[id] != None:
                    print(f"{self.Hash[id]}")
            input("\nPress enter to continue...")

        elif int(selection) == 3:
            while True:
                eval_var = input("Enter the variable you want to evaluate:\n")
                
                if self.Hash[eval_var] == None:
                    print("Variable not found!")
                    continue
                else:
                    exp = self.Hash[eval_var].getExp()
                    parser = ParseTree(exp)
                    tree = parser.buildParseTree(exp)
                    print("\nExpression Tree:")
                    tree.printInorder(0)
                    print(f'Value for variable "{eval_var}" is {self.Hash[eval_var].getEval()}')
                input("\nPress enter to continue...")
                break


        elif int(selection) == 4:
            target_file = input("Enter the file path: ")
            opt4_fileReader = (fileReader(target_file, 'list'))
            contents = opt4_fileReader.read_contents()
            print(contents)
            for expression in contents:
                parser = ParseTree(expression)
                evaluation = parser.evaluate(parser.buildParseTree(expression))
                alpha = expression.strip()[0]
                self.Hash[alpha] = Variable(expression, evaluation)
            print("\nCURRENT ASSIGNMENT:\n*******************")
            for id in self.Hash.__getkeys__():
                if self.Hash[id] != None:
                    print(f"{self.Hash[id]}")               
        elif int(selection) == 5:
            opt5_evaluator = AssignmentEvaluator(self.Hash)
            print(self.Hash)