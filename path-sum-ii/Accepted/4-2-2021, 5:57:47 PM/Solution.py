// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ceck_node = root
        res = []
        def helper(root, target, ans = []):
            if not root:
                return
            if not root.left and not root.right:
                if target == root.val:
                    ans.append(root.val)
                    res.append(ans)
                return 

            helper(root.left, target - root.val, ans + [root.val])
            helper(root.right, target - root.val, ans + [root.val])
        helper(root, targetSum)
        return res