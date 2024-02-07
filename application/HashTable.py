# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

from application.Variable import Variable

class HashTable:
    """
    A hash table implementation with dynamic resizing.

    Attributes:
        size (int): The initial size of the hash table.
        load_factor (float): The load factor at which the hash table should be resized.
        keys (list): A list of keys stored in the hash table.
        buckets (list): A list of values associated with the keys.
        num_items (int): The number of items currently stored in the hash table.
    """

    def __init__(self, initial_size=10, load_factor=0.75):
        """
        Initialize a new hash table with the given size and load factor.

        Args:
            initial_size (int, optional): The initial size of the hash table. Defaults to  10.
            load_factor (float, optional): The load factor at which the hash table should be resized. Defaults to  0.75.
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.num_items =  0

    def hashFunction(self, key):
        """
        Compute the hash of the given key.

        Args:
            key (str): The key to hash.

        Returns:
            int: The computed hash.
        """
        key_int = sum(ord(char) for char in key)
        return key_int % self.size

    def rehashFunction(self, oldHash):
        """
        Recompute the hash of the given old hash.

        Args:
            oldHash (int): The old hash to rehash.

        Returns:
            int: The recomputed hash.
        """
        return (oldHash +  1) % self.size

    def resize(self, new_size):
        """
        Resize the hash table to the given size.

        Args:
            new_size (int): The new size for the hash table.
        """
        old_keys = self.keys
        old_buckets = self.buckets
        self.size = new_size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.num_items =  0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.__setitem__(old_keys[i], old_buckets[i])

    def __setitem__(self, key, value):
        """
        Set the value for the given key in the hash table.

        Args:
            key (str): The key for which to set the value.
            value (any): The value to set for the given key.
        """
        if self.num_items >= self.size * self.load_factor:
            # Resize the hashtable
            self.resize(self.size *  2)

        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.buckets[index] is None:
                self.buckets[index] = value
                self.keys[index] = key
                self.num_items +=  1
                break
            elif self.keys[index] == key:
                self.buckets[index] = value
                break
            else:
                index = self.rehashFunction(index)
                if index == startIndex:
                    # No available space, resize and try again
                    self.resize(self.size *  2)
                    index = self.hashFunction(key)
                    startIndex = index

    def __getitem__(self, key):
        """
        Get the value for the given key from the hash table.

        Args:
            key (str): The key for which to retrieve the value.

        Returns:
            any: The value associated with the given key, or None if the key is not found.
        """
        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys[index] == key:
                return self.buckets[index]
            elif self.keys[index] is None:
                return None
            else:
                index = self.rehashFunction(index)
                if index == startIndex:
                    return None

    def __getkeys__(self):
        """
        Retrieve a sorted list of keys in the hash table.

        Returns:
            list: A sorted list of keys.
        """
        return sorted([key for key in self.keys if key is not None])

    def __str__(self):
        """
        Return a string representation of the hash table.

        Returns:
            str: A string representation of the hash table.
        """
        output_str = ""
        sorted_keys = self.__getkeys__()

        for key in sorted_keys:
            value = self.__getitem__(key)
            output_str += f"{value}\n"
        return output_str

    def totext(self):
        """
        Convert the hash table to a textual representation.

        Returns:
            str: A textual representation of the hash table.
        """
        output_str = ""
        sorted_keys = self.__getkeys__()

        for key in sorted_keys:
            value = self.__getitem__(key)
            output_str += f"{value}\n"

        return output_str

    def fromtext(self, text):
        """
        Create a new hash table from a textual representation.

        Args:
            text (str): The textual representation of the hash table.

        Returns:
            HashTable: A new hash table constructed from the text.
        """
        newHash = HashTable()
        text = text.split('\n')
        for line in text:
            if line != "":
                newHash.__setitem__(line.split('=')[0], Variable(line.split('=')[0], line))
        return newHash
