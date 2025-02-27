// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(root):
            ans = 0
            queue = [root]
            while queue:
                temp_queue = []
                while queue:
                    node = queue.pop()
                    if node.left:
                        temp_queue.append(node.left)
                    if node.right:
                        temp_queue.append(node.right)
                if temp_queue:
                    queue = temp_queue
                else:
                    break
                # print(queue, 15)
                ans = 0
                for i in queue:
                    ans += i.val
            return ans
        return helper(root)