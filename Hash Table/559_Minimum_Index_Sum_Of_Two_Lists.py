class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {}
        for i in range(len(list1)):
            mapping[list1[i]] = i 
            
        minsum = 100000000
        res = []
        
        for i in range(len(list2)):
            cur_sum = 0
            if list2[i] in mapping:
                cur_sum = mapping[list2[i]] + i   
                if cur_sum<minsum:
                    res.clear()
                    res.append(list2[i])
                    minsum = cur_sum
                elif cur_sum == minsum:
                    res.append(list2[i])
        return res
