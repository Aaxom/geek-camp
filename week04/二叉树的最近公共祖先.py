# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left

        return root



# 递归终止条件：root不存在，或者当root == p则返回p，或者当root == q则返回q
# 向下递归
# left = lowestCommonAncestor(root.left, p, q)
# right = lowestCommonAncestor(root.right, p, q)
# if not left and not right: # left和right都不存在，就是最近公共祖先不存在
# if not left: # left不存在，就是最近公共祖先在右子树里面
# if not right: # right不存在，就是最近公共祖先在左子树里面
# 通过上面的判断后，剩下的就是left和right都存在，这时候返回root即可


