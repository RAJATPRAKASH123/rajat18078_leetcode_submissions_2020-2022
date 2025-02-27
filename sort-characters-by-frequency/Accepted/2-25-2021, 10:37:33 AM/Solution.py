// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        frequency = [[i, 0] for i in range(255)]
        
        for alphabet in s:
            frequency[ord(alphabet)][1] += 1
            
        frequency.sort(key=lambda x : x[1])

        res = ""
        for i in frequency[::-1]:
            res += chr(i[0]) * i[1]
        return res