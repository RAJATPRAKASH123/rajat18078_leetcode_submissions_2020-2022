// https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.leftSum=[]
        temp = 0
        for i in self.nums:
            temp = temp + i
            self.leftSum.append(temp)
            

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.leftSum[j]
        return self.leftSum[j] - self.leftSum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)