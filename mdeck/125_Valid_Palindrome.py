class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1
        s = s.lower()
        print(s)
        while left<=right:
            
            if not s[left].isalpha() and not s[left].isnumeric():
                left+=1
                continue
            if not s[right].isalpha() and not s[right].isnumeric():
                right-=1
                continue
            print(left, right, s[left], s[right])
            if s[left].isalpha() and s[right].isalpha():
                if s[left].lower() == s[right].lower():
                    left+=1
                    right-=1
                    continue
                else:
                    return False
            elif s[left].isnumeric() and s[right].isnumeric():
                if s[left] == s[right]:
                    left+=1
                    right-=1
                    continue
                else:
                    return False
            else:
                return False
        return True
                
