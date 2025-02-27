// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        max_index = height.index(max(height))
        
        # 0 -> max_index
        # max_index -> len(height)-1
        
        def trapWater(arr):
            stack = []
            next_greater = []
            for i in range(len(arr)-1, -1, -1):
                
                while stack and arr[i] > arr[stack[-1]]:
                    stack.pop()
                if stack and arr[i] <= arr[stack[-1]]:
                    next_greater = [stack[-1]] + next_greater
                    stack.append(i)
                else:
                    next_greater = [-1] + next_greater
                    stack.append(i)
            left = 0
            water = 0
            # print(next_greater)
            while left < len(arr)-1:
                if next_greater[left] == -1:
                    break
                for i in range(left, next_greater[left]):
                    water += arr[left]- arr[i]
                left = next_greater[left]
            return water
            
        return  trapWater(height[:max_index+1]) + trapWater(height[max_index:][::-1] )