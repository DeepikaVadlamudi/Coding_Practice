# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p1 = list1
        p2 = list2
        prev = dummy
        while p1 and p2:
            if p1.val<p2.val:
                prev.next = p1
                p1 = p1.next 
            else:
                prev.next = p2
                p2 = p2.next 
            prev = prev.next 
        prev.next = p1 if p1 else p2
        return dummy.next
                
        
