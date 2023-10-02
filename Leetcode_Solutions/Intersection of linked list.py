'''Given the heads of two singly linked-lists headA and headB,
 return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        return None