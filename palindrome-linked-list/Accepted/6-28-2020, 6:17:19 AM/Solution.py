// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, ll):
        count = 0
        temp = ll
        while temp:
            temp = temp.next
            count += 1
        return count
    def isPalindrome(self, head: ListNode) -> bool:
        l =  self.getLength(head)
        h_l = l//2
        prev = None
        cur = head
        nt = None
        while h_l != 0:
            nt = cur.next
            cur.next = prev
            prev = cur
            cur = nt
            h_l -= 1
        if l%2 == 0:
            temp1 = prev
            temp2 = cur
        if l%2 == 1:
            temp1 = prev
            temp2 = cur.next
        while temp1 and temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True