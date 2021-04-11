# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 哈希
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        already = set()

        curr = head
        while(curr and curr.next):
            if curr in already:
                return curr
            else:
                already.add(curr)
                curr = curr.next

        return None


# 快慢指针法
# 看图：https://assets.leetcode-cn.com/solution-static/142/142_fig1.png
# 设链表head距离入环点是a，入环点距离相遇点的距离是b，相遇点再顺时针再次到入环点是c
# 则根据两个指针相遇，且fast走过的路是slow的刚好2倍
# 有：fast走过的路程 = a+n(b+c) = 2*slow走过的路程 = 2(a+b)
# <=> a+n(b+c)+b = 2*(a+b)
# <=> a = n(b+c)-b = nb+nc-b = c+ (nb+nc-b) -c = c + (n-1)(b+c)
# 所以head到入环点的距离，就是slow在相遇点，按照1倍的速度走，到下次相遇时，走过的距离。

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next # fast先开2倍速
            slow = slow.next

            if fast == slow:
              # 存在环，现在找入环点
              fast = head
              while fast != slow:
                fast = fast.next # fast变成一倍速
                slow = slow.next
              return fast

        return None