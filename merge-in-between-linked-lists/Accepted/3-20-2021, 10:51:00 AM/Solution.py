// https://leetcode.com/problems/merge-in-between-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        count = 0
        prev_a = None
        while count != b:
            if count < a:
                prev_a = head
            head = head.next
            count += 1
        
        if prev_a is None:
            list2.next = head.next
            return list2
        prev_a.next = list2
        while list2.next is not None:
            list2 = list2.next
        list2.next = head.next
        return list1