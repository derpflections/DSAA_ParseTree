# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

"""
menu.py

This module serves as the entry point for the ST1507 DSAA Assignment Statement Evaluator & Sorter application. 
It integrates various components such as parsing, evaluation, and visualization of assignment statements 
to provide a comprehensive tool for analyzing and managing programming assignments.

The application features a menu-driven interface that allows users to:
- Add or modify assignment statements directly or through file input.
- Display current assignment statements stored in the hash table.
- Evaluate expressions and compute their values.
- Save the current state of assignment statements to a file.
- Load assignment statements from a file and integrate them into the application.
- Manage multiple versions of hash tables for different sets of assignment statements.
- Analyze dependencies among variables to understand their relationships.
- Visualize the dependency graph for a specific variable.
- View and rollback to previous states of the application using a history management feature.

"""

from application.Variable import Variable
from application.ParseTree import ParseTree
from application.HashTable import HashTable
from application.ParseInsert import ParseInserter
from application.HistoryLogger import HistoryHook
from application.FileReader import fileManipulator
from application.AssignmentEvaluator import AssignmentEvaluator
from application.DependencyIdentifier import DependencyIdentifier
from application.utility import utilities
from application.GraphTree import GraphTree
import itertools


class MainMenu:
    def __init__(self, options=None): # done by Hong Yi
        # Initialize the MainMenu class with default and dynamic attributes.
        self.border_length = 71  # Defines the length of the border for the welcome screen.
        self.border = "*" * self.border_length  # Creates a string of asterisks to use as a border in the UI.
        self.options = options  # A list of menu options provided to the class instance.
        self.Hash = HashTable(200)  # Initializes a HashTable object with a specified size for storing assignment statements.
        self.__historyHook = HistoryHook(self.Hash)  # Initializes a history logger to track changes in the hash table.
        self.utilities = utilities()  # Initializes a utilities object for miscellaneous helper functions.
        self.hash_tables = {}  # A dictionary to manage multiple hash tables, if needed.
        self.current_hash_name = "Original Hash Table"  # Default name for the initially created hash table.

    # Display the welcome screen to the user.
    def display_welcome_screen(self): # done by Hong Yi
        utilities.cls()  # Clears the console screen for a clean display.
        print("\n")
        # Prints the welcome screen, framed by borders, and includes project and author information.
        print(self.border)
        print("* ST1507 DSAA: Welcome to: Evaluating & Sorting Assignment Statements".ljust(self.border_length - 1) + "*")
        print("*" + "-" * (self.border_length - 2) + "*")
        print("*".ljust(self.border_length - 1) + "*")
        print("*    - Done by: Teo Wei Qi (2201902) & Lee Hong Yi (2223010)".ljust(self.border_length - 1) + "*")
        print("*    - Class: DAAA/2B/07".ljust(self.border_length - 1) + "*")
        print("*".ljust(self.border_length - 1) + "*")
        print(self.border)
        print("\n")

    # Display the main menu and handle user selection.
    def display_main_menu(self): # done by Hong Yi
        # Logs the current state of the hash table for history tracking.
        self.__historyHook.logger(self.Hash)
        invalid_input = True
        while invalid_input:
            # Prompt the user to select an option from the menu.
            print("\nPlease select your choice (" + ", ".join(f"'{i}'" for i in range(1, len(self.options) + 1)) + "):")
            for i in range(len(self.options)):
                print(f"\t{i + 1}. {self.options[i]}")
            selection = input("Enter choice: ")
            try:
                # Validates the user's selection to ensure it's within the range of available options.
                if int(selection) in range(1, len(self.options) + 1):
                    invalid_input = False
                else:
                    print(f"Please enter a valid option!\n")
            except ValueError:
                # Catches and handles the case where the input is not a number.
                print(f"Please enter a valid option!\n")
        return selection

    # Navigate to the appropriate program function based on user selection.
    def program_navigation(self, selection, exit_int): # done by Hong Yi
        if int(selection) == exit_int:
            # Handles the case where the user chooses to exit the application.
            print(f"\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter")
            exit()

        elif int(selection) == 1: #done by Wei Qi
            opt1_parseInserter = ParseInserter(self.Hash)
            # Enter an infinite loop to prompt the user for input until valid data is provided or an action is completed.
            while True:
                # Prompt the user to input an assignment statement to add or modify.
                exp = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
                # Strip leading and trailing whitespace from the input for clean processing.
                exp = exp.strip()

                # Check if the input is empty after stripping whitespace. If so, prompt again.
                if not exp:
                    print("Invalid input. Please provide a valid assignment statement.")
                    continue  # Restart the loop, asking for input again.
                # Extract the variable part (left of the '=') of the assignment statement.
                # This is used to validate the variable name according to specific rules (e.g., alphabetic characters).
                alpha = exp.split("=")[0].strip()
                try:
                    # Attempt to check if the variable name is valid and if the expression can be parsed.
                    # This method may throw a ValueError if the expression is invalid or doesn't meet the criteria.
                    opt1_parseInserter.checkForAlpha(exp, alpha)
                except ValueError:
                    # If an exception is caught, notify the user and break out of the loop to stop prompting for input.
                    print("Please input a valid expression.")
                    break  # Exit the loop since an invalid expression was entered.
                
                # After a successful operation (valid input and no exceptions), prompt the user to press enter to continue.
                input("\nPress enter to continue...")
                break  # Exit the loop after valid input is provided, moving on to the next part of the program.

        elif int(selection) == 2: #done by Wei Qi
            # This option displays all current assignment statements stored in the hash table.
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end="")
            print(self.Hash)  # Print the contents of the hash table representing current assignments.
            input("\nPress enter to continue...")  # Pause execution until the user acknowledges by pressing enter.

        elif int(selection) == 3: #done by Wei Qi
            # This option allows the user to evaluate a specific variable's expression.
            while True:
                eval_var = input("Enter the variable you want to evaluate:\n")  # Prompt for variable name.
            
                if self.Hash[eval_var] == None:  # Check if the variable is not found in the hash table.
                    print("Variable not found!")
                    continue  # Prompt again if variable not found.
                else:
                    exp = self.Hash[eval_var].getExp()  # Get the expression associated with the variable.
                    parser = ParseTree(exp)  # Initialize a parse tree for the expression.
                    tree = parser.buildParseTree(exp)  # Build the parse tree from the expression.
                    print("\nExpression Tree:")  # Print the expression tree.
                    tree.printInorder(0)  # Display the tree in an inorder traversal.
                    # Display the evaluated result of the variable's expression.
                    print(f'Value for variable "{eval_var}" is {self.Hash[eval_var].getEval()}')
                input("\nPress enter to continue...")  # Pause execution for user acknowledgment.
                break  # Exit the loop after successful evaluation.

        elif int(selection) == 4: # done by Hong Yi
            # This option handles importing assignment statements from a specified file.
            invalidFile = True
            i = 0  # Counter for invalid assignments found in the file.
            opt4_parseInserter = ParseInserter(self.Hash)  # Initialize ParseInserter with the current hash table.

            while invalidFile:
                target_file = input("Enter the file path: ")  # Prompt for the file path.
                opt4_fileManipulator = fileManipulator(target_file, "list")  # Initialize file manipulator for the file.
                invalidFile, contents = opt4_fileManipulator.read_contents()  # Read the contents of the file.

            # Process each expression found in the file.
            for exp in contents:
                alpha = exp.split("=")[0].strip()  # Extract the variable part of the assignment.
                # Check the validity of the expression and its brackets.
                if opt4_parseInserter.checkValidity(exp, alpha) or opt4_parseInserter.checkBrackets(exp):
                    i += 1  # Increment invalid assignments counter.
                    continue  # Skip processing this expression.
                opt4_parseInserter.checkForAlpha(exp, alpha)  # Insert the valid expression into the hash table.

            if i > 0:
                # Warn the user if any invalid assignments were skipped during the import.
                print(f"Warning, {i} invalid assignments were found and skipped.")
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end='')  # Display the current state of assignments.

            # Revalidate and insert all assignments again to ensure correctness.
            for id in self.Hash.__getkeys__():
                opt4_parseInserter.checkForAlpha(self.Hash[id].getExp(), id)

            print(self.Hash)  # Print the updated hash table with imported assignments.
            input("\nPress enter to continue...")  # Pause execution for user acknowledgment.

        elif int(selection) == 5: # done by Hong Yi
            # This option exports the evaluated results of all variables to a specified output file.
            output_file = input("Please enter output file: ")  # Prompt for the output file path.
            opt5_evaluator = AssignmentEvaluator(self.Hash)  # Initialize the evaluator with the current hash table.
            opt5_fileManipulator = fileManipulator(output=output_file)  # Initialize file manipulator for output.
            # Write the evaluated results to the output file, splitting the string into lines.
            opt5_fileManipulator.write_contents(opt5_evaluator.evaluation().split("\n"))

        elif int(selection) == 6: #done by Wei Qi
            while True:
                # Display the main menu for Option 6
                print("\nWelcome to Option 6. This option allows you to save your current hashtable and create a new one.")
                print("You may load the saved hashtable later on.")

                # If it is not the original hash table, display its name
                if self.current_hash_name != "Original Hash Table":
                    print(f"Name of current hashtable: {self.current_hash_name}\n")

                # Display available options
                print("\n1. Create new hashtable")
                print("2. Load saved hashtable")
                print("3. Save/Delete hashtable")
                print("4. Compare current hashtable with saved hashtable")
                print("5. Return to the main menu\n")

                # Get user's choice
                sub_selection = input("Enter your choice: ")

                # Create new hashtable
                if sub_selection == "1":
                    print("\nSaved hash tables:")
                    for i, name in enumerate(self.hash_tables):
                        print(f"{i + 1}. {name}")

                    # Check if the current hashtable is not saved and prompt the user to save it
                    if self.Hash not in self.hash_tables.values() and self.current_hash_name:
                        prompt_save = input("\nDo you want to save the current hashtable? (y/n): ")

                        if prompt_save.lower() == "y":
                            while True:
                                saved_hash_name = input("\nEnter the name to save the current hashtable: ")
                                # Check if the name is already taken
                                if saved_hash_name in self.hash_tables:
                                    print("Name already taken. Please enter another name.")
                                elif saved_hash_name == "":
                                    print("Invalid input. Please enter a name.")
                                else:
                                    break
                                
                            # Remove the original hash table from the dictionary of saved hashtables
                            if self.current_hash_name == "Original Hash Table":
                                self.hash_tables.pop("Original Hash Table", None)

                            # Add the new hashtable to the dictionary of saved hashtables
                            self.hash_tables[saved_hash_name] = self.Hash
                            print(f"Hashtable saved as '{saved_hash_name}'.")
                        elif prompt_save.lower() == "n":
                            pass
                        else:
                            print("Invalid input. Returning to the main menu.")
                            break
                        
                    # Proceed to create a new hashtable
                    new_hash_table = HashTable(100)
                    self.Hash = new_hash_table
                    while True:
                        new_hash_name = input("\nEnter the name for the new hashtable: ")
                        if new_hash_name == "":
                            print("Invalid input. Please enter a name.")
                        elif new_hash_name in self.hash_tables:
                            print("Name already taken. Please enter another name.")
                        else:
                            break
                        
                    # Update the name of the current hashtable
                    self.current_hash_name = new_hash_name
                    # Add the new hashtable to the dictionary of saved hashtables
                    self.hash_tables[new_hash_name] = self.Hash
                    print("New hashtable created.")
                    input("\nPress enter to continue...")
               # Load saved hashtable
                elif sub_selection == "2":
                    # If there are no saved hashtables, prompt the user to create one
                    if len(self.hash_tables) == 0:
                        print("No saved hashtable found.")
                        print("Please create and save a hashtable first.")
                    else:
                        print("\nSaved hash tables:")
                        for i, name in enumerate(self.hash_tables):
                            print(f"{i + 1}. {name}")
                        saved_hash_name = input("\nEnter the name of the hash table to load: ")
                        if saved_hash_name in self.hash_tables:
                            self.Hash = self.hash_tables[saved_hash_name]
                            self.current_hash_name = saved_hash_name
                            print(f"Hashtable '{saved_hash_name}' loaded.")
                            print("\nCURRENT ASSIGNMENT:\n*******************\n", end="")
                            print(self.Hash)
                        else:
                            print("Hash Table not found.")
                    input("\nPress enter to continue...")

                # Save/delete current hashtable
                elif sub_selection == "3":
                    if (
                        self.current_hash_name == "Original Hash Table"
                        or self.Hash not in self.hash_tables.values()
                        or self.current_hash_name not in self.hash_tables
                    ):
                        while True:
                            saved_hash_name = input(
                                "Enter the name to save current hashtable: "
                            )
                            if saved_hash_name in self.hash_tables:
                                print("Name already taken. Please enter another name.")
                            elif saved_hash_name == "":
                                print("Invalid input. Please enter a name.")
                            else:
                                break
                            
                        self.hash_tables[saved_hash_name] = self.Hash
                        self.current_hash_name = saved_hash_name
                        print(f"{saved_hash_name} saved.")
                    elif self.current_hash_name in self.hash_tables:
                        delete_choice = input(
                            f"Do you want to delete '{self.current_hash_name}'? (y/n): "
                        )
                        if delete_choice.lower() == "y":
                            self.hash_tables.pop(self.current_hash_name, None)

                            print(f"Hashtable '{self.current_hash_name}' deleted.")
                            self.current_hash_name = "Original Hash Table"
                            print("Current hashtable is now the original hashtable.")
                        elif delete_choice.lower() == "n":
                            pass
                        else:
                            print("Invalid input. Returning to main menu.")
                            break
                        
                    input("\nPress enter to continue...")
                
                # Compare current hashtable with saved hashtable
                elif sub_selection == "4":
                    if self.current_hash_name == "Original Hash Table":
                        print("Current hashtable is the original hashtable.")
                        print("Please create and save a new hashtable first.")
                    elif len(self.hash_tables) == 0 or len(self.hash_tables) == 1:
                        print("No saved hashtable found or only 1 hashtable is saved.")
                        print("Please create and save a hashtable first.")
                    else:
                        print("\nSaved hash tables:")
                        for i, name in enumerate(self.hash_tables):
                            print(f"{i + 1}. {name}")
                        while True:
                            original_hash_name = input(
                                "Enter the name of the hash table you would like to compare: "
                            )
                            if original_hash_name == self.current_hash_name:
                                print("Cannot compare the current hashtable with itself.")
                            else:
                                break
                            
                        if original_hash_name in self.hash_tables:
                            # Get the saved hashtable
                            original_hash = self.hash_tables[original_hash_name]

                            # Compare the saved hashtable with the current one
                            if original_hash == self.Hash:
                                print("Current hashtable is identical to the saved one.")
                                print("Hashtable:")
                                print(self.Hash)
                                break
                            else:
                                # Print the heading with adjusted width
                                print(f"\n{'Current hashtable':<51}| {'Saved hashtable':<50}|")
                                print("-" * 51 + "|" + "-" * 51 + "|")

                                # Get all keys from both dictionaries
                                all_keys = set(self.Hash.__getkeys__()) | set(
                                    original_hash.__getkeys__()
                                )

                                # Iterate over keys
                                for key in sorted(all_keys):
                                    # Get values or empty string if key does not exist
                                    current_value = str(self.Hash[key])
                                    saved_value = str(original_hash[key])

                                    # Split values into lines if necessary
                                    current_lines = [
                                        current_value[i : i + 50]
                                        for i in range(0, len(current_value), 50)
                                    ]
                                    saved_lines = [
                                        saved_value[i : i + 50]
                                        for i in range(0, len(saved_value), 50)
                                    ]

                                    # Print values side by side
                                    max_lines = max(len(current_lines), len(saved_lines))
                                    for i in range(max_lines):
                                        current_line = (
                                            current_lines[i]
                                            if i < len(current_lines)
                                            else ""
                                        )
                                        saved_line = (
                                            saved_lines[i]
                                            if i < len(saved_lines)
                                            else ""
                                        )
                                        print(f"{current_line:<50} | {saved_line:<50}|")

                        else:
                            print("No such hash table exists.")

                    input("\nPress enter to continue...")

                elif sub_selection == "5":
                    break

        elif int(selection) == 7: # done by Hong Yi
            # Initialize an empty string to hold the final output for display.
            final_output_str = ""
            # Instantiate a DependencyIdentifier object with the current HashTable.
            opt7_dependency = DependencyIdentifier(self.Hash)
            # Parse assignments to identify all dependencies among variables.
            dependency_dict = opt7_dependency.parse_assignments()
            # Identify which variables are dependants of other variables.
            dependant_dict = opt7_dependency.find_dependants()
            # Initialize an empty string to later specify what type of data we are dealing with (Dependencies or Dependants).
            keyword = ""

            # Loop indefinitely until the user makes a valid selection or chooses to exit.
            while True:
                try:
                    # Prompt the user for their choice on what information to view.
                    option = input("\nPress 1 to view dependencies.\nPress 2 to view dependants.\nPress 3 to exit.\n>>> ")

                    if int(option) == 1:
                        keyword = "Dependencies"  # Set the keyword to indicate we're dealing with dependencies.
                        # Iterate through each variable in the dependency dictionary.
                        for var_name in dependency_dict:
                            internal_str = ""  # Initialize a string to build the output for this variable.
                            if len(dependency_dict[var_name]) != 0:
                                # If the variable has dependencies, construct a string listing them.
                                internal_str += f"{var_name} depends on:"
                                for dependency in dependency_dict[var_name]:
                                    internal_str += f" {dependency},"
                                internal_str = internal_str[:-1] + "."  # Remove the last comma and end with a period.
                            else:
                                # If the variable has no dependencies, note that in the string.
                                internal_str += f"{var_name} has no dependencies."
                            final_output_str += f"{internal_str} \n"  # Add this variable's string to the final output.

                    elif int(option) == 2:
                        keyword = "Dependants"  # Set the keyword to indicate we're dealing with dependants.
                        # Iterate through each variable in the dependant dictionary.
                        for var_name in dependant_dict:
                            internal_str = ""  # Initialize a string to build the output for this variable.
                            if len(dependant_dict[var_name]) != 0:
                                # If the variable has dependants, construct a string listing them.
                                internal_str += f"{var_name} is depended on by:"
                                for dependant in dependant_dict[var_name]:
                                    internal_str += f" {dependant},"
                                internal_str = internal_str[:-1] + "."  # Remove the last comma and end with a period.
                            else:
                                # If the variable has no dependants, note that in the string.
                                internal_str += f"{var_name} has no dependants."
                            final_output_str += f"{internal_str} \n"  # Add this variable's string to the final output.

                    elif int(option) == 3:
                        return  # Exit the feature if the user chooses to do so.

                    else:
                        # If the input doesn't match any of the valid options, notify the user and restart the loop.
                        print("Invalid input. Please try again.\n")
                        return

                    break  # Break the loop if a valid option was chosen.

                except ValueError:
                    # If the input cannot be converted to an integer, notify the user and restart the loop.
                    print("Invalid input. Please try again.\n")

            # Print the constructed string containing either the dependencies or dependants as chosen by the user.
            print(f"\n{keyword}:\n*************")
            print(f"{final_output_str}")

            # Prompt the user to press enter to continue, indicating readiness to return to the main menu.
            input("\nPress enter to continue and return to the main menu...")


        elif int(selection) == 8: #done by Wei Qi
            # Initialize DependencyIdentifier with the current HashTable to analyze dependencies.
            opt8_dependency = DependencyIdentifier(self.Hash)
            # Parse the current assignments to identify all dependencies.
            dependency_dict = opt8_dependency.parse_assignments()
            # Identify which variables depend on the given variable.
            dependant_dict = opt8_dependency.find_dependants()

            # Prompt the user to input the variable name for which the dependency graph will be generated.
            variable_name = input("Enter the variable for which you want to generate the graph: ")

            # Check if the entered variable name exists in either the dependency or dependant dictionaries.
            if variable_name not in dependency_dict and variable_name not in dependant_dict:
                print("Variable not found.")  # If not found, inform the user and exit this option.
                return

            # Initialize the root of the graph with the specified variable name. This node represents the variable itself.
            graph_root = GraphTree(variable_name, None)
            graph_root.is_root = True

            # Create nodes for Dependencies and Dependants under the root to categorize the relationships.
            dependencies_node = graph_root.add_child("Dependencies")
            dependants_node = graph_root.add_child("Dependants")

            # Populate the Dependencies node with all variables that the selected variable depends on.
            if variable_name in dependency_dict:
                for dependency in dependency_dict[variable_name]:
                    dependencies_node.add_child(dependency)

            # Populate the Dependants node with all variables that depend on the selected variable.
            if variable_name in dependant_dict:
                for dependant in dependant_dict[variable_name]:
                    dependants_node.add_child(dependant)

            # Display the generated graph to the user, illustrating the dependencies and dependants.
            print(graph_root.display())

        elif int(selection) == 9: # done by Hong Yi
            # Flag to control the display and interaction with the assignment history.
            opt9_criteria = True
            # Retrieve the history of assignments and their timestamps from the HistoryHook.
            history, timestamps = self.__historyHook.displayer()
            # Clear the screen for a clean display of the history.
            utilities.cls()
            # Print each entry in the assignment history along with its timestamp.
            print("Assignment History:")
            for i in range(len(history)):
                if i == len(history) - 1:
                    print(f"Time: {timestamps[i]}, iteration {i} (latest)")  # Mark the latest iteration for clarity.
                else:
                    print(f"Time: {timestamps[i]}, iteration {i}")
                print(history[i])
                print("\n")
            
            # Loop to handle user input for history management actions.
            while opt9_criteria:
                try:
                    # Prompt the user to choose between exiting or rolling back to a previous version.
                    opt9_select = int(input("Press 1 if you would like to exit.\nPress 2 if you would like to rollback.\n>>> "))
                    if opt9_select == 1:
                        return  # Exit the history management option.
                    elif opt9_select == 2:
                        # Prompt the user for the version number to rollback to.
                        opt9_2 = int(input("Enter the version number you would like to rollback to: "))
                        # Attempt the rollback operation and update the hash table to the selected version.
                        self.Hash, no_of_rollbacks = self.__historyHook.rollback(opt9_2)
                        if self.Hash == None:
                            print("Invalid input. Please try again.\n")  # Handle invalid version number input.
                            continue
                        else:
                            # Inform the user of a successful rollback and the number of versions reverted.
                            print(f"Rollback successful. Reverted {no_of_rollbacks} versions.")
                            return
                    else:
                        print("Invalid input. Please try again.\n")  # Handle any other invalid inputs.
                except ValueError:
                    # Catch and handle non-integer inputs for the selection.
                    print("Invalid input. Please try again.\n")


##7261232
