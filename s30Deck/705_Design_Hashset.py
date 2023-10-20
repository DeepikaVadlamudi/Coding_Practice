class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.hashset = [Bucket() for _ in range(self.size)]
    
    def hashk(self,key):
        return key%self.size

    def add(self, key: int) -> None:
        index = self.hashk(key)
        self.hashset[index].insert(key)

    def remove(self, key: int) -> None:
        index = self.hashk(key)
        self.hashset[index].delete(key)

    def contains(self, key: int) -> bool:
        index = self.hashk(key)
        return self.hashset[index].exists(key)

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

    def delete(self,key):
        if self.exists(key):
            prev = self.node
            cur = self.node.next
            while cur:
                if cur.val == key:
                    prev.next = cur.next 
                    return
                prev = cur 
                cur = cur.next

    def exists(self,key):
        node = self.node.next
        while node:
            if node.val==key:
                return True
            node = node.next
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
