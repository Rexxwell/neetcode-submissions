# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Dummy Node
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, None)
        newTail = newHead
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                newTail.next = list1
                list1 = list1.next
            else:
                newTail.next = list2
                list2 = list2.next
            newTail = newTail.next
        
        if (list1 != None):
            newTail.next = list1
        elif (list2 != None):
            newTail.next = list2

        return newHead.next