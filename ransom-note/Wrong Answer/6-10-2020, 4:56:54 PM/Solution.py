// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        visited = [True]*len(magazine)
        for j in ransomNote:
            papa = True
            for i in range(len(magazine)):
                if visited[i]:
                    if magazine[i] == j:
                        visited[i] = False
                        papa = False
            if papa:
                return False
        return True