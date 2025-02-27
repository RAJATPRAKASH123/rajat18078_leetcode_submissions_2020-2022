// https://leetcode.com/problems/count-primes

class Solution {
    public int countPrimes(int n) {
        boolean[] arr = new boolean[n + 1];
        for ( int i = 2; i <= Math.sqrt(n); i++ )
        {
            if(arr[i] == true) 
            {
                continue;
            }
            for ( int j = 2 * i ; j <= n; j += i )
            {
                arr[j] = true;
            }
        }
        int count = 0;
        for ( int i = 2; i < n; i++ )
        {
            if ( arr[i] == false )
            {
                count++;
            }
        }
        return count;
    }
}