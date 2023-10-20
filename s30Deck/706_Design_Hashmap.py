class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.hashmap = [Bucket() for _ in range(self.size)]
    
    def hashk(self, key):
        return key%self.size

    def put(self, key: int, value: int) -> None:
        index = self.hashk(key)
        self.hashmap[index].insert(key, value)

    def get(self, key: int) -> int:
        index = self.hashk(key)
        return self.hashmap[index].getv(key)


    def remove(self, key: int) -> None:
        index = self.hashk(key)
        return self.hashmap[index].delete(key)

class Bucket:
    def __init__(self):
        self.bucket = []

    def insert(self, key, val):
        found = False
        for i,kv in enumerate(self.bucket):
            if kv[0]== key:
                self.bucket[i]=(key,val)
                found = True
        if not found:
            self.bucket.append((key,val))
    
    def getv(self, key):
        for k,v in self.bucket:
            if k==key:
                return v
        return -1
    
    def delete(self, key):
        for i,kv in enumerate(self.bucket):
            if kv[0]==key:
                del self.bucket[i]
                return 
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
