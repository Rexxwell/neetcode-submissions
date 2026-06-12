# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Depth-First Search (DFS) using a Stack
    # Runtime:  28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: 
    #   Best Case: O(1)
    #   Worst Case: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return None
        stack = []
        rootTemp = root
        stack.append(root)
        while (len(stack) != 0):
            parentNode = stack.pop()
            leftNode = parentNode.left
            parentNode.left = parentNode.right
            parentNode.right = leftNode
            if (parentNode.left != None):
                stack.append(parentNode.left)
            if (parentNode.right != None):
                stack.append(parentNode.right)
        return rootTemp