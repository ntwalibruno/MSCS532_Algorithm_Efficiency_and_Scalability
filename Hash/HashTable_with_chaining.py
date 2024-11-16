class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def InsertItem(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def DeleteItem(self, key):
        index = self.hash(key)

        for idx, k in enumerate(self.table[index]):
            if k == key:
                del self.table[index][idx]
                return True  
        return False  
        
    def Search(self, key):
        index = self.hash(key)
        for k, value in self.table[index]:
            if k == key:
                return value
            
        return None

    def display_hashtable(self):
        print(str(self.table))

if __name__ == "__main__":
    hashTable = HashTable()
    
    hashTable.InsertItem(1, "House")
    hashTable.InsertItem(2, "Apartment")
    hashTable.InsertItem(2, "Condo")
    hashTable.InsertItem("Room", 5)

    value = hashTable.Search("Room")
    print("Search for key 'Room':",value)

    hashTable.DeleteItem("Room")

    hashTable.display_hashtable()