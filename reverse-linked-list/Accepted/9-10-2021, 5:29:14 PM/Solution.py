// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            if not head:
                return head
            if not head.next:
                return head
            cur = helper(head.next)
            head.next.next = head# 5.next = 4
            head.next = None
            return cur
        return helper(head)
'''
1 -> 2 -> 3 -> 4 -> 5
'''