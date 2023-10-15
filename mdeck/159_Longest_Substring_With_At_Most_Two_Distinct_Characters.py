class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = defaultdict(int)
        maxlen = 0 
        n = len(s)
        for right in range(n):
            count[s[right]]+=1
            if len(count)<=2:
                maxlen+=1
            else:
                count[s[right-maxlen]]-=1
                if count[s[right-maxlen]]==0:
                    del count[s[right-maxlen]]
        return maxlen
