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
        while temp:
            count += 1
            temp = temp.next
        k = count - k % count
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