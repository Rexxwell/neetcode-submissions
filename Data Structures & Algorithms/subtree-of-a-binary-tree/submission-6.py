# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Tree Serialization + Substring Search (KMP Algorithm)
    # Runtime: 27ms
    # Memory: 8.2 MB
    # Time Complexity: O(n + m)
    # Space Complexity: O(n + m) 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootTree = self.isSubtreeHelper(root)
        subRootTree = self.isSubtreeHelper(subRoot)
        return subRootTree in rootTree
        
    def isSubtreeHelper(self, node: Optional[TreeNode]) -> str:
        if (node == None):
            return "#"
        return f"^{node.val}" + self.isSubtreeHelper(node.left) + self.isSubtreeHelper(node.right)