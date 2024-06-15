'''Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = [0]
        def height(node):
            if not node: return 0

            left_height = height(node.left)
            right_height = height(node.right)
            curr_diameter =  left_height + right_height
            max_diameter[0] = max(curr_diameter, max_diameter[0])

            return 1 + max(left_height, right_height)

        height(root)
        return max_diameter[0]