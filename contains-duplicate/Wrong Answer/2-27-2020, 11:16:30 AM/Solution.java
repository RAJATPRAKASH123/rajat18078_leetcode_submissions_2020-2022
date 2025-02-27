// https://leetcode.com/problems/contains-duplicate

class Solution {
    public boolean containsDuplicate(int[] nums) {
        if ( nums.length <= 1 )
        {
            return false;
        }
        int t = nums[0];
        for ( int i = 1; i < nums.length; i++ )
        {
            t = t ^ nums[i];
            if ( t == 0 )
            {
                return true;
            }
        }
        return false;
    }
}