// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        pairs = defaultdict(int)
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(i)
                continue
            if s[i] == ']':
                pairs[stack.pop()] = i
        
        def helper(s, left, right):
            if left == right:
                return s[left]
            if left > right:
                return ""
            if s[left].isalpha():
                return s[left] + helper(s, left+1, right)
            int_index = -1
            for i in range(left, right):
                if s[i] == '[':
                    int_index = i
                    break
            if int_index == -1:
                return ""
            # print(int_index)
            num = int(s[left:int_index])
            return num * helper(s, int_index + 1, pairs[int_index] - 1 ) + helper(s, pairs[int_index] + 1, right)
        
        return helper(s, 0, len(s)-1)
'''
"3 [a 2[c] ] "

223[abc]


3 * helper("a2[c]") -> "a" + 2 * helper("c")

'''