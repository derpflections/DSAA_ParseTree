import time as time
import datetime
from application.utility import utilities
from application.HashTable import HashTable

class HistoryHook():
    def __init__(self, hashTable):
        self.__Hash = hashTable
        self.__history = []
        self.__historyTime = []
    
    def logger(self):
        now = datetime.datetime.now()
        now = now.strftime("%d %B %Y, %H:%M:%S")        
        if self.__Hash != None and self.__Hash.totext() not in self.__history:
            self.__history.append(self.__Hash.totext())
            self.__historyTime.append(now)


    def displayer(self):
        utilities.cls() 
        print("Assignment History:")
        for i in range(len(self.__history)):
            if i == len(self.__history) - 1:
                print(f"Time: {self.__historyTime[i]}, iteration {i} (latest)")
            else:
                print(f"Time: {self.__historyTime[i]}, iteration {i}")
            print(self.__history[i])
            print("\n")
    
    def rollback(self, version):
        #this function can rollback the hashtable to any version incidated to the user
        # version is a integer corresponding to the iteration as in displayer
        if version <= len(self.__history):
            self.__Hash = self.__Hash.fromtext(self.__history[version])
            print(f"Rollback to version {version} successful.")
            no_of_versions = (len(self.__history) - 1) - version
            print(f"Number of versions rolled back: {no_of_versions}")
            return self.__Hash
        elif version == "":
            return 
        else:
            print("Invalid version number, returning to main menu...")

    def debugger(self):
        print(self.__history)
        print(self.__historyTime)