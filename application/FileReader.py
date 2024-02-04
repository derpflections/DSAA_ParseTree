import os

class fileReader():
    def __init__(self, input, output):
        self.__input = input
        self.__output = output
    
    def read_contents(self, type = 'list'):
        try:
            if self.__input.endswith(".txt") == False:
                raise RuntimeError("The file is not a .txt file, please try entering a valid file!")
            with open(self.__input, "r") as contents:
                if type == "list":
                    content_list = [line for line in contents]
                    output_list = []
                    for line in content_list:
                        line = line.replace("\n", "")
                        output_list.append(line)
                    return False, output_list
                elif type == "dict":
                    output_dict = {}
                    for line in contents:
                        letter, freq = line.split(",")
                        output_dict[letter] = float(freq.strip())
                    return False, output_dict
        except FileNotFoundError:
            print("The file is not found, please try entering a valid file!")
        except PermissionError:
            print("This file cannot be read from, please try another file!")
        except RuntimeError:
            print("The file is not a .txt file, please try entering a valid file!")
        except Exception as e:
            print(f"Unknown error occurred. Please try again later.\n Debug info: {e}")
        return True, None