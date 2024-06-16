'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            lis = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    lis.append(node.val) 
                    q.append(node.left)
                    q.append(node.right)
            if lis: res.append(lis)
        return res