'''Given a binary tree, determine if it is height-balanced
ie, |Left Height - Right Height| should be less than one'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node: return [True,0]

            L = height(node.left)
            R = height(node.right)
            balanced = True if L[0] and R[0] and abs(L[1]-R[1]) <= 1 else False
            
            return [balanced, 1 + max(L[1],R[1])]   
            
        res = height(root)
        return res[0]