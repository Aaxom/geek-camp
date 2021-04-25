# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS和层次遍历的方法
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append(root)
        max_each_level = [root.val]

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
            if level:
                max_each_level.append(max(level))

        return max_each_level


# DFS方法
class Solution:
    import math
    def dfs(self, curNode, level, results):
        # 递归终止条件
        if len(results) == level:
            results.append(-math.inf)
        # 当层处理
        results[level] = max(results[level], curNode.val)
        # 向下递归
        if curNode.left:
            self.dfs(curNode.left, level+1, results)
        if curNode.right:
            self.dfs(curNode.right, level+1, results)

    def largestValues(self, root):
        results = []
        if not root:
            return results
        self.dfs(root, 0, results)
        return results


