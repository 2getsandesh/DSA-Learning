'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = l3 = ListNode()

        while list1 and list2:
            if list2.val > list1.val: 
                l3.next = list1
                
                list1 = list1.next

            else:
                l3.next = list2
               
                list2 = list2.next
            l3 = l3.next
        if list1: l3.next = list1
        if list2: l3.next = list2
            
            
        return dummy.next