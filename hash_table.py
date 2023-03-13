class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size
        # return 1 para testar colisão

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        found = False

        for index, element in enumerate(self.table[hash_key]):
            if element[0] == key:
                self.table[hash_key][index] = (key, value)
                found = True
                break

        if not found:
            self.table[hash_key].append((key, value))

    def find(self, key):
        hash_key = self.hash_function(key)

        for element in self.table[hash_key]:
            if element[0] == key:
                return element[1]

        raise KeyError(key)

    def print(self):
        for element in self.table:
            print('line: ')
            for reg in element:
                print(reg)
