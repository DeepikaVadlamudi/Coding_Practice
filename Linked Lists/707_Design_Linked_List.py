class Node:
    def __init__(self, val = 0, nex = None):
        self.val = val
        self.next = nex
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        node = self.head
        if index>=self.size or index<0:
            return -1
        for i in range(index):
            node =node.next
        return node.next.val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        new = Node(val)
        new.next = node.next
        node.next = new
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
