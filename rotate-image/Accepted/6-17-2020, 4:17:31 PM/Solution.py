// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(arr)
        for i in range(l):
            for j in range(i, l):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for i in range(l):
            for j in range(l//2):
                arr[i][j], arr[i][l-j-1] = arr[i][l-j-1], arr[i][j]