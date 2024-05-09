class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):           # Creates index based on key's hash value
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)         # Calculates the index where the key will go

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
            return self.table[index].append((key, value))

    def lookup(self, key):
        index = self._hash(key)         # Calculates the index where the key will go
        if self.table[index] is not None:           # Checks if the index is populated
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
            return None

    def remove(self, key):          # Checks if the given index is empty and if not deletes it.
        index = self._hash(key)         # Calculates the index where the key will go
        if self.table[index] is not None:           # Checks if the index is populated
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return
