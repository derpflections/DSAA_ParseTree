# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

import os

class fileManipulator(): # done by Hong Yi
    """
    A utility class for manipulating files, including reading and writing contents.

    Attributes:
        __input (str): The path to the input file.
        __output (str): The path to the output file.
    """

    def __init__(self, input='', output=''):
        """
        Initialize the fileManipulator with paths to an input and output file.
        
        Args:
            input (str, optional): Path to the input file. Defaults to ''.
            output (str, optional): Path to the output file. Defaults to ''.
        """
        self.__input = input
        self.__output = output

    def read_contents(self, type='list'):
        """
        Reads the contents of the input file and returns them as either a list or a dictionary.
        
        Args:
            type (str, optional): The desired format of the returned contents. Options are 'list' or 'dict'. Defaults to 'list'.
        
        Returns:
            tuple: A tuple where the first element is a boolean indicating success or failure, and the second element contains the contents or an error message.
        """
        try:
            if not self.__input.endswith(".txt"):
                raise RuntimeError("The file is not a .txt file, please enter a valid file.")
            with open(self.__input, "r") as contents:
                if type == "list":
                    content_list = [line.strip() for line in contents]
                    return False, content_list
                elif type == "dict":
                    output_dict = {}
                    for line in contents:
                        letter, freq = line.split(",")
                        output_dict[letter.strip()] = float(freq.strip())
                    return False, output_dict
        except FileNotFoundError:
            print("The file is not found, please enter a valid file.")
        except PermissionError:
            print("This file cannot be read from, please try another file.")
        except RuntimeError:
            print("The file is not a .txt file, please enter a valid file.")
        except Exception as e:
            print(f"An unknown error occurred. Please try again later.\nDebug info: {e}")
        return True, None

    def write_contents(self, input_list):
        """
        Writes the contents of a list to the output file.
        
        Args:
            input_list (list): A list of strings to write to the output file.
        """
        with open(self.__output, "w") as output_file:
            for line in input_list:
                output_file.write(line + '\n')
