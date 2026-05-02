# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        stack.append((root,1))
        count = 0
        while stack:
            node,lvl = stack.pop()
            if node.left:
                stack.append((node.left,lvl+1))
            if node.right:
                stack.append((node.right,lvl+1))
            count = max(count,lvl)
        return count