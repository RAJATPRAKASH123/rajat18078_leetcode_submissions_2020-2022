// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(",")
        print(preorder)
        for i in preorder:
            if i != "#" or len(stack) < 2:
                stack.append(i)
                continue
            if stack[-1] != "#":
                stack.append(i)
                continue
            if len(stack) >= 2 and stack[-1] == "#":
                stack.pop()
                if not stack:
                    return False
                stack.pop()
                stack.append("#")
            
        print(stack)
        return stack == ["#"]
        
        
'''
analysis : stack, preorder

whenever len(stack) >= 2 and stack[-1] == '#' and stack[-2] == "#":
    pop()
    pop()


'''