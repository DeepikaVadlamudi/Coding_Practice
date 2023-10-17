class Solution:
    def calculate(self, s: str) -> int:
        operations = {'+','-','*','/'}
        curnum = lastnum = res = 0
        op ='+'

        for i in range(len(s)):
            if s[i].isdigit():
                curnum = curnum*10+ (ord(s[i])-ord('0'))
            if s[i] in operations or i==len(s)-1:
                if op == '+' or op == '-':
                    res+=lastnum 
                    lastnum = curnum if op=='+' else -curnum
                elif op=='*':
                    lastnum*=curnum
                elif op=='/':

                    lastnum = lastnum//curnum if lastnum>=0 else ceil(lastnum/curnum)
                curnum = 0 
                op = s[i]
        res+=lastnum
        return res
