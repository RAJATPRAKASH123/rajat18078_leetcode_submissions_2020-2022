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
        if n == 1:
            return head.next
        def remove_nth(head, n, prev):
            if n == -1:
                prev.next = head.next
                return 
            remove_nth(head.next, n-1, head)
            return head
        return remove_nth(head, n, None)