# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Two Pointers
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n + m)
    # Space Complexity: O(n + m)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1
        if (list1 == None and list2 == None):
            return None
        currNodeList1 = list1
        currNodeList2 = list2
        sortedList = []
        while (currNodeList1 != None and currNodeList2 != None):
            if (currNodeList1.val <= currNodeList2.val):
                sortedList.append(currNodeList1)
                currNodeList1 = currNodeList1.next
            else:
                sortedList.append(currNodeList2)
                currNodeList2 = currNodeList2.next
        
        while (currNodeList1 != None):
            sortedList.append(currNodeList1)
            currNodeList1 = currNodeList1.next
        
        while (currNodeList2 != None):
            sortedList.append(currNodeList2)
            currNodeList2 = currNodeList2.next
        
        for i in range(len(sortedList) - 1):
            sortedList[i].next = sortedList[i + 1]
        
        return sortedList[0]