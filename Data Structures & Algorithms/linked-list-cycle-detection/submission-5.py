# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Visited List (Hash Set)
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        currNode = head
        while (currNode != None):
            if (currNode in visited):
                return True
            else:
                visited.add(currNode)
            currNode = currNode.next
        return False
