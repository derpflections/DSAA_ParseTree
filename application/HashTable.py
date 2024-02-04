class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size

    # get the hash value of the alphabet
    def hashFunction(self, key):
        key = key.lower()
        return ord(key) - ord('a')

    # Deal with collision resolution by means of
    # linear probing with a 'plus 1' rehash
    def rehashFunction(self, oldHash):
        return (oldHash + 1) % self.size

    def __setitem__(self, key, value):
        index = self.hashFunction(key)
        startIndex = index
        while True:
            # If bucket is empty then just use it
            if self.buckets[index] == None:
                self.buckets[index] = value
                self.keys[index] = key
                break
            else:  # If not empty and the same key then just overwrite
                if self.keys[index] == key:
                    self.buckets[index] = value
                    break
                else:  # Look for another available bucket
                    index = self.rehashFunction(index)
                    # We must stop if no more buckets
                    if index == startIndex:
                        break

    def __getitem__(self, key):
        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys[index] == key:
                return self.buckets[index]
            elif self.keys[index] is None:
                return None  # Key not found, return None
            else:
                index = self.rehashFunction(index)
                if index == startIndex:
                    return None 
                
    def __getkeys__(self):
        return [key for key in self.keys if key is not None]