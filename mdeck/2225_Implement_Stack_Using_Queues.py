class MyStack:

    def __init__(self):
       self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty() :
            return self.queue.pop()
        else:
            raise IndexError("Stack is empty")

    def top(self) -> int:
        if not self.empty() :
            return self.queue[-1]
        else:
            raise IndexError("Stack is empty")


    def empty(self) -> bool:
        return len(self.queue)==0
 
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
