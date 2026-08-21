# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Slow and fast pointers
    # Runtime: 32ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next != None: 
            slow = head
            fast = head.next

            # Get the midpoint of the linked list using the slow and
            # fast pointer.
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            
            second_half = slow.next
            slow.next = None
            prev = None
            curr = second_half

            # Reverse the second half.
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Merge the two halves, head and prev.
            first_half = head
            second_half = prev
            while first_half != None and second_half != None:
                first_half_temp = first_half.next
                first_half.next = second_half
                second_half_temp = second_half.next
                second_half.next = first_half_temp
                first_half = first_half_temp
                second_half = second_half_temp