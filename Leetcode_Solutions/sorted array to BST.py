class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l,r = 0,len(nums)-1

        def bst(l,r):
            if l>r: return None
            mid = (l + r)//2
            node = TreeNode(nums[mid])
            node.left = bst(l,mid-1)
            node.right = bst(mid+1,r)
            return node
        return bst(l,r)