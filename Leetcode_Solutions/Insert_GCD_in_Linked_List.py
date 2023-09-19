'''Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one=head
        two=head.next
        while(two):
            gcd_res=gcd(one.val,two.val)
            new=ListNode(gcd_res)
            one.next=new
            new.next=two
            one=two
            two=two.next
        return head