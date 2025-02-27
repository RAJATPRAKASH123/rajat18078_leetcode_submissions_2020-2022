// https://leetcode.com/problems/goal-parser-interpretation

class Solution:
    def interpret(self, command: str) -> str:
        i = 0; res = ""
        while i < len(command):
            if command[i] == 'G':
                i += 1
                res += "G"
                continue
            if command[i] == '(' and command[i+1] == ')':
                i += 2
                res += "o"
                continue
            else:
                i += 4
                res += "al"
        return res