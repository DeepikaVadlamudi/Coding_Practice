class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.hashset = [Bucket() for _ in range(self.keyRange)]
    
    def hashk(self, key:int):
        return key%self.keyRange

    def add(self, key: int) -> None:
        bucket = self.hashk(key)
        self.hashset[bucket].insert(key)

    def remove(self, key: int) -> None:
        bucket = self.hashk(key)
        self.hashset[bucket].delete(key)

    def contains(self, key: int) -> bool:
        bucket = self.hashk(key)
        return self.hashset[bucket].exists(key)

class Node:
    def __init__(self, val, nex=None):
        self.val = val 
        self.next = nex
        
class Bucket:
    def __init__(self):
        self.node = Node(0)
    
    def insert(self, key):
        if not self.exists(key):
            new = Node(key)
            new.next = self.node.next 
            self.node.next = new
    
    def delete(self, key):
        if self.exists(key):
            prev=self.node
            cur = self.node.next 
            while cur:
                if cur.val == key:
                    prev.next = cur.next
                    return 
                prev = cur
                cur = cur.next 
    
    def exists(self, key):
        cur = self.node.next
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
