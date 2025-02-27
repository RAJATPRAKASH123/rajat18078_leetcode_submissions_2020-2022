// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
    public int removeDuplicates(int[] nums) {
        if ( nums.length == 0 )
        {
            return 0;
        }
        int count = 1;
        int temp = 0;
        for ( int i = 1; i < nums.length; i++ )
        {
            if ( nums[i] != nums[i - 1])
            {
                count++;
                nums[count - 1] = nums[i];
            }
        }
        nums[count] = nums[nums.length - 1];
        return count;
    }
}