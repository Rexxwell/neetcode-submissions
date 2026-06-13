# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Breadth-First Search using Queue (FIFO)
    # Runtime: 37ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(1)
    #       If the tree is perfectly unbalanced, then we would append
    #       pop one node at a time.
    #   Worst Case: O(n)
    #       If the tree is perfectly balanced, then we would append and pop
    #       n/2 nodes at the last level of the tree.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        queue = deque()
        depth = 0
        queue.append(root)
        while (queue):
            depth += 1
            for i in range(len(queue)):
                parentNode = queue.popleft()
                if (parentNode.left != None):
                    queue.append(parentNode.left)
                if (parentNode.right != None):
                    queue.append(parentNode.right)
        return depth