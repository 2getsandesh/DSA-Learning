class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next

        if li == li[::-1] : return True
        else: return False