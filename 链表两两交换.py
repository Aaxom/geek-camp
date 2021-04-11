# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 解法一，递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        virtHead = ListNode()
        virtHead.next = head
        self.recursive(virtHead)
        return virtHead.next
    
    def recursive(self, root):
        if(root.next and root.next.next):
            a = root.next
            b = a.next

            root.next = b
            a.next = b.next
            b.next = a

            self.recursive(a)

# 解法二，迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        while (curr.next and curr.next.next):
            a = curr.next
            b = a.next

            curr.next = b
            a.next = b.next
            b.next = a

            curr = a
        return dummyHead.next
        
        


# 递归法
# 1. 添加虚拟头结点virtHead，令virtHead.next = head
# 2. 调用递归 recursive(virtHead.next)

# recursive(root) {
#     if(root.next and root.next.next):
#         a = root.next
#         b = a.next

#         root.next = b
#         a.next = b.next
#         b.next = a

#         recursive(a)
