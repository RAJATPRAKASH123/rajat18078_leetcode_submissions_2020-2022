// https://leetcode.com/problems/counting-bits

import math
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans = [0,1]
        for i in range(1, math.ceil(log2(num))+1):
            temp = []
            for k in ans:
                temp.append(k+1)
            ans.extend(temp)
        return ans[:num+1]
'''
0 - 0        
1 - 1

2 - 1
3 - 2

4 - 1
5 - 2
6 - 2
7 - 3

8 - 1
9 - 2
10 - 2
11 - 3
12 - 2
13 - 3
14 - 3
15 - 4

16 - 1
17 - 2
18 - 2
19 - 3

20 - 2
21 - 3
22 - 3
23 - 4

24 - 2
25 - 3
26 - 3
27 - 4

28 - 3
29 - 4
30 - 4
31 - 5
32 - 1
'''
