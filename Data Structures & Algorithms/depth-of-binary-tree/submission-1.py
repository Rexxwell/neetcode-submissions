# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion DFS (Depth-First Search)
    # Runtime: 28ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       If the tree is perfectly balanced, then it would have logn
    #       levels. Thus, it would have logn recursion calls.
    #   Worst Case: O(n)
    #       If the tree is perfectly unbalanced, then it would have
    #       n levels. Thus, it would have n recursion calls.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        leftMaxDepth = 1 + self.maxDepth(root.left)
        rightMaxDepth = 1 + self.maxDepth(root.right)
        return max(leftMaxDepth, rightMaxDepth)