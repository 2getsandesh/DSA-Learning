'''You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree,
 ordered from top to bottom.'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            rightside = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside: res.append(rightside.val)
        return res