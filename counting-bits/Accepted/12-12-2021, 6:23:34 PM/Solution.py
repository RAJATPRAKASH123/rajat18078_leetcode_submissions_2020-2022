// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        
#         recursive approach
        # if n <= 1:
        #     return [n]
        # # if n - 2 ** int(math.log2(n)) 
        # return [1 + self.countBits(n - 2 ** int(math.log2(n)) )[0] ]
        
#         dp
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        count_arr = [0] * (n + 1)
        count_arr[1] = 1
        for i in range(2, n+1):
            count_arr[i] = 1 + count_arr[i - 2 ** int(math.log2(i))]
        return count_arr
'''

20 : 10100

recursive relation : 
 number of bits(20) = 1 + number of bits(20 - 2 ** int(log2(20)) )
 
 countBits(i) = 1 + countBits(i - 2 ** int(math.log2(i)) )

Recursive function -> implement recursive function -> use dictionary
to memoize(memoization) -> use array for dp

'''