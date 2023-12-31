class TwoSum:

    def __init__(self):
        self.count = {}

    def add(self, number: int) -> None:
        if number in self.count:
            self.count[number]+=1
        else:
            self.count[number] = 1

    def find(self, value: int) -> bool:
        for num in self.count:
            if value-num in self.count and value-num!=num:
                return True
            elif value-num in self.count and value-num==num and self.count[value-num]>1:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
