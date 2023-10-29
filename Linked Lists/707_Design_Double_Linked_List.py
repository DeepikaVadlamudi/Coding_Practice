class Node:
    def __init__(self, val=0, next = None, prev= None):
        self.val = val 
        self.next = next 
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 

    def get(self, index: int) -> int:
        if index>=self.size or index<0:
            return -1
        if index+1<self.size-index:
            node = self.head
            for i in range(index+1):
                node = node.next
        else:
            node = self.tail 
            for i in range(self.size-index):
                node = node.prev
        return node.val
        

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        cur = self.head
        suc = cur.next
        cur.next = new 
        new.next = suc
        suc.prev = new
        new.prev = cur 
        self.size+=1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        suc = self.tail
        prev = self.tail.prev
        prev.next = new
        new.next = suc 
        suc.prev = new
        new.prev = prev
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index < 0:
            index = 0
        new = Node(val)
        if index<self.size-index:
            prev = self.head 
            for _ in range(index):
                prev = prev.next 
            suc = prev.next
        else:
            suc = self.tail
            for _ in range(self.size-index):
                suc = suc.prev
            prev = suc.prev
        prev.next = new
        new.next = suc
        suc.prev = new 
        new.prev = prev
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        if index<self.size-index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            suc = prev.next.next

        else:
            suc = self.tail
            for _ in range(self.size-index-1):
                suc = suc.prev
            prev = suc.prev.prev
        prev.next = suc
        suc.prev = prev
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
