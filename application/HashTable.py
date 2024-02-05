# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

"""
HashTable.py
"""

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.keys = [None] * self.size
#         self.buckets = [None] * self.size

#     # get the hash value of the alphabet
#     def hashFunction(self, key):
#         key = key.lower()
#         return ord(key) - ord('a')

#     # Deal with collision resolution by means of
#     # linear probing with a 'plus 1' rehash
#     def rehashFunction(self, oldHash):
#         return (oldHash + 1) % self.size

#     def __setitem__(self, key, value):
#         index = self.hashFunction(key)
#         startIndex = index
#         while True:
#             # If bucket is empty then just use it
#             if self.buckets[index] == None:
#                 self.buckets[index] = value
#                 self.keys[index] = key
#                 break
#             else:  # If not empty and the same key then just overwrite
#                 if self.keys[index] == key:
#                     self.buckets[index] = value
#                     break
#                 else:  # Look for another available bucket
#                     index = self.rehashFunction(index)
#                     # We must stop if no more buckets
#                     if index == startIndex:
#                         break

#     def __getitem__(self, key):
#         index = self.hashFunction(key)
#         startIndex = index
#         while True:
#             if self.keys[index] == key:
#                 return self.buckets[index]
#             elif self.keys[index] is None:
#                 return None  # Key not found, return None
#             else:
#                 index = self.rehashFunction(index)
#                 if index == startIndex:
#                     return None

#     def __getkeys__(self):
#         return [key for key in self.keys if key is not None]


class HashTable:
    def __init__(self, initial_size=10, load_factor=0.75):
        self.size = initial_size
        self.load_factor = load_factor
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.num_items = 0

    def hashFunction(self, key):
        key_int = sum(ord(char) for char in key)
        return key_int % self.size

    def rehashFunction(self, oldHash):
        return (oldHash + 1) % self.size

    def resize(self, new_size):
        old_keys = self.keys
        old_buckets = self.buckets
        self.size = new_size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.num_items = 0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.__setitem__(old_keys[i], old_buckets[i])

    def __setitem__(self, key, value):
        if self.num_items >= self.size * self.load_factor:
            # Resize the hashtable
            self.resize(self.size * 2)

        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.buckets[index] is None:
                self.buckets[index] = value
                self.keys[index] = key
                self.num_items += 1
                break
            elif self.keys[index] == key:
                self.buckets[index] = value
                break
            else:
                index = self.rehashFunction(index)
                if index == startIndex:
                    # No available space, resize and try again
                    self.resize(self.size * 2)
                    index = self.hashFunction(key)
                    startIndex = index

    def __getitem__(self, key):
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
        return sorted([key for key in self.keys if key is not None])

    def __str__(self):
        output_str = ""
        sorted_keys = self.__getkeys__()

        for key in sorted_keys:
            value = self.__getitem__(key)
            output_str += f"{value}\n"

        return output_str
