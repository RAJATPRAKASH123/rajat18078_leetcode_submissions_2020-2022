// https://leetcode.com/problems/single-number

class Solution {
    public int singleNumber(int[] nums) {
        for ( int i = 1; i < nums.length; i++ )
        {
            temp[0] = temp[0] ^ nums[i];
        }
        return temp[0];
    }
}