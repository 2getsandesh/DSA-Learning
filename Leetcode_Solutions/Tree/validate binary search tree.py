class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left,right):
            if not node: return True
            if not left<node.val<right: return False
            if valid(node.left, left, node.val) and valid(node.right, node.val, right): return True
            
        return valid(root, float("-inf"), float("inf"))