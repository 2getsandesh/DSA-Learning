'''You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = new = ListNode()
        while head:
            currsum = 0
            while head.val != 0:
                currsum += head.val
                head = head.next
            if currsum!=0: 
                new.next = ListNode(currsum)
                new = new.next
            head = head.next
        return dummy.next
    

#------------------------------------------------------------#

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currsum=0
        dummy = new = ListNode()
        while head:
            if head.val != 0:
                currsum += head.val
            else:
                if currsum != 0: 
                    new.next = ListNode(currsum)
                    new  = new.next
                currsum = 0
            head = head.next
        return dummy.next