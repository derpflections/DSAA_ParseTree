# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

import time as time
import datetime
from application.utility import utilities
from application.HashTable import HashTable
from application.ParseInsert import ParseInserter

class HistoryHook():
    """
    A class that manages the history of a hash table, allowing logging, displaying, rolling back, and checking for redundancy.

    Attributes:
        __Hash (HashTable): The hash table whose history is being managed.
        __history (list): A list storing the history of the hash table.
        __historyTime (list): A list storing the timestamps of each history entry.
        __strRepr (list): A list storing the string representations of each history entry.
        __ignore (bool): A flag indicating whether the next operation should be ignored.
    """

    def __init__(self, hashTable):
        """
        Initializes the HistoryHook with a given hash table.
        
        Args:
            hashTable (HashTable): The initial hash table to manage.
        """
        self.__Hash = hashTable
        self.__history = []
        self.__historyTime = []
        self.__strRepr = []
        self.__ignore = False

    def logger(self, hashTable):
        """
        Logs the current state of the hash table and updates the history.
        
        Args:
            hashTable (HashTable): The current state of the hash table to log.
        """
        self.__Hash = hashTable
        loggerTable = HashTable(100)
        logger_parseInsert = ParseInserter(loggerTable)
        now = datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S")
        if self.__Hash is not None and not self.redundancyChecker() and not self.__ignore:
            for id in self.__Hash.__getkeys__():
                logger_parseInsert.checkForAlpha(self.__Hash.__getitem__(id).getExp(), id)
            self.__history.append(loggerTable)
            self.__strRepr.append(loggerTable.totext())
            self.__historyTime.append(now)
        self.__ignore = False
        loggerTable, self.__Hash = None, None

    def displayer(self):
        """
        Retrieves the history of the hash table along with the corresponding timestamps.
        
        Returns:
            tuple: A tuple containing the list of histories and the list of timestamps.
        """
        return self.__history, self.__historyTime

    def rollback(self, version):
        """
        Rolls back the hash table to a specified version.
        
        Args:
            version (int): The version number to roll back to.
            
        Returns:
            tuple: A tuple containing the rolled-back hash table and the number of versions removed.
        """
        slaveTable = HashTable(100)
        rollback_parseInsert = ParseInserter(slaveTable)
        if version <= len(self.__history):
            for id in self.__history[version].__getkeys__():
                rollback_parseInsert.checkForAlpha(self.__history[version][id].getExp(), id)
            no_of_versions = (len(self.__history) -  1) - version
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
        """
        Checks if the current version of the hash table is redundant (the same as the previous version).
        
        Returns:
            bool: True if the current version is redundant, otherwise False.
        """
        for i in range(0, len(self.__history)):
            if self.__history[i].totext() == self.__Hash.totext():
                return True
        return False
