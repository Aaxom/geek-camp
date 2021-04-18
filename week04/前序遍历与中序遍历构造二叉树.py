# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 终止条件
        if not preorder or not inorder:
            return
        # 当层处理
        root_val = preorder[0]
        root_node = TreeNode(val=root_val)
        root_index_inorder = inorder.index(root_val)
        
        # 向下递归
        left_node = self.buildTree(preorder[1:root_index_inorder+1], inorder[:root_index_inorder+1])
        right_node = self.buildTree(preorder[root_index_inorder+1:], inorder[root_index_inorder+1:])
        # 递归后处理
        root_node.left = left_node
        root_node.right = right_node

        return root_node
        


# 思路
# 先根据前序遍历找root，然后根据中序遍历，把整个树分为左右子树，
# 新的左半部分是左子树的中序遍历，假设有m个，右半部分是右子树的中序遍历。前序遍历从第2个开始算m个，是左子树的前序遍历，剩下的是右子树的先序遍历。下一步详情操作如下
# 在前序遍历中，接下来的第一个节点就是左子节点，然后到中序遍历中，找到这个左子节点，将树再分为两半
        


# 思路
# 先根据前序遍历找root，然后根据中序遍历，把整个树分为左右子树，
# 新的左半部分是左子树的中序遍历，假设有m个，右半部分是右子树的中序遍历。前序遍历从第2个开始算m个，是左子树的前序遍历，剩下的是右子树的先序遍历。下一步详情操作如下
# 在前序遍历中，接下来的第一个节点就是左子节点，然后到中序遍历中，找到这个左子节点，将树再分为两半


# 思路
# 先根据前序遍历找root，然后根据中序遍历，把整个树分为左右子树，
# 在前序遍历中，接下来的第一个节点就是左子节点，然后到中序遍历中，找到这个左子节点，将树再分为两半

