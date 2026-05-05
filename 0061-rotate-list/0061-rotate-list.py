# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        l = 1
        while cur.next:
            l += 1
            cur = cur.next
        cur.next = head


        for i in range(l-k%l):
            cur = cur.next

        pos = cur.next
        cur.next = None
        return pos

        
        