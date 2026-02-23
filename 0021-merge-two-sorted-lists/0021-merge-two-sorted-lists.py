# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        head = ListNode()
        l = head

        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                l.next = cur1
                cur1 = cur1.next
            else:
                l.next = cur2
                cur2 = cur2.next

            l = l.next

        while cur1:
            l.next = cur1
            cur1 = cur1.next
            l = l.next

        while cur2:
            l.next = cur2
            cur2 = cur2.next
            l = l.next

        return head.next
                

        