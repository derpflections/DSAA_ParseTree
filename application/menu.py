# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

"""
menu.py


"""

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
from application.GraphTree import GraphTree
import itertools


class MainMenu:
    def __init__(self, options=None):
        self.border_length = 71
        self.border = "*" * self.border_length
        self.options = options
        self.Hash = HashTable(200)
        self.__historyHook = HistoryHook(self.Hash)
        self.utilities = utilities()
        self.hash_tables = {}
        self.current_hash_name = "Original Hash Table"

    def display_welcome_screen(self):
        utilities.cls()
        print("\n\n")
        # generates welcome screen for users upon entry
        print(self.border)
        print(
            "* ST1507 DSAA: Welcome to: Evaluating & Sorting Assignment Statements".ljust(
                self.border_length - 1
            )
            + "*"
        )
        print("*" + "-" * (self.border_length - 2) + "*")

        print("*".ljust(self.border_length - 1) + "*")
        print(
            "*    - Done by: Teo Wei Qi (2201902) & Lee Hong Yi (2223010)".ljust(
                self.border_length - 1
            )
            + "*"
        )
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
            print(
                "\nPlease select your choice ("
                + ", ".join(f"'{i}'" for i in range(1, len(self.options) + 1))
                + "):"
            )
            for i in range(len(self.options)):
                print(f"\t{i + 1}. {self.options[i]}")
            selection = input("Enter choice: ")
            try:
                if int(selection) in range(1, len(self.options) + 1):
                    invalid_input = False
                else:
                    print(f"Please enter a valid option!\n")
            except ValueError:
                print(f"Please enter a valid option!\n")
        return selection

    def program_navigation(self, selection, exit_int):
        if int(selection) == exit_int:
            # exit_int is set by main.py, depending on the length of the options array there.
            print(
                f"\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter"
            )
            exit()

        elif int(selection) == 1:
            opt1_parseInserter = ParseInserter(self.Hash)
            while True:
                exp = input(
                    "Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n"
                )
                exp = exp.strip()
                if not exp:
                    print("Invalid input. Please provide a valid assignment statement.")
                    continue
                alpha = exp.split("=")[0].strip()
                try:
                    opt1_parseInserter.checkForAlpha(exp, alpha)
                except ValueError:
                    print("Please input a valid expression.")
                    break

                input("\nPress enter to continue...")
                break  # Exit the loop after valid input is provided

        elif int(selection) == 2:
            print("\nCURRENT ASSIGNMENT:\n*******************\n", end="")
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
                    print(
                        f'Value for variable "{eval_var}" is {self.Hash[eval_var].getEval()}'
                    )
                input("\nPress enter to continue...")
                break

        elif int(selection) == 4:
            invalidFile = True
            i = 0
            opt4_parseInserter = ParseInserter(self.Hash)
            while invalidFile:
                target_file = input("Enter the file path: ")
                opt4_fileManipulator = fileManipulator(target_file, "list")
                invalidFile, contents = opt4_fileManipulator.read_contents()
            for exp in contents:
                alpha = exp.split("=")[0].strip()
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
            opt5_fileManipulator = fileManipulator(output=output_file)
            opt5_fileManipulator.write_contents(opt5_evaluator.evaluation().split("\n"))
            # print(self.Hash)

        elif int(selection) == 6:
            while True:
                print(
                    "\nWelcome to Option 6. This option allows you to save your current hashtable and create a new one."
                )
                print("You may load the saved hashtable later on.")

                # if it is the original hash table (1st run of program), do not show name
                if self.current_hash_name != "Original Hash Table":
                    print(f"Name of current hashtable: {self.current_hash_name}\n")

                print("\n1. Create new hashtable")
                print("2. Load saved hashtable")
                print("3. Save/Delete hashtable")
                print("4. Compare current hashtable with saved hashtable")
                print("5. Return to main menu\n")
                sub_selection = input("Enter your choice: ")

                # Create new hashtable
                if sub_selection == "1":
                    print("\nSaved hash tables:")
                    for i, name in enumerate(self.hash_tables):
                        print(f"{i + 1}. {name}")

                    if (
                        self.Hash not in self.hash_tables.values()
                        and self.current_hash_name
                    ):
                        # If the current hashtable is not saved, prompt the user to save it
                        prompt_save = input(
                            "\nDo you want to save the current hashtable? (y/n): "
                        )

                        if prompt_save.lower() == "y":
                            while True:
                                saved_hash_name = input(
                                    "\nEnter the name to save current hashtable: "
                                )
                                # check if name is taken
                                if saved_hash_name in self.hash_tables:
                                    print(
                                        "Name already taken. Please enter another name."
                                    )
                                elif saved_hash_name == "":
                                    print("Invalid input. Please enter a name.")
                                else:
                                    break

                            # Remove the original hash table from the dictionary of saved hashtables
                            if self.current_hash_name == "Original Hash Table":
                                self.hash_tables.pop("Original Hash Table", None)

                            # Add the new hashtable to the dictionary of saved hashtables
                            self.hash_tables[saved_hash_name] = self.Hash
                            # print(f"Updated '{self.hash_tables}'.")
                            print(f"Hashtable saved as '{saved_hash_name}'.")
                        elif prompt_save.lower() == "n":
                            pass
                        else:
                            print("Invalid input. Returning to main menu.")
                            break

                    # Proceed to create a new hashtable
                    new_hash_table = HashTable(100)
                    self.Hash = new_hash_table
                    while True:
                        new_hash_name = input(
                            "\nEnter the name for the new hashtable: "
                        )
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
                        saved_hash_name = input(
                            "\nEnter the name of the hash table to load: "
                        )
                        if saved_hash_name in self.hash_tables:
                            self.Hash = self.hash_tables[saved_hash_name]
                            self.current_hash_name = saved_hash_name
                            print(f"Hashtable '{saved_hash_name}' loaded.")
                            print(
                                "\nCURRENT ASSIGNMENT:\n*******************\n", end=""
                            )
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
                                print(
                                    "Cannot compare the current hashtable with itself."
                                )
                            else:
                                break

                        if original_hash_name in self.hash_tables:
                            # Get the saved hashtable
                            original_hash = self.hash_tables[original_hash_name]
                            # Compare the saved hashtable with the current one
                            if original_hash == self.Hash:
                                print(
                                    "Current hashtable is identical to the saved one."
                                )
                                print("Hashtable:")
                                print(self.Hash)
                                break
                            else:
                                # Print the heading with adjusted width
                                print(
                                    f"\n\n{'Current hashtable':<51}| {'Saved hashtable':<50}|"
                                )
                                print("-" * 51 + "|" + "-" * 51 + "|")

                                # Get all keys from both dictionaries
                                all_keys = set(self.Hash.__getkeys__()) | set(
                                    original_hash.__getkeys__()
                                )
                                # print(sorted(all_keys))

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
                                    max_lines = max(
                                        len(current_lines), len(saved_lines)
                                    )
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

        elif int(selection) == 7:
            final_output_str = ""
            opt7_dependency = DependencyIdentifier(self.Hash)
            dependency_dict = opt7_dependency.parse_assignments()
            dependant_dict = opt7_dependency.find_dependants()
            keyword = ""  # comment
            while True:
                try:
                    option = input(
                        "\nPress 1 to view dependencies.\nPress 2 to view dependants.\nPress 3 to exit.\n>>> "
                    )
                    if int(option) == 1:
                        keyword = "Dependencies"
                        for var_name in dependency_dict:
                            internal_str = ""
                            if len(dependency_dict[var_name]) != 0:
                                internal_str += f"{var_name} depends on:"
                                for dependency in dependency_dict[var_name]:
                                    internal_str += f" {dependency},"
                                internal_str = internal_str[:-1] + "."
                            else:
                                internal_str += f"{var_name} has no dependencies."
                            final_output_str += f"{internal_str} \n"
                    elif int(option) == 2:
                        keyword = "Dependants"
                        for var_name in dependant_dict:
                            internal_str = ""
                            if len(dependant_dict[var_name]) != 0:
                                internal_str += f"{var_name} is depended on by:"
                                for dependant in dependant_dict[var_name]:
                                    internal_str += f" {dependant},"
                                internal_str = internal_str[:-1] + "."
                            else:
                                internal_str += f"{var_name} has no dependants."
                            final_output_str += f"{internal_str} \n"
                    elif int(option) == 3:
                        return
                    else:
                        print("Invalid input. Please try again.\n")
                        return
                    break
                except ValueError:
                    print("Invalid input. Please try again.\n")
            print(f"\n{keyword}:\n*************")
            print(f"{final_output_str}")

        elif int(selection) == 8:
            opt8_dependency = DependencyIdentifier(self.Hash)
            dependency_dict = opt8_dependency.parse_assignments()
            dependant_dict = opt8_dependency.find_dependants()

            variable_name = input("Enter the variable for which you want to generate the graph: ")

            # Check if the variable exists in either dependency or dependant data
            if variable_name not in dependency_dict and variable_name not in dependant_dict:
                print("Variable not found in either dependencies or dependants.")
                return

            # Initialize the graph with the variable of interest as the root node
            graph_root = GraphTree(variable_name, None)
            graph_root.is_root = True

            # Create branches for dependencies and dependants
            dependencies_root = graph_root.add_child("Dependencies")
            dependants_root = graph_root.add_child("Dependants")

            # A helper function to recursively add nodes
            def add_nodes_to_graph(current_node, data_dict):
                for dep in data_dict.get(current_node.name.split(" - ")[0], []):
                    child_node = current_node.add_child(dep)
                    # If dealing with dependencies, check further dependencies to build the graph
                    if dep in dependency_dict:
                        add_nodes_to_graph(child_node, data_dict)

            # Populate the graph with dependency nodes
            add_nodes_to_graph(dependencies_root, dependency_dict)

            # Populate the graph with dependant nodes
            add_nodes_to_graph(dependants_root, dependant_dict)

            # Display the graph
            print(graph_root.display())


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
                    opt9_select = int(
                        input(
                            "Press 1 if you would like to exit.\nPress 2 if you would like to rollback.\n>>> "
                        )
                    )
                    if opt9_select == 1:
                        return
                    elif opt9_select == 2:
                        opt9_2 = int(
                            input(
                                "Enter the version number you would like to rollback to: "
                            )
                        )
                        self.Hash, no_of_rollbacks = self.__historyHook.rollback(opt9_2)
                        if self.Hash == None:
                            print("Invalid input. Please try again.\n")
                            continue
                        else:
                            print(
                                f"Rollback successful. Reverted {no_of_rollbacks} versions."
                            )
                            return
                    else:
                        print("Invalid input. Please try again.\n")
                except ValueError:
                    print("Invalid input. Please try again.\n")


##7261232
