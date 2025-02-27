// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = ListNode(0)
        res_track = res
        carry = 0
        while l1 or l2:
            
            first, second = 0, 0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val
                l2 = l2.next
            cur_digit = first + second + carry
            res.next = ListNode(cur_digit%10)
            carry = cur_digit // 10
            res = res.next
        if carry:
            res.next = ListNode(carry%10)
        return res_track.next
            
'''
   1 1 1 1
[9,9,9,9,9,9,9]
[9,9,9,9]
 8 9 9 9
 '''
