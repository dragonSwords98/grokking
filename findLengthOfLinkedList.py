# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findLengthOfLinkedList(self, head: Optional[ListNode], length = 0) -> int:
        if not head.next:
            return 1
        return length + self.findLengthOfLinkedList(head.next)


    def generateListNode(self, length) -> ListNode:
        next = ListNode(-1)
        head = next
        for a in range(length):
            a = ListNode(val=a, next=next)
            next = a
            print(a.val)
        return head

s = Solution()
n = s.generateListNode(10)
print(s.findLengthOfLinkedList(n))