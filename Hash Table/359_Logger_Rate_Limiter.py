class Logger:

    def __init__(self):
        self.table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.table:
            if timestamp >= self.table[message]+10:
                self.table[message] = timestamp 
                return True 
            else:
                return False 
        else:
            self.table[message] = timestamp 
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
