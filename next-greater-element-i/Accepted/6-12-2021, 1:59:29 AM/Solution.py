// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng_arr = [0] * (max(nums2) + 1)
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            # print(i, stack)
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack and nums2[i] < stack[-1]:
                ng_arr[nums2[i]] = stack[-1]
                stack.append(nums2[i])
            elif not stack:
                ng_arr[nums2[i]] = -1
                stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = ng_arr[nums1[i]]
        return nums1
            
            
'''
analysis : 

design : next_greater array
keep an array
traverse from last to first
keep the next max possiblities in the stack
'''