// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(merged, left, right):
            # iterators for merged, left, right
            i, j  = 0, 0
            count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged[count] = left[i]
                    i += 1
                else:
                    merged[count] = right[j]
                    j += 1
                count += 1
            while i < len(left):
                merged[count] = left[i]
                count += 1
                i += 1
            while j < len(right):
                merged[count] = right[j]
                count += 1
                j += 1
            return merged
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(arr.copy(), left, right)
        return mergeSort(nums)