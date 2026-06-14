# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion Depth-First Search (DFS)
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       For a perfectly balanced tree, the recursion will have
    #       logn call stacks.
    #   Worst Case: O(n)
    #       For a perfectly unbalanced tree, the recursion will have
    #       n call stacks.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.diameterOfBinaryTreeHelper(root)
        return self.maxDiameter
    
    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        leftHeight = self.diameterOfBinaryTreeHelper(root.left)
        rightHeight = self.diameterOfBinaryTreeHelper(root.right)
        diameter = leftHeight + rightHeight
        if (diameter > self.maxDiameter):
            self.maxDiameter = diameter
        return 1 + max(leftHeight, rightHeight)