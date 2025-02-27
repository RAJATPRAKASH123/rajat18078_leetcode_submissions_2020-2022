// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, l, r):
            m = (l + r)//2
            temp_node = TreeNode(0)
            if l <= r:
                temp_node.val = nums[m]
                temp_node.left = helper(nums, l, m - 1)
                temp_node.right = helper(nums, m + 1, r)
                return temp_node
            return None
        return helper(nums, 0, len(nums) - 1)