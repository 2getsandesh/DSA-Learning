'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself'''

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True
        if not root: return False
        if self.same(root,subRoot): return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
    def same(self,p,q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val == q.val:
                return self.same(p.left,q.left) and self.same(p.right, q.right)