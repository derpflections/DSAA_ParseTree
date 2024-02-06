# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

'''
menu.py


'''

# from BinaryTree import BinaryTree
# from Stack import Stack
from application.Variable import Variable
from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.ParseInsert import ParseInserter
from application.HistoryLogger import HistoryHook
from application.FileReader import fileManipulator
from application.AssignmentEvaluator import AssignmentEvaluator
from application.DependencyIdentifier import DependencyIdentifier
from application.utility import utilities

class MainMenu:
    def __init__(self, options = None):
        self.border_length = 71
        self.border = '*' * self.border_length
        self.options = options
        self.Hash = HashTable(100)
        self.__historyHook = HistoryHook(self.Hash)
        self.utilities = utilities()
    
    def display_welcome_screen(self):
        utilities.cls()
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
        self.__historyHook.logger(self.Hash)
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
                exp = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
                exp = exp.strip()
                if not exp:
                    print("Invalid input. Please provide a valid assignment statement.")
                    continue
                alpha = exp.split('=')[0].strip()
                try:
                    opt1_parseInserter.checkForAlpha(exp, alpha)
                except ValueError:
                    print("Please input a valid expression.")
                    break
                input("\nPress enter to continue...")
                break  # Exit the loop after valid input is provided


        elif int(selection) == 2:
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end='')
            print(self.Hash)
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
            invalidFile = True
            i = 0
            opt4_parseInserter = ParseInserter(self.Hash)
            while invalidFile:
                    target_file = input("Enter the file path: ")
                    opt4_fileManipulator = (fileManipulator(target_file, 'list'))
                    invalidFile, contents = opt4_fileManipulator.read_contents()
            for exp in contents:
                alpha = exp.split('=')[0].strip()
                if opt4_parseInserter.checkValidity(exp, alpha):
                    i += 1
                    continue
                opt4_parseInserter.checkForAlpha(exp, alpha)
            if i > 0:
                print(f"Warning, {i} invalid assignments were found and skipped.")
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end='')
            
            for id in self.Hash.__getkeys__():
                opt4_parseInserter.checkForAlpha(self.Hash[id].getExp(), id)
            
            print(self.Hash)
            input("\nPress enter to continue...")


        elif int(selection) == 5:
            output_file = input("Please enter output file: ")
            opt5_evaluator = AssignmentEvaluator(self.Hash)
            opt5_fileManipulator = fileManipulator(output = output_file)
            opt5_fileManipulator.write_contents(opt5_evaluator.evaluation().split('\n'))
            # print(self.Hash)
    
        elif int(selection) == 6:
            pass

        elif int(selection) == 7:
            final_output_str = ""
            opt7_dependency = DependencyIdentifier(self.Hash)
            dependency_list = opt7_dependency.parse_assignments()
            for var_name in dependency_list:
                internal_str = ""
                if len(dependency_list[var_name]) != 0:
                    internal_str += f"{var_name} depends on:"
                    for dependency in dependency_list[var_name]:
                        internal_str += f" {dependency},"
                    internal_str = internal_str[:-1] + "."
                else:
                    internal_str += f"{var_name} has no dependencies."
                final_output_str += f"{internal_str} \n"
            print("\n\nDependencies:\n*************")
            print(f"{final_output_str}")

        elif int(selection) == 8:
            pass
        elif int(selection) == 9:
            opt9_criteria = True
            history, timestamps = self.__historyHook.displayer()
            utilities.cls()
            print("Assignment History:")
            for i in range(len(history)):
                if i == len(history) - 1:
                    print(f"Time: {timestamps[i]}, iteration {i} (latest)")
                else:
                    print(f"Time: {timestamps[i]}, iteration {i}")
                print(history[i])
                print("\n")
            while opt9_criteria:
                try:
                    opt9_select = int(input("Press 1 if you would like to exit.\nPress 2 if you would like to rollback.\n>>> "))                
                    if opt9_select == 1:
                        return
                    elif opt9_select == 2:
                        opt9_2 = int(input("Enter the version number you would like to rollback to: "))
                        self.Hash, no_of_rollbacks = self.__historyHook.rollback(opt9_2)
                        if self.Hash == None:
                            print("Invalid input. Please try again.\n")
                            continue
                        else:
                            print(f"Rollback successful. Reverted {no_of_rollbacks} versions.")
                            return
                    else:
                        print("Invalid input. Please try again.\n")
                except ValueError:
                    print("Invalid input. Please try again.\n")



##7261232
