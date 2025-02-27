// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        prev = None
        cur = head
        nextNode = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        head = prev
        return head

            
'''
None< - 1 <- 2  3
             p  c, n

'''