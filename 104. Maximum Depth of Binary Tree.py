# depth first search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root == None:
            return 0
        
        # recursively find the depth of the left and right nodes
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # return 1 + the longest depth
        return 1 + max(left, right)
        