# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法1. 哈希表 存储已经走过的节点
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         already = set()
#         curr = head
#         while curr and curr.next:
#             curr = curr.next
#             if curr in already:
#                 return True        
#             else:
#                 already.add(curr)

#         return False
        
# 解法2. 快慢指针，龟兔赛跑。速度不同还出现环，必定出现重合
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        quick = head
        slow = head

        while(quick and quick.next):
            quick = quick.next.next
            slow = slow.next
            if(quick == slow):
                return True
        return False
        
