// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            # head, head.next
            if not head or not head.next:
                return head
            res = head.next
            temp = head.next.next 
            head.next.next = head
            head.next = helper(temp)
            return res
        return helper(head)

'''
None

1 -> 2 -> 3 -> 4 -> 5 -> 6

2 -> 1 
'''