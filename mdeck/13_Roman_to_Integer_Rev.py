class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1, 'V':5, 'X':10, 'L':50,'C': 100,'D':500, 'M': 1000}
        if len(s)<1:
            return 0
        total = mapping[s[-1]]
        n = len(s)
        for i in range(n-2,-1,-1):
            if mapping[s[i]]<mapping[s[i+1]]:
                total -= mapping[s[i]]
            else:
                total+=mapping[s[i]]
        return total
