// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = []
        self.cur = 0
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)
        inorder(root)
    def next(self) -> int:
        ans = self.res[self.cur]
        self.cur += 1
        return ans

    def hasNext(self) -> bool:
        return self.cur < len(self.res)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()