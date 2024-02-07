# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

import re

class DependencyIdentifier(): # done by Hong Yi
    """
    A class to identify dependencies between identifiers in a given hash table.

    Attributes:
        __Hash (HashTable): The hash table containing the assignments to analyze.
        __identifier (str): A regular expression pattern for matching identifiers.
        __keys (list): A list of keys from the hash table.
        __assignment_list (list): A list of expressions from the hash table.
    """

    def __init__(self, hashTable):
        """
        Initializes the DependencyIdentifier with a hash table to analyze.
        
        Args:
            hashTable (HashTable): The hash table containing the assignments.
        """
        self.__Hash = hashTable
        self.__identifier = r"[A-Za-z]+"
        self.__keys = self.__Hash.__getkeys__()
        assignment_list = [self.__Hash.__getitem__(key).getExp() for key in self.__keys]
        self.__assignment_list = assignment_list

    def parse_assignments(self):
        """
        Parses the assignments from the hash table to extract dependencies.
        
        Returns:
            dict: A dictionary mapping identifiers to lists of their dependencies.
        """
        dependencies = {}
        for assignment in self.__assignment_list:
            alpha = assignment.split('=')[0].strip()
            exp = assignment.split('=')[1].strip()
            dependencies[alpha] = re.findall(self.__identifier, exp)
        return dependencies

    def find_dependants(self):
        """
        Finds and returns dependants for each identifier in the hash table.
        
        Returns:
            dict: A dictionary mapping identifiers to lists of their dependants.
        """
        dependencies = self.parse_assignments()
        dependants = {key: [] for key in self.__keys}
        for key in self.__keys:
            for alpha in dependencies[key]:
                if alpha in self.__keys:
                    dependants[alpha].append(key)
        return dependants
