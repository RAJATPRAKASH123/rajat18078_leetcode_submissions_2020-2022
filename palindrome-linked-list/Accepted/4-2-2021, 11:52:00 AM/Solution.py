// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        temp = head
        nodes = 0
        while temp:
            temp = temp.next
            nodes += 1
        cur = head
        for i in range(nodes//2):
            cur = cur.next
        if nodes % 2 == 1:
            cur = cur.next
        
        # reversing the half linked list
        prev = None
        next_node = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        temp_sec = prev
        temp_fir = head
        while temp_sec:
            if temp_fir.val != temp_sec.val:
                return False
            temp_fir = temp_fir.next
            temp_sec = temp_sec.next
        return True