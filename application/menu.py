class MainMenu:
    def __init__(self, options = None):
        self.border_length = 71
        self.border = '*' * self.border_length
        self.options = options
    
    def display_welcome_screen(self):
        print("\n\n")
        # generates welcome screen for users upon entry
        print(self.border)
        print("* ST1507 DSAA: Welcome to: Evaluating & Sorting Assignment Statements".ljust(self.border_length - 1) + "*")
        print("*" + "-" * (self.border_length - 2) + "*")

        print("*".ljust(self.border_length - 1) + "*")
        print("*    - Done by: Teo Wei Qi (231233) & Lee Hong Yi (2223010)".ljust(self.border_length - 1) + "*")
        print("*    - Class DAAA/2B/07".ljust(self.border_length - 1) + "*")
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
            #exit_int is set by main.py, depending on the length of the options array there.
            print(f"\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter")
            exit()
        elif int(selection) == 1:
            print("Function 1 is not implemented yet!")
        elif int(selection) == 2:
            print("Function 2 is not implemented yet!")
        elif int(selection) == 3:
            print("Function 3 is not implemented yet!")
        elif int(selection) == 4:
            print("Function 4 is not implemented yet!")
        elif int(selection) == 5:
            print("Function 5 is not implemented yet!")