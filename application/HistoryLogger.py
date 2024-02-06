import time as time
import datetime
from application.utility import utilities
from application.HashTable import HashTable
from application.ParseInsert import ParseInserter

class HistoryHook():
    def __init__(self, hashTable):
        self.__Hash = hashTable
        self.__history = []
        self.__historyTime = []
        self.__strRepr = []
        self.__ignore = False
    
    def logger(self, hashTable):
        self.__Hash = hashTable
        loggerTable = HashTable(100)
        logger_parseInsert = ParseInserter(loggerTable)
        now = datetime.datetime.now()
        now = now.strftime("%d %B %Y, %H:%M:%S")
        if self.__Hash != None and self.redundancyChecker() == False and self.__ignore == False:
            for id in self.__Hash.__getkeys__():
                logger_parseInsert.checkForAlpha(self.__Hash.__getitem__(id).getExp(), id)
            self.__history.append(loggerTable)
            self.__strRepr.append(loggerTable.totext())
            self.__historyTime.append(now)
        self.__ignore = False
        loggerTable, self.__Hash = None, None


    def displayer(self):
        return self.__history, self.__historyTime
    
    def rollback(self, version):
        slaveTable = HashTable(100)
        rollback_parseInsert = ParseInserter(slaveTable)
        #this function can rollback the hashtable to any version incidated to the user
        # version is a integer corresponding to the iteration as in displayer
        if version <= len(self.__history):
            for id in self.__history[version].__getkeys__():
                rollback_parseInsert.checkForAlpha(self.__history[version][id].getExp(), id)
            no_of_versions = (len(self.__history) - 1) - version
            for i in range(0, no_of_versions):
                self.__history.pop()
                self.__historyTime.pop()
                self.__strRepr.pop()
            self.__ignore = True
            return slaveTable, no_of_versions
        elif version == "":
            return 
        else:
            return None, None
    

    def redundancyChecker(self):
        #this function checks for redundant versions of the hashtable
        #if the current version is the same as the previous version, it will not be added to the history
        for i in range(0, len(self.__history)):
            if self.__history[i].totext() == self.__Hash.totext():
                return True
        return False