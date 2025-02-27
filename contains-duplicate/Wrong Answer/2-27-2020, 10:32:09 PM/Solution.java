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
        int count = 0;
        for ( int i = 0; i < nums.length; i++ )
        {
            if (nums[i] != 0 )
            {
                temp = temp ^ nums[i];
                if ( temp == 0 || count == 2 )
                {
                    return true;
                }
            }else{
                count++;
            }
        }
        return false;
    }
}