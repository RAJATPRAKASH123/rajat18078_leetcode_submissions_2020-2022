// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        pos = length - n
        
        prev = head
        if pos == 0:
            return head.next
        while pos != 0:
            pos -= 1
            if pos == 0:
                if not prev.next:
                    prev.next = None
                else:
                    prev.next = prev.next.next
                break
            prev = prev.next
        return head