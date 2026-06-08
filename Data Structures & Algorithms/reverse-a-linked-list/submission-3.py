# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 28 ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None

        linkedList = []
        currNode = head
        while (currNode != None):
            linkedList.append(currNode)
            currNode = currNode.next

        for i in range(len(linkedList) - 2, -1, -1):
            currNode = linkedList[i]
            currNode.next.next = currNode

        linkedList[0].next = None          
        return linkedList[len(linkedList) - 1]