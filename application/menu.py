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
from application.FileReader import fileManipulator
from application.AssignmentEvaluator import AssignmentEvaluator
from application.ParseInsert import ParseInserter

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
            opt1_parseInserter = ParseInserter(self.Hash)
            while True:
                exp = input("Enter the assignment statement you want to modify:\nFor example, a=(1+2)\n")
                if not exp.strip():
                    print("Invalid input. Please provide a valid assignment statement.")
                    continue
                alpha = exp.split('=')[0].strip()
                opt1_parseInserter.checkForAlpha(exp, alpha)
                # print(evaluation) # remove this line when you are done with the program
                input("\nPress enter to continue...")
                break  # Exit the loop after valid input is provided


        elif int(selection) == 2:
            opt2_parseInserter = ParseInserter(self.Hash)
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end='')
            # Check if any value in the hashtable is None
            for id in self.Hash.__getkeys__():
                # print(f"{self.Hash[id].getExp()}")
                opt2_parseInserter.checkForAlpha(self.Hash[id].getExp(), id)
            for id in sorted(self.Hash.__getkeys__()):
                opt2_parseInserter.checkForAlpha(self.Hash[id].getExp(), id)
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
            opt4_parseInserter = ParseInserter(self.Hash)
            invalidFile = True
            invalidContent = True
            while invalidContent:
                while invalidFile:
                    target_file = input("Enter the file path: ")
                    opt4_fileManipulator = (fileManipulator(target_file, 'list'))
                    invalidFile, contents = opt4_fileManipulator.read_contents()
                for expression in contents:
                    try:
                        alpha = expression.split('=')[0].strip()
                        invalidContent = opt4_parseInserter.checkForAlpha(expression, alpha)
                    except IndexError:
                        print("Invalid input. Please provide a valid assignment statement.")
                        invalidContent, invalidFile = True, True
                        break
                    except Exception as e:
                        print(f"Unknown error occurred. Please try again later.\n Debug info: {e}")
                        invalidContent, invalidFile = True, True
                        break
            print("\nCURRENT ASSIGNMENT:\n*******************")
            for id in self.Hash.__getkeys__():
                if self.Hash[id] != None:
                    print(f"{self.Hash[id]}") 
        elif int(selection) == 5:
            output_file = input("Please enter output file: ")
            opt5_evaluator = AssignmentEvaluator(self.Hash)
            opt5_fileManipulator = fileManipulator(output = output_file)
            opt5_fileManipulator.write_contents(opt5_evaluator.evaluation().split('\n'))
            # print(self.Hash)
    


##726132