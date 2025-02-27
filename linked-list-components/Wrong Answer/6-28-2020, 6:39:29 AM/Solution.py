// https://leetcode.com/problems/linked-list-components

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = head
        ans = 0
        if not head.next:
            if head.val in G:
                return 1
            return 0
        while temp.next:
            if temp.val in G and temp.next.val in G:
                p = True       
            elif temp.val in G or temp.next.val in G:
                ans += 1
            temp = temp.next
        return ans