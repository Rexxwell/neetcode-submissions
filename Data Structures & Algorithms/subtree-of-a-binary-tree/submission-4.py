# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    # Recursive Depth-First Search (DFS)
    # Runtime: 32ms
    # Memory: 8.2 MB
    # Time Complexity: O(nm) 
    # Space Complexity:
    #   Best Case: O(logn + logm)
    #       If the tree is perfectly balanced, then there will be
    #       logn call stacks.
    #   Worst Case: O(n + m)
    #       If the tree is perfectly unbalanced, then there will be
    #       n call stacks.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (subRoot == None):
            return True
        elif (root == None and subRoot != None):
            return False
        elif (root.val == subRoot.val):
            if (self.isSubtreeHelper(root, subRoot)):
                return True     
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None and subRoot == None):
            return True
        elif ((root == None or subRoot == None)
            or (root.val != subRoot.val)):
            return False
        return self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)