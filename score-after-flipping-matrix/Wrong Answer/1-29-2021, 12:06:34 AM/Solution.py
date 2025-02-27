// https://leetcode.com/problems/score-after-flipping-matrix

class Solution:
    def matrixScore(self, arr: List[List[int]]) -> int:
        
        
        for i in range(len(arr)):
            temp = ''
            for j in arr[i]:
                temp += str(j)
            temp2 = ''
            for c in temp:
                if c == '0':
                    temp2 += '1'
                else:
                    temp2 += '0'
            if int(temp, 2) > int(temp2,2):
                continue
            else:
                temp2 = list(temp2)
                arr[i] = [int(t) for t in temp2]
        ans = 0
        print(arr)
        for j in range(len(arr[0])):
            temp = 0
            for i in range(len(arr)):
                if arr[i][j] == 1:
                    temp += 1
            temp = max(temp, len(arr)-temp)
            # print(temp)
            ans += temp*(2**(j))
        return ans

'''     
0
1


[[1, 1, 0, 0],
[1, 0, 1, 0],
[1, 1, 0, 0]]


[[0,0,1,1],
 [1,0,1,0],
 [1,1,0,0]]
 
 1 1 1 1
 1 0 0 1
 1 1 1 1
'''