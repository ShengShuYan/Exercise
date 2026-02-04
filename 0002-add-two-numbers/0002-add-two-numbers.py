# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode(0)
        cur = r
        p = 0
        while l1 or l2 or p:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            t = l1v + l2v + p
            cur.next = ListNode(t % 10)
            cur = cur.next
            p = t // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return r.next

        
        