// https://leetcode.com/problems/maximum-subarray

class Solution {
    public int maxSubArray(int[] nums) {
        int i = Integer.MAX_VALUE;int temp1 = 0;
        int j = Integer.MIN_VALUE;int temp2 = 0;
        if ( nums.length == 1)
        {
            return nums[0];
        }
        if ( nums.length == 0)
        {
            return 0;
        }
        for ( int k = 1; k< nums.length; k++ )
        {
            nums[k] += nums[k-1];
        }
        for ( int k = 0; k < nums.length; k++)
        {
            if ( i > nums[k] )
            {
                i = nums[k];temp1 = k;
            }
            if ( j < nums[k] )
            {
                j = nums[k];temp2 = k;
            }
        }
        return nums[temp2] - nums[temp1];
    }
}