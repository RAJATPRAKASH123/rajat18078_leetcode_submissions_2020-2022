// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:

    def recoverFromPreorder(self, s: str) -> TreeNode:
        # count
        node_dash = []
        i = 0
        while i < len(s):
            if s[i] != '-':
                count_nums = 0
                res = ""
                while i < len(s) and s[i] != '-':
                    res += s[i]
                    i += 1
                    count_nums += 1
                node_dash.append(int(res))
            else:
                count_dashes = 0
                while s[i] == '-':
                    count_dashes += 1
                    i += 1
                node_dash.append(count_dashes)
        # print(node_dash)
        def createTree(l, r, level=1):
            if l < 0 or r > len(node_dash) or r - l <= 0:
                return None
            root = TreeNode(int(node_dash[l]))
            l_node, r_node = None, None
            flag = True
            for i in range(l+1,r,2):
                # print(i, node_dash[i], level)
                if flag and node_dash[i] == level:
                    flag = False
                    l_node = i+1
                else:
                    if node_dash[i] == level:
                        r_node = i+1
            # print(l_node, r_node)
            if l_node and r_node:
                root.left = createTree(l+2, r_node-1, level + 1 )
                root.right = createTree(r_node, r, level + 1 )
            elif l_node:
                root.left = createTree(l+2, r, level + 1 )
            return root
        return createTree(0, len(node_dash))