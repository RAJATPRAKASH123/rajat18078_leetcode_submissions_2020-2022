// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # ans = ""
        # while head:
        #     ans+=str(head.val)
        #     head = head.next
        # return int(ans,2)
        ans=0
        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans