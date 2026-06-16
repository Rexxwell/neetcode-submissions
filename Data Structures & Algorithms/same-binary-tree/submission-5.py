# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Depth-First Search (DFS)
    # Runtime: 43ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       If the tree is perfectly balanced, then there will be
    #       logn call stacks.
    #   Worst Case: O(n)
    #       If the tree is perfectly unbalanced and the last node
    #       has the value mismatch, then there will be n call stacks
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q == None):
            return True
        if (p == None or q == None):
            return False
        if (p.val != q.val):
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return (left and right)