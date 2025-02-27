// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        def waterTrapped(arr):
            n = len(arr)
            nextGreater = [n]*(n) # or equal stack
            stack = []
            
            
            for i in range(n - 1, -1,-1):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                if stack:
                    nextGreater[i] = stack[-1]
                stack.append(i)
            # print(arr, nextGreater)
            
            cur = 0
            water = 0
            while cur != n-1:
                next = nextGreater[cur]
                water += (next - cur - 1) * arr[cur]
                for mid in range(cur+1, next):
                    water -= arr[mid]
                cur = next
            return water
        
        max_index = height.index(max(height))
        return waterTrapped(height[:max_index+1]) + waterTrapped(height[max_index:][::-1] )
                
            
        
'''
[0,1,0,2,1,0,1,3,2,1,2,1]

given an array: 
whose max is at the end, 
find next greater or equal and fill it , do it til the end
return
'''