// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         two traversal , this is faaltu
#         one traversal , use fundamental of tortoise and hare ( fast and slow pointer)    
#         concept : use two pointers at a time to traverse a single linked list and
#         keep track of two positions (in a single traversal).
        # 1 2 3 4 5 : n = 2
#             p   q
        
        p = head
        q = head
        count = n 
        while ( count != 0):
            q = q.next
            count -= 1
        if not q:
            return head.next
        while q.next:
            q = q.next
            p = p.next
        if not p.next:
            p.next = None
        else:
            p.next = p.next.next
        return head
        