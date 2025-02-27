// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26
        for i in s:
            freq[ord(i)-97] += 1
        freq.sort()
        right = 25; visited = set()
        count = 0
        while right != -1:
            if freq[right] == 0:
                count += sum(freq[:right])
                break
            if freq[right] in visited:
                freq[right] -= 1
                count += 1
                continue
            visited.add(freq[right])
            right -= 1
            
        return count