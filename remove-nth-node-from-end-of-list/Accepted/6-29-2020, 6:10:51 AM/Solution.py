// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        prev = None
        fut_cur = head
        cur = head
        count = 0
        flag = False
        while cur.next:
            count += 1
            if count == n or flag:
                flag = True
                prev = fut_cur
                fut_cur = fut_cur.next
            cur = cur.next
        if not prev:
            return head.next
        prev.next = prev.next.next
        return head