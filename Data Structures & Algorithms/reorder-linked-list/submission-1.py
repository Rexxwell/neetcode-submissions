# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the number of nodes in the linked list.
    def reorderList(self, head: Optional[ListNode]) -> None:
        linked_list = []
        curr = head

        while curr != None:
            linked_list.append(curr)
            curr = curr.next
            
        new_linked_list = []
        low = 0
        high = len(linked_list) - 1
        mid = low + (high - low) // 2

        for i in range(mid):
            new_linked_list.append(linked_list[i])
            new_linked_list.append(linked_list[len(linked_list) - 1 - i])

        if len(linked_list) % 2 == 0:
            new_linked_list.append(linked_list[mid])
            new_linked_list.append(linked_list[mid + 1])
        else:
            new_linked_list.append(linked_list[mid])

        curr = head

        for i in range(1, len(new_linked_list)):
            curr.next = new_linked_list[i]
            curr = new_linked_list[i]
        
        new_linked_list[-1].next = None