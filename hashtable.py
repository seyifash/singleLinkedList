class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
            
        if not found:
            self.arr[h].append((key, val))
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                
hash = HashTable()
print(hash.get_hash("march 6"))
print(hash.get_hash("march 17"))
hash["march 9"] = 130
hash["march 6"] = 78
hash["march 25"] = 250
hash["march 4"] = 15
hash["march 17"] = 15
hash["march 9"] = 200
print(hash["march 9"])
del hash["march 9"]
print(hash.arr)



