# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Breadth-First Search (BFS) using Queue
    # Runtime: 29ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(1)
    #       When the tree is a perfectly unbalanced tree,
    #       it appends and pops one node at the time,
    #       which makes the space complexity O(1).
    #   Worst Case: O(n)
    #       When the tree is perfectly balanced,
    #       in the last level of the tree, it contains n/2 nodes
    #       so the queue will append and pop n/2 nodes, which makes it
    #       O(n/2) time
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return None
        queue = deque()
        rootTemp = root
        queue.append(root)
        while (queue):
            parentNode = queue.pop()
            leftNode = parentNode.left
            parentNode.left = parentNode.right
            parentNode.right = leftNode
            if (parentNode.left != None):
                queue.append(parentNode.left)
            if (parentNode.right != None):
                queue.append(parentNode.right)
        return rootTemp