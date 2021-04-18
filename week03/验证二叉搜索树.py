# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = True
        if root.left:
            if root.left.val < root.val:
                if self.isValidBST(root.left): # 验证左子树是否是二叉搜索树
                    max_left = root.left # 取得 max_left，左子树最大值
                    while(max_left.right):
                        max_left = max_left.right
                    if max_left.val < root.val:
                        result = True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        if root.right:
            if root.val < root.right.val:
                if self.isValidBST(root.right): # 验证右子树
                    min_right = root.right # 取得 min_right，右子树最小值
                    while(min_right.left):
                        min_right = min_right.left
                    if root.val < min_right.val:
                        result = True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return result
