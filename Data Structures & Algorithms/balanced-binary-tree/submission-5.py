# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Depth-First Search (DFS)
    # Runtime: 39ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Memory Complexity: O(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
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
                stack.pop()
                leftHeight = heights[topNode.left]
                rightHeight = heights[topNode.right]
                differenceHeight = abs(leftHeight - rightHeight)
                currentHeight = 1 + max(leftHeight, rightHeight)
                if (differenceHeight > 1):
                    return False
                heights[topNode] = currentHeight

        return True