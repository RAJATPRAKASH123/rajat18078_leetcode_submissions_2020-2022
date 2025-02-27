// https://leetcode.com/problems/longest-increasing-subsequence

class Solution {
    public int lengthOfLIS(int[] nums) {
        
        int n = nums.length;
        
        int[] new_nums = new int[n+1]; 
        
        for( int i = 0; i < n; i++ ){
            new_nums[i] = nums[i];
        }
        new_nums[n] = 100000000;
        
        int[][] dp = new int[n+1][n+1];
        for (int i = 0; i < n+1; i++){
            for ( int j = 0; j < n+1; j++){
                dp[i][j] = -1;    
            }
        }
        return helper( new_nums, n-1, n, dp);
    }
    public int helper( int[] arr,int i,int nextt, int[][] dp ){
        
        if (i == -1){return 0;}
        int cur = -1;
        if (dp[i][nextt] != -1){
            return dp[i][nextt];
        }
        for (int t = i; t > -1; t--){
            if (arr[t] < arr[nextt]){
                cur = t;
                break;
            }
        }
        if (cur == -1){return 0;}
        
        dp[i][nextt] = Math.max( 1 + helper( arr, cur-1, cur , dp), helper( arr, cur-1, nextt, dp ));
        return dp[i][nextt];
    }
}