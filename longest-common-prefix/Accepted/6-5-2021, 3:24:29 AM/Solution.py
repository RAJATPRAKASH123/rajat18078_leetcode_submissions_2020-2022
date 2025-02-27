// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = 0
        temp = True
        for i in range(len(min(strs))):
            for word in strs[1:]:
                temp = word[cur] == strs[0][cur]
                if not temp:
                    if cur == 0:
                        return ""
                    return strs[0][:cur]
            cur += 1
        return strs[0][:cur]
            