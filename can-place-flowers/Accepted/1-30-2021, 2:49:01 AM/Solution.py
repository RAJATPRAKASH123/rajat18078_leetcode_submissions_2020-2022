// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        temp = 0
        for i in range(len(arr)):
            if arr[i] == 0 and (i-1 == -1 or arr[i-1] == 0) and (i+1 == len(arr) or arr[i+1] == 0):
                temp += 1
                arr[i] = '1'
        print(temp)
        if n > temp:
            return False
        return True
'''
arr: flowerbed


'''