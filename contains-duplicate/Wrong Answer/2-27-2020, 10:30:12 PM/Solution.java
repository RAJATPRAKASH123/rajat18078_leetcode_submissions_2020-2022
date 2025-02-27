// https://leetcode.com/problems/contains-duplicate

class Solution {
    public boolean containsDuplicate(int[] nums) {
        int temp = Integer.MIN_VALUE;
        for ( int i = 0; i < nums.length; i++ ){
            if ( temp < nums[i] )
            {
                temp = nums[i];
            }
        }
        for ( int i = 0; i < nums.length; i++ )
        {
            temp = temp ^ nums[i];
            if ( temp == 0 )
            {
                return true;
            }
        }
        return false;
    }
}