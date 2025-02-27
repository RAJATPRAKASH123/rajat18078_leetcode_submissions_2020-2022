// https://leetcode.com/problems/rotate-array

class Solution {
    static int gcd( int a, int b )
    {
        if ( b == 0 )
        {
            return a;
        }else{
            return gcd(b, a % b);
        }
    }
    public void rotate(int[] nums, int k) {
        int temp1 = 0, temp = 0;
        for ( int i = 0; i < gcd(nums.length, k ); i++)
        {
            int c = 0, j = i;
            while ( c != nums.length/gcd(nums.length, k) )
            {
                c++;
                if ( j == i){
                    temp = nums[j];
                    temp1 = nums[(j + k) % nums.length ];
                }else{
                    temp = temp1;
                    temp1 = nums[(j + k) % nums.length ];
                }
                //System.out.println(temp);
                nums[(j + k) % nums.length ] = temp;
                j += k;
            }
        }
    }
}