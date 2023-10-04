# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow= fast = dummy
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                break
        if slow == None or fast == None or fast.next ==None:
            return None
        slow = dummy
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
        
