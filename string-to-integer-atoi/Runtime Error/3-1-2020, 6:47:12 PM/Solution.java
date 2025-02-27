// https://leetcode.com/problems/string-to-integer-atoi

class Solution {
    public int myAtoi(String str) {
        
        for ( int i = 0; i < str.length(); i++ )
        {
            if ( str.charAt(i) == '-')
            {
                String nn = str.substring(i + 1, str.length());
                return Integer.valueOf(nn) * -1;
            }
        }
        return Integer.valueOf(str);
    }
}