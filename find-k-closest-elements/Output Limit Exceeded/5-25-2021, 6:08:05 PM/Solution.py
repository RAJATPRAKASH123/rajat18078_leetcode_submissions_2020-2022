// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def binSearch(arr, left, right, target):
            
            while left < right:
                print(left, right)
                mid = (left+right)//2
                if target >= arr[mid]:
                    left = mid
                else:
                    right = mid-1
            return left
        pivot = binSearch(arr, 0, len(arr)-1, x)
        
        print(pivot)
        left = max(pivot-k+1-2, 0 )
        right = min(len(arr)-1, left + k-1+2)
        print(left, right)
        while abs(arr[left]-x) > abs(arr[min(right,left+k)]-x):
            # print(abs(arr[min(right,left+k)]-x))
            left += 1
            
            if right == left+k:
                break
        return arr[left:left+k]