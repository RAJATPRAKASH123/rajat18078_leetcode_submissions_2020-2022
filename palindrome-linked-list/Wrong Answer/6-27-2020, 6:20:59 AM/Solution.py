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
        half_len_ll = self.getLength(head)//2
        mid = head
        while half_len_ll > 0:
            mid = mid.next
            half_len_ll -= 1
        def helper(left, mid, half_len_ll):
            if half_len_ll == 0:
                return True
            print(left.val)
            between_them = helper(left.next, mid.next, half_len_ll - 1)
            print(mid.val)
            return between_them and left.val == mid.val
        return helper(head, mid, half_len_ll)