// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        if head and head.val == val:
            return
        prev = None
        cur = head
        while cur:
            if prev and cur.val == val:
                cur = cur.next
                prev.next = cur
                continue
            if not prev and cur.val == val:
                cur = cur.next
                head = head.next
                continue
            cur = cur.next
            if not prev:
                prev = head
            else:
                prev = prev.next
        return head