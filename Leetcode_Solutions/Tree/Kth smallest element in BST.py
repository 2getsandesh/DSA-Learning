'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            if len(li) == k: return 
            li.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return li[-1]