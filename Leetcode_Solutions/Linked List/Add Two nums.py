'''Add two numbers given as linked list and return as linked list'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        while l1:
            a.append(l1.val)
            l1=l1.next
        while l2:
            b.append(l2.val)
            l2=l2.next
        a.reverse()
        b.reverse()
        x=''.join(map(str,a))
        y=''.join(map(str,b))
        res = int(x)+int(y)
        res = str(res)
        
        sum = list(map(str,res))
        sum.reverse()

        head = ListNode(sum[0])
        curr = head
        for i in sum[1:]:
            newnode = ListNode(i)
            curr.next = newnode
            curr = newnode
        return head
    

#---------------------------------------------------

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            newval = v1 + v2 + carry
            carry = newval//10
            newval = newval % 10
            curr.next = ListNode(newval)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next