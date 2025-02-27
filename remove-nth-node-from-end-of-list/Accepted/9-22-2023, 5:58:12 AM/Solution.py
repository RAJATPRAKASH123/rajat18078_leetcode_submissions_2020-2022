// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        cur = head
        count = 0
        prevToNthFromLast = None
        nthFromLast = head
        while cur:
            if count >= n:
                prevToNthFromLast = nthFromLast
                nthFromLast = nthFromLast.next
            cur = cur.next
            count += 1
        if not prevToNthFromLast:
            return head.next
        prevToNthFromLast.next = nthFromLast.next
        return head
'''
nth
cur

[1,2,3,4,5]
       p   c

'''