// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        total_nodes = len(inorder)
        def search(arr, l , r, key):
            m = (l+r)//2
            # print(l, r)
            if l == r and key == arr[l]:
                return l
            if l < r:
                if key == arr[m]:
                    return m
                if key < arr[m]:
                    return search(arr, l, m, key)
                return search(arr, m+1, r, key)
            return -1
        def helper(li, ri, lp, rp):
            nonlocal postorder
            nonlocal inorder
            if li < ri and lp < rp:
                root = TreeNode(postorder[rp])
                idx_inorder = search(inorder, li, ri, root.val)
                if idx_inorder == -1:
                    return root
                print(idx_inorder)
                temp1 = root
                temp2 = root
                temp1.left = helper(li, idx_inorder - 1, lp, rp - (ri - idx_inorder) )
                temp2.right = helper(idx_inorder + 1, ri, idx_inorder , rp-1 )
                return root
            if li == ri:
                return TreeNode(inorder[li])
        return helper(0, total_nodes-1, 0, total_nodes-1)
'''     
inorder =   [1, 9, 3, 15, 20, 7]
            
postorder = [1, 9, 15, 7, 20, 3]


'''