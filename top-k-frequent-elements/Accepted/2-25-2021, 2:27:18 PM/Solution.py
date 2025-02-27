// https://leetcode.com/problems/top-k-frequent-elements

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        elem_freq_arr = []
        for key in frequency:
            elem_freq_arr.append([key, frequency[key]])
            
        elem_freq_arr.sort(key = lambda x : x[1])
        res = []
        for i, j in elem_freq_arr[-1:-k-1:-1]:
            res.append(i)
        return res