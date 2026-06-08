# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # In-Place Reversal
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head ==  None):
            return None

        currNode = head
        prevNode = None
        nextNode = head.next
        while (currNode.next != None):
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = currNode.next
        currNode.next = prevNode
        return currNode