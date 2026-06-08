# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # In-Place Reversal (Optimized)
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prevNode = None
        while (currNode != None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode