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
        return self.__history, self.__historyTime
    
    def rollback(self, version):
        #this function can rollback the hashtable to any version incidated to the user
        # version is a integer corresponding to the iteration as in displayer
        if version <= len(self.__history):
            self.__Hash = self.__Hash.fromtext(self.__history[version])
            no_of_versions = (len(self.__history) - 1) - version
            for i in range(0, no_of_versions):
                self.__history.pop()
                self.__historyTime.pop()
            print(self.__Hash)
            return self.__Hash, no_of_versions
        elif version == "":
            return 
        else:
            return None, None
        