class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_st = {}
        mapping_ts = {}

        for c1, c2 in zip(s,t):
            
            if c1 not in mapping_st and c2 not in mapping_ts:
                mapping_st[c1] = c2
                mapping_ts[c2] = c1
            elif mapping_st.get(c1)!=c2 or mapping_ts.get(c2)!=c1:
                return False
        
        return True
