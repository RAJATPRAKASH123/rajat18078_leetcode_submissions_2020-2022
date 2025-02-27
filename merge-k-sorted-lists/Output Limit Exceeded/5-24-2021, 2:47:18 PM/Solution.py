// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, arr: List[ListNode]) -> ListNode:
        # arr : array of linkedLIsts
        if len(arr) == 0:
            return 
        if len(arr) == 1:
            return arr[0]
        def merge(left, right):
            merged = ListNode(-100000)
            temp = merged
            while left and right:
                if left.val > right.val:
                    merged.next = ListNode(right.val)
                    right = right.next
                else:
                    merged.next = ListNode(left.val)
                    left = left.next
                merged = merged.next
            if left:
                merged.next = left
            if right:
                merged.next = right
            return temp.next
        def mergeSort(arr, l=0, r=len(arr)-1):
            #base cases
            print(l,r, arr)
            if l > r:
                return
            if l == r:
                return arr[l]
            mid = (l+r)//2
            # dividing into two parts
            left = mergeSort(arr, l, mid)
            right = mergeSort(arr, mid+1, r)
            #merging
            return merge(left, right)
        return mergeSort(arr)