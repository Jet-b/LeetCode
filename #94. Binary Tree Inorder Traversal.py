# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        root = [0] + root
        tree = [None for i in range(2*len(root))]
        for i in range(1, len(tree)):
            if root[i] == "null":
                tree[2*i] = "null"
                tree[2*i + 1] = "null"