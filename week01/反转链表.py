# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 解法一：迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prevNode = None
        currNode = head
        while(currNode):
            nextNode = currNode.next # 临时存储curr的下一个节点
            currNode.next = prevNode # a(prev) <= b(curr) -> c (next)
            prevNode = currNode # a <= b(prev, curr) -> c (next)
            currNode = nextNode # a <= b(prev) -> c (curr, next)

        return prevNode

# 解法二：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # 递归调用，拿到head.next后续链表反转后的头结点
        prevNode = self.reverseList(head.next) # 此时，a(head) => b <- c <- d <- e(prev)
        head.next.next = head # 让head的下一个节点，指向自己，此时，a(head) <= b <- c <- d <- e
        head.next = None

        return prevNode



# 1. 标记 pre, curr, back
# curr.next = pre
# 
# pre = curr
# curr = back
# back = back.next