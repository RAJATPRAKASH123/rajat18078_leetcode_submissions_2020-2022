// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        count, cur, prev = 0, head, None
        while cur:
            count += 1
            prev = cur
            cur = cur.next
        if k % count == 0:
            return head
        k = count - k%count
        cur = head
        while k != 1:
            cur = cur.next
            k -= 1
        fut = cur.next
        cur.next = None
        prev.next = head
        return fut