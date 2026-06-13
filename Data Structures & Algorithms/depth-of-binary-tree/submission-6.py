# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Depth First Search using a Stack (LIFO)
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(1)
    #       If the tree is perfectly unbalanced, then the stack will
    #       append and pop one node at a time.
    #   Worst Case: O(n)
    #       If the tree is perfectly balanced, then the stack will
    #       append and pop n/2 nodes at the last level.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        stack = []
        maxDepth = 0
        stack.append((root, 1))
        while (len(stack) != 0):
            currentNode, currentDepth = stack.pop()
            if (currentDepth > maxDepth):
                maxDepth = currentDepth
            if (currentNode.left != None):
                stack.append((currentNode.left, currentDepth + 1))
            if (currentNode.right != None):
                stack.append((currentNode.right, currentDepth + 1))
        return maxDepth
