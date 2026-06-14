# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Approach without a shared state
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       When the tree is perfectly balanced, there will be logn
    #       call stacks.
    #   Worst Case: O(n)
    #       When the tree is perfectly unbalanced, there will be n
    #       call stacks.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height, maxDiameter = self.diameterOfBinaryTreeHelper(root)
        return maxDiameter
        
    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if (root == None):
            return (0, 0)
        leftHeight, leftMaxDiameter = self.diameterOfBinaryTreeHelper(root.left)
        rightHeight, rightMaxDiameter = self.diameterOfBinaryTreeHelper(root.right)
        currentDiameter = leftHeight + rightHeight
        currentHeight = 1 + max(leftHeight, rightHeight)
        return (currentHeight, max(leftMaxDiameter, rightMaxDiameter, currentDiameter))