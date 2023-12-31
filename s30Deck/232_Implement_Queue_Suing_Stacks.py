class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if not self.empty():
            return self.stack1.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self) -> int:
        if not self.empty():
            return self.stack1[-1]
        else:
            raise IndexError("Stack is empty")

    def empty(self) -> bool:
        return len(self.stack1)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
