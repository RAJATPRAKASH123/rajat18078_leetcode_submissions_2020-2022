// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count=0
        def helper(head):
            nonlocal n
            nonlocal count
            if head is None:
                return
            helper(head.next)
            count += 1
            if count == n:
                if head and head.next:
                    head.val = head.next.val
                    head.next=head.next.next
                else:
                    head=None
            return head
        return helper(head)