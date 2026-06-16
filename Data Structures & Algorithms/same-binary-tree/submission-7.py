# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Depth-First Search (DFS)
    # Runtime: 29ms
    # Memory: 8.0 MB
    # Time Complexity: O(n + m)
    # Space Complexity:
    #   Best Case: O(logn)
    #       In a perfectly balanced tree
    #   Worst Case: O(n)
    #       In a perfectly unbalanced tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = []
        pStack.append(p)
        qStack = []
        qStack.append(q)
        while (pStack or qStack):
            pTopNode = pStack.pop()
            qTopNode = qStack.pop()
            if (pTopNode == None and qTopNode == None):
                continue
            elif (pTopNode == None or qTopNode == None):
                return False
            elif (pTopNode.val != qTopNode.val):
                return False
            else:
                pStack.append(pTopNode.right)
                pStack.append(pTopNode.left)
                qStack.append(qTopNode.right)
                qStack.append(qTopNode.left)
        return True