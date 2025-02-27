// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq_1, seq_2 = [], []
        def leafSeq(root, seq):
            if root:
                leafSeq(root.left, seq)
                if not root.left and not root.right:
                    seq.append(root.val)
                leafSeq(root.right, seq)
            return seq
        if leafSeq(root1, seq_1) == leafSeq(root2, seq_2):
            return True
        return False
        