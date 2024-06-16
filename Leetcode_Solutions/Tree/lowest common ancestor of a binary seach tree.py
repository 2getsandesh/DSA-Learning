'''LCA for Binary SEARCH Tree'''
# Note: This is different from LCA for Binary Tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def dfs(node):
            if not node: return
            lca[0] = node
            if node is p or node is q: return 
            elif p.val < node.val and q.val < node.val: dfs(node.left)
            elif p.val > node.val and q.val > node.val: dfs(node.right)
            else: return 

        dfs(root)
        return lca[0]
    
#----------------------------------------------------------------------------------#
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        curr = root
        while curr:
            if curr is p or curr is q: return curr
            elif p.val < curr.val and q.val < curr.val: curr = curr.left
            elif p.val > curr.val and q.val > curr.val: curr = curr.right
            else: return curr
