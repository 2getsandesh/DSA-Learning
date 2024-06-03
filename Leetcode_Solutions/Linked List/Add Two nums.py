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