class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        stack = []
        for curday, curtemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<curtemp:
                prevday =stack.pop()
                output[prevday] = curday-prevday
            stack.append(curday)
        return output
