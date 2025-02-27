// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, ino: List[int]) -> Optional[TreeNode]:
        
        def createBST(nums):
            if not nums:
                return
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            mid = len(nums)//2
            cur_node = TreeNode(nums[mid])
            
            cur_node.left = createBST(nums[:mid])
            cur_node.right = createBST(nums[mid+1:])
            return cur_node
        
        return createBST(ino)