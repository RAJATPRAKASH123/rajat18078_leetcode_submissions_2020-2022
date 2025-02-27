// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, a):
        len_a = 0
        temp = a
        while temp:
            len_a += 1
            temp = temp.next
        return len_a
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return
        len_a = self.getLength(a)
        len_b = self.getLength(b)
        if len_a > len_b:
            a,b = b, a
        for i in range(abs(len_b - len_a)):
            b = b.next
        while a and b:
            if a == b:
                return a
            a = a.next 
            b = b.next