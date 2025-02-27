// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        temp = head
        count = 0
        prev_b = None
        while temp:
            count += 1
            prev_b = temp
            temp = temp.next
        if k % count == 0:
            return head
        k = count - k % count
        if k % count == 1:
            prev_b.next = head
            cc = head.next
            head.next = None
            return cc
        temp = head
        count = 1
        cur = head
        prev = None
        while cur.next:
            if k <= count + 1:
                if head:
                    prev = head
                head = head.next
            cur = cur.next
            count += 1
        if prev:
            prev.next = None
        cur.next = temp
        return head