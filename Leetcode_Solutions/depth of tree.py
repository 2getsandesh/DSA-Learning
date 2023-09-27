# To find the depth of a biary tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:          
            return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
    
#--------------------------------------------------------------------------------------------------------#

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1