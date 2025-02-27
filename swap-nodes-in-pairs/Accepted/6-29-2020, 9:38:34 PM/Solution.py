// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return 
        if not head.next:
            return head
        prev = None
        cur = head
        nt = head.next
        ans = None
        while cur:
            if not nt:
                break
            temp = nt.next
            nt.next = cur
            if not prev:
                ans = nt
                
            else:
                prev.next = nt
            cur.next = temp
            prev = cur
            cur = temp
            if cur:
                nt = cur.next
        return ans
'''
None - > 1 -> 2 -> 3 -> 4
    p    c    nt
         2 -> 1 -> 3 -> 4 -> 5
                   
                    
store n.next
if n.next:
    c = n.next
c.next = p
'''