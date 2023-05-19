from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1:
        return list2
      if not list2:
        return list1

      res = list1

      while list2.next:
        print(list1.val, list2.val)
        if not list1:
          res.next = list2
          return res

        if list1.val >= list2.val:
          res.next = list1
          list1 = list1.next
        else:
          res.next = list2
          list1 = list1.next
          list2 = list2.next

        res = res.next

      if list1.next:
        res.next = list1

      return res


s = Solution()
