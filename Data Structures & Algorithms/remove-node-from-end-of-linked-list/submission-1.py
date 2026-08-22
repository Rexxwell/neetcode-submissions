# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the length of the linked list.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list = []
        curr = head

        while curr != None:
            linked_list.append(curr)
            curr = curr.next

        if n == 1 and len(linked_list) == 1:
            head = None
        elif n == 1:
            linked_list[-(n + 1)].next = None
        elif n == len(linked_list):
            head = linked_list[-n].next
            linked_list[-n].next = None
        else:
            linked_list[-(n + 1)].next = linked_list[-n].next
            linked_list[-n].next = None
        
        return head