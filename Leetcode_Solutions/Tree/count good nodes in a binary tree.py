'''Within a binary tree, a node x is considered good if the path from the root of the tree 
to the node x contains no nodes with a value greater than the value of node x
Given the root of a binary tree root, return the number of good nodes within the tree.'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(node,v):
            if not node: return
            if node.val >= v:
                count[0]+=1
            v = max(v,node.val)
            dfs(node.left,v)
            dfs(node.right,v)
        dfs(root,root.val)
        return count[0]