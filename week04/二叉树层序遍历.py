# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 层序遍历就是BFS，不过此题要求输出是二维数组
        # 所以需要每一层前先算好该层的数组的长度n，然后再进行n次循环进行append
        if not root:
            return []

        result = []
        queue = []
        queue.append(root)
        while len(queue):
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result