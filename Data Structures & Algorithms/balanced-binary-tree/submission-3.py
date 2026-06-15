# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Recursive Depth-First Search (DFS)
    # Runtime: 33ms
    # Memory: 8.2 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       If the tree is perfectly balanced, then there will logn call
    #       stacks.
    #   Worst Case: O(n)
    #       If the tree is perfectly unbalanced, then there will be
    #       n call stacks.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isHeightBalanced, height = self.isBalancedHelper(root)
        return isHeightBalanced

    def isBalancedHelper(self, root: Optional[TreeNode]) -> tuple(bool, int):
        if root == None:
            return (True, 0)
        leftIsHeightBalanced, leftHeight = self.isBalancedHelper(root.left)
        rightIsHeightBalanced, rightHeight = self.isBalancedHelper(root.right)
        currentHeight = 1 + max(leftHeight, rightHeight)
        if not leftIsHeightBalanced:
            return (False, currentHeight)
        if not rightIsHeightBalanced:
            return (False, currentHeight)
        elif abs(leftHeight - rightHeight) > 1:
            return (False, currentHeight)
        else:
            return (True, currentHeight)
