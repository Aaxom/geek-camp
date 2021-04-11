# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 常规迭代解法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 or l2:

            if l1 and l2:
                if l1.val >= l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
            elif l1 and not l2:
                curr.next = l1
                l1 = l1.next
            elif l2 and not l1:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        return head.next

# 递归解法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
          return l2
        if not l2:
          return l1

        if l1.val < l2.val:
          l1.next = self.mergeTwoLists(l1.next, l2)
          return l1
        else:
          l2.next = self.mergeTwoLists(l1, l2.next)
          return l2