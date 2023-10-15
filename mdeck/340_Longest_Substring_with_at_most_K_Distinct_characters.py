class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        maxlen = right = 0
        count = defaultdict(int)

        for right in range(n):
            count[s[right]]+=1
            
            if len(count)<=k:
                maxlen+=1
            else:
                count[s[right-maxlen]]-=1
                if count[s[right-maxlen]]==0:
                    del count[s[right-maxlen]]
        return maxlen
