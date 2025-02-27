// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        if not preorder:
            return True
        valid_pos = 1
        
        for i in preorder:
            if valid_pos == 0:
                return False
            if i == '#':
                valid_pos -= 1
            else:
                valid_pos += 1
                
        return valid_pos == 0

'''
preoorder

idx = 0


'''