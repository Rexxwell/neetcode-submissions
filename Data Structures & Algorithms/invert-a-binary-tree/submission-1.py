# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion
    # Runtime: 38ms
    # Memory: 8.2 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       If the tree is perfectly balanced,
    #       then the tree would have logn levels.
    #       Which means logn recursion calls.
    #   Worst Case: O(n)
    #       If the tree is perfectly unbalanced,
    #       then the tree would have O(n) levels.
    #       Which means n recursion calls.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        rightTemp = root.right
        root.right = root.left
        root.left = rightTemp
        return root
