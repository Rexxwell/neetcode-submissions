from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Graph Theory Approach (Double BFS)
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0

        stack = []
        adjacencyList = {}
        stack.append(root)
        while (stack):
            topNode = stack.pop()
            if (topNode not in adjacencyList):
                adjacencyList[topNode] = []
            if (topNode.left != None):
                if (topNode.left not in adjacencyList):
                    adjacencyList[topNode.left] = []
                adjacencyList[topNode].append(topNode.left)
                adjacencyList[topNode.left].append(topNode)
                stack.append(topNode.left)
            if (topNode.right != None):
                if (topNode.right not in adjacencyList):
                    adjacencyList[topNode.right] = []
                adjacencyList[topNode].append(topNode.right)
                adjacencyList[topNode.right].append(topNode)
                stack.append(topNode.right)

        queue = deque()
        queue.append(root)
        visited = set()
        visited.add(root)
        farthestNode = root
        while (queue):
            currentNode = queue.popleft()
            farthestNode = currentNode
            neighbors = adjacencyList[currentNode]
            for neighbor in neighbors:
                if (neighbor not in visited):
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        queue = deque()
        queue.append((farthestNode, 0))
        visited = set()
        visited.add(farthestNode)
        maxDistance = 0
        while (queue):
            currentNode, distance = queue.popleft()
            if (distance > maxDistance):
                maxDistance = distance
            neighbors = adjacencyList[currentNode]
            for neighbor in neighbors:
                if (neighbor not in visited):
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        return maxDistance