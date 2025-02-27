// https://leetcode.com/problems/create-maximum-number

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        we_can_leave = n1 + n2 - k
        
        i, j = 0, 0
        soln = []
        while i < n1 and j < n2 and k != 0:
            
            temp = nums1[i]
            idx = i
            for cur in range(i, min(i + we_can_leave + 1, n1)):
                if temp < nums1[cur]:
                    temp = nums1[cur]
                    idx = cur
            idx1 = idx
            temp1 = temp
            
            temp = nums2[j]
            idx = j
            for cur in range(j, min(j + we_can_leave + 1, n2)):
                if temp < nums2[cur]:
                    temp = nums2[cur]
                    idx = cur
            idx2 = idx
            temp2 = temp
            
            if nums1[idx1] > nums2[idx2]:
                soln.append(temp1)
                k -= 1
                we_can_leave -= idx1 - i
                i = idx1 + 1
            elif nums1[idx1] < nums2[idx2]:
                soln.append(temp2)
                k -= 1
                we_can_leave -= idx2 - j
                j = idx2 + 1
            else:
                f = self.maxNumber(nums1[idx1+1:], nums2[j:], k-1)
                s = self.maxNumber(nums1[i:], nums2[idx2+1:], k-1)
                soln.append(nums1[idx1])
                # print(f,s)
                for i, j in zip(f,s):
                    if i > j:
                        if f:
                            soln += f
                        return soln
                    elif i < j:
                        if s:
                            soln += s
                        return soln
                if f:
                    soln += f
                return soln
        while i < n1 and k != 0:
            
            temp = nums1[i]
            idx = i
            for cur in range(i, min(i + we_can_leave + 1, n1)):
                if temp < nums1[cur]:
                    temp = nums1[cur]
                    idx = cur

            soln.append(temp)
            we_can_leave -= idx - i
            i = idx + 1
            k -= 1
            
            # print(soln, k)

        while j < n2 and k != 0:
            temp = nums2[j]
            idx = j
            for cur in range(j, min(j + we_can_leave + 1, n2)):
                if temp < nums2[cur]:
                    temp = nums2[cur]
                    idx = cur
            soln.append(temp)
            we_can_leave -= idx - j
            j = idx + 1
            k -= 1
            # print(soln, k)
        return soln