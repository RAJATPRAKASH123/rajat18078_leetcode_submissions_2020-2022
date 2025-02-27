// https://leetcode.com/problems/palindromic-substrings

class Solution {
    boolean[][] visited = null;
    int count = 0;
    public int countSubstrings(String s) {
        visited = new boolean[s.length()][s.length()];
        helper(s, 0, s.length() - 1);
        return count;
    }
    
    public void helper(String s, int si, int ei){
        if(si > ei){
            return;
        }
        
         if(visited[si][ei]){
             return;
         }
        
        if(s.charAt(si) == s.charAt(ei) && isPalindrome(s, si, ei)){
            count++;
        }
        
        helper(s, si + 1, ei);
        helper(s, si, ei - 1);
        
        visited[si][ei] = true;
        
    }
    
    public boolean isPalindrome(String s, int si, int ei){
        
        while(si <= ei){
            if(s.charAt(si) != s.charAt(ei)){
                return false;
            }
            si++;
            ei--;
        }
        
        return true;
    }
}