// https://leetcode.com/problems/rotate-array

class Solution {
    public void rotate(int[] nums, int k) {
        int l = nums.length;
        if ( k % l == 0 )
        {
            return;
        }
        int count = 0;int i = 0;
        int temp1 = nums[0];
        int temp2 = 0;
        while ( count != nums.length )
        {
            temp2 = nums[( i + k) % l];
            nums[( i + k) % l] = temp1;
            temp1 = temp2;
            i = ( i + k) % l;
            count++;
        }
        return;
    }
}