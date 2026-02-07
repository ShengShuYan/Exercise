# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        num1 = 0
        while current:
            num1 *= 10
            num1 += current.val
            current = current.next
        num2 = 0
        current = l2
        while current:
            num2 *= 10
            num2 += current.val
            current = current.next
        L = [int(x) for x in str(num1 + num2)]
        head = ListNode(L[0])
        current = head
        for i in L[1:]:
            current.next = ListNode(i)
            current = current.next
        return head



        