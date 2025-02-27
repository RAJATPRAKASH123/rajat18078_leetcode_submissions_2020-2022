// https://leetcode.com/problems/contains-duplicate

import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> h = new HashSet<Integer>();
        for ( int i = 0; i < nums.length ; i++ )
        {
            int temp1 = h.size();
            h.add(nums[i]);
            if ( h.size() == temp1 )
            {
                return true;
            }
        }
        return false;
    }
}