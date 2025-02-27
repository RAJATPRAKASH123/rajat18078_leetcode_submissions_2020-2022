// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

class Solution:
    def count_1s(self, n):
        ans = 0
        for i in range(15):
            if n & 1 << i != 0:
                ans += 1
        return ans
    def merge(self, arr,c,  l, r, m):
        i, j = l, m+1
        temp_arr, temp_c = [], []
        while i < m+1 and j < r+1:
            if c[i] < c[j] or (c[i] == c[j] and arr[i] < arr[j]):
                temp_arr.append(arr[i])
                temp_c.append(c[i])
                i += 1
            else:
                temp_arr.append(arr[j])
                temp_c.append(c[j])
                j += 1
        temp_arr.extend(arr[i:m+1] + arr[j:r+1])
        temp_c.extend(c[i:m+1] + c[j:r+1])
        arr[l:r+1] = temp_arr[:r-l+1]
        c[l:r+1] = temp_c[:r-l+1]
            
    def mergeSort(self,arr, c, l, r):
        if l < r:
            m = (l + r)//2
            self.mergeSort(arr, c, l, m)
            self.mergeSort(arr, c, m+1, r )
            self.merge(arr, c, l, r, m)
            return arr
    def sortByBits(self, arr: List[int]) -> List[int]:
        c = [self.count_1s(i) for i in arr]
        return self.mergeSort(arr, c, 0, len(arr) - 1)

'''
    def sortByBits(self, A):
        return sorted(A, key=lambda a: [bin(a).count('1'), a])
'''
'''

class Solution(object):
    def sortByBits(self, arr):
        res = []
        for num in arr:
            ones = self.countBits(num)
            res.append((ones, num))
        heapq.heapify(res)
        finalres = []
        while len(res)>0:
            finalres.append(heappop(res)[1])
        return finalres
    
    def countBits(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
            n >>= 1
        return count
'''