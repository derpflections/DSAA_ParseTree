import re

class DependencyIdentifier():
    def __init__(self, hashTable):
        self.__Hash = hashTable
        self.__identifier = r"[A-Za-z]+"
        self.__keys = self.__Hash.__getkeys__()
        assignment_list = []
        for key in self.__keys:
            assignment_list.append(self.__Hash.__getitem__(key).getExp())
        self.__assignment_list = assignment_list

    def parse_assignments(self):
        dependencies = {}
        for assignment in self.__assignment_list:
            alpha = assignment.split('=')[0].strip()
            exp = assignment.split('=')[1].strip()
            dependencies[alpha] = re.findall(self.__identifier, exp)
        return dependencies