// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque()
        n = len(nums)
        res = []
        i = 0
        for j in range(n):
            while mono_queue and nums[j] >= nums[mono_queue[-1]]:
                mono_queue.pop()
            mono_queue.append(j)
            while j - mono_queue[0] >= k:
                mono_queue.popleft()
            if j - i + 1 == k:
                res.append(nums[mono_queue[0]])
                i += 1
            # print(mono_queue)
        return res
'''

1 3 -1 -3 5 3 6 7

https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript

We have nums array
Now, while sliding the window
we will create a monotonic queue (a queue in increasing order)
i.e. if cur >= 

'''