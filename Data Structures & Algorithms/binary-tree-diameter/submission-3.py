# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Depth-First Search (DFS) using Stack
    # Runtime: 30ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       If the tree is perfectly balanced, then the stack will
    #       contain logn nodes inside before it starts popping them out.
    #   Worst Case: O(n)
    #       If the tree is perfectly unbalanced, then the stack
    #       will contain n nodes inside before it starts popping them
    #       out.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        maxDiameter = 0
        stack = []
        stack.append(root)
        heights = {None: 0}
        while (stack):
            topNode = stack[-1]
            if (topNode.left not in heights):
                stack.append(topNode.left)
            elif (topNode.right not in heights):
                stack.append(topNode.right)
            else:
                node = stack.pop()
                leftHeight = heights[node.left]
                rightHeight = heights[node.right]
                diameter = leftHeight + rightHeight
                if (diameter > maxDiameter):
                    maxDiameter = diameter
                heights[node] = 1 + max(leftHeight, rightHeight)
        return maxDiameter