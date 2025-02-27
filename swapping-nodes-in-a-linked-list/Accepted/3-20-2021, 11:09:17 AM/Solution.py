// https://leetcode.com/problems/swapping-nodes-in-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        start_head = head
        begin = None
        count = 1
        k_before = None
        
        flag_start = False
        
        while head:
            if count == k:
                begin = head
                flag_start = True
            if flag_start:
                if k_before is None: 
                    k_before = start_head
                else:
                    k_before = k_before.next
            head = head.next
            count += 1
        # print(begin.val, k_before.val)
        k_before.val, begin.val = begin.val, k_before.val
        return start_head