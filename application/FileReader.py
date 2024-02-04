import os

class fileReader():
    def __init__(input, output):
        self.__input = input
        self.__output = output
    
    def read_contents(self, type = 'list'):
        try:
            with open(self.__input, "r") as contents:
                if type == "list":
                    output_list = [line for line in contents]
                    return output_list
                elif type == "dict":
                    output_dict = {}
                    for line in contents:
                        letter, freq = line.split(",")
                        output_dict[letter] = float(freq.strip())
                    return output_dict
        except FileNotFoundError:
            print("The file is not found, please try entering a valid file!")
        except PermissionError:
            print("This file cannot be read from, please try another file!")
        except Exception as e:
            print(f"Unknown error occurred. Please try again later.\n Debug info: {e}")
        return None