class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            if i in mapping:
                top = stack.pop() if stack else '#'
                if top != mapping[i]:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
