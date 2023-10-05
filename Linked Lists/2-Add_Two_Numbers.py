# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        op = ListNode(0)
        res = op
        c = 0 
        p1 = l1
        p2 = l2
        while p1 or p2 or c!=0:
            n1 = p1.val if p1 else 0 
            n2 = p2.val if p2 else 0 
            temp = n1+n2+c
            c = temp//10
            num = temp%10
            node = ListNode(num)
            res.next = node
            res = node
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return op.next
