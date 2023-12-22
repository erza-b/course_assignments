#Task 3

#Implement in (__contains__) len (__len__) methods for HashTable

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def __getitem__(self, key):
        index = self._hash(key)
        item = self.table[index]
        if item and item[0] == key:
            return item[1]
        raise KeyError(key)

    def __contains__(self, key):
        index = self._hash(key)
        item = self.table[index]
        return item is not None and item[0] == key

    def __len__(self):
        return sum(1 for item in self.table if item is not None)


hash_table = HashTable(size=10)

hash_table['apple'] = 5
hash_table['banana'] = 8
hash_table['cherry'] = 12

print('apple' in hash_table)  
print('grape' in hash_table)  

print(len(hash_table))  
