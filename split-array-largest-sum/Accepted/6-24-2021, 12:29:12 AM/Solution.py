// https://leetcode.com/problems/split-array-largest-sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == len(nums):
            return max(nums)
        low, high = max(nums), sum(nums)

        def checkIt(cur):
            nonlocal m
            parts = m
            sum = 0
            for i in range(len(nums)):
                sum += nums[i]
                if sum > cur:
                    sum = nums[i]
                    parts -= 1
            if sum != 0:
                parts -= 1
            if parts < 0:
                return False
            return True

        while low < high:
            cur = (low + high)//2
            if checkIt(cur):
                high = cur
            else:
                low = cur + 1
        return low
'''
Just share something like a trick or template for remembering about Binary Search.
[I can't explain] , but this [trick] seems to work.
I know we'd better understand the theory but this is just a trick for remembering.
When using Binary Search, it looks like to find the first T or the last F in FFFFFTTTTTTTTTTTT.(T means TRUE while F means FALSE.)

l <= r
This means l can be chosen, and r can be chosen i.e. [l, r]. (vec[0], ..., vec.back())
For example:
FFFFFFTTTTTT
↑..........↑
l..........r
[l,r]
If we want to find first T,
when mid is FALSE, the first T must on the right, so l = mid +1;
when mid is TRUE, just remember to do as we do in the simplest binary search such as finding a distinct number in an ascending array, i.e. r = mid-1;
Then it will end like this:

FFFFFTTTTTT
....↑↑
....rl
(l points to the first T, and r points to the last F)
So, if we want to find the first TRUE, we return l. If we want to find the last FALSE, we return r.
It seems that the Binary Search partitions the array to two parts:
[0,r] : F, [l, size-1] : T, and maybe that's why we update l and r in that way.
Code maybe like this:

int BinarySearch(){
	while(l<=r){
		int mid = l + (r-l)/2;
		if(TRUE(mid)){
			r = mid -1;
		}
		else{
			l = mid + 1;
		}
	}
	return l;// find the first T
	//return r;//find the last F
}
l < r
This means r can not be chosen, i.e. [l, r).(Think about vec.begin(), vec.end())
For example:
FFFFFFTTTTTT
↑...........↑
l...........r
[l,r)
Just remember to do as we do in the simplest binary search such as finding a distinct number in an ascending array.
If we want to find first T,
when mid is FALSE, so the first T must be on the right, l = mid+1;
when mid is TRUE, r = mid;(because r can not be chosen.)(Just remember to do as we do in the simplest binary search such as finding a distinct number in an ascending array).
Then it will end like this:

FFFFTTTTTTT
....↑
....l&&r
(l and r points to the first T)
So, if we want to find the first TRUE, we return l(or r); if we want to find the last FALSE, we return l-1(or r-1).
[0,r) : F, [l, size) : T
Code maybe like this:

int BinarySearch(){
    while(l<r){
        int mid = l + (r-l)/2;
        if(TRUE(mid)){
    		r =mid;
        }
        else{
        	l = mid +1;
        }
    }
    return l;//find the first T
	//return l-1;//find the last F
}
'''
'''
[2,3,1,2,4,3]

2  5  6  8  12  15


5






[7,2,5,10,8]  # sum = 32 -> 
2

cur = (10 + 32)//2 = 21

10 and 20 : (10+20)//2 = 15

 7  9  14  24  32
    
'''
    
    

    