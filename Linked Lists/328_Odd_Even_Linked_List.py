# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddH = head
        evenH = head.next
        even = evenH
        while even and even.next:
            oddH.next = even.next 
            oddH = oddH.next 
            even.next = oddH.next
            even = even.next
        oddH.next = evenH
        return head
