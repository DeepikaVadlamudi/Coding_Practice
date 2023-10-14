class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mapping = {')':'('}
        stack = []
        index = set()

        for i in range(len(s)):
            if s[i].isalpha():
                continue
            elif s[i] in mapping:
                val = s[stack[-1]] if stack else '#'
                if mapping[s[i]]!=val:
                    index.add(i)
                else:
                    stack.pop()
            else:
                stack.append(i)
        for i in stack:
            index.add(i)
        
        op =''
        for i in range(len(s)):
            if i not in index:
                op+=s[i]
        return op
