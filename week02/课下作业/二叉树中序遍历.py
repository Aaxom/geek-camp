# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return []
        else:
            self.recursive(result, root)
        return result

    
    def recursive(self, result, root):
        if root.left:
            # 左孩子递归
            self.recursive(result, root.left)
        # 根节点
        result.append(root.val)
        if root.right:
            # 右边孩子递归
            self.recursive(result, root.right)



