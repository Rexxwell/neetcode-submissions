# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Breadth-First Search (BFS)
    # Runtime: 41ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity:
    #   Best Case: O(logn)
    #       In a perfectly balanced tree
    #   Worst Case: O(n)
    #       In a perfectly unbalanced tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        while (queue):
            pNode, qNode = queue.popleft()
            if (pNode == None and qNode == None):
                continue
            elif (pNode == None or qNode == None):
                return False
            elif (pNode.val != qNode.val):
                return False
            else:
                queue.append((pNode.left, qNode.left))
                queue.append((pNode.right, qNode.right))
        return True
            