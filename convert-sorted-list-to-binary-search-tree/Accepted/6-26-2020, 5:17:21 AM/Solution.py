// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def len_ll(self, head):
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        return count
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        def helper(l, r):
            nonlocal head
            m = (l + r)//2
            if l <= r:
                left = helper( l, m- 1,)
                root = TreeNode(head.val)
                head = head.next
                right = helper( m + 1, r)
                root.left = left
                root.right = right
                return root
        return helper(0, self.len_ll(head)-1)