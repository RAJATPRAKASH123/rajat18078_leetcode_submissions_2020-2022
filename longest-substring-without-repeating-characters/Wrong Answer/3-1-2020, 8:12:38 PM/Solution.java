// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if ( s.length() == 0)
        {
            return 0;
        }
        if ( s.length() == 1 )
        {
            return 1;
        }
        HashSet<Character> h = new HashSet<Character>();
        int count = 0;
        int temp = -1;boolean papa = false;
        for ( int i = 0; i < s.length(); i++ )
        {
            if (!h.contains(s.charAt(i))){
                papa = false;
                count++;
            }else{
                if ( temp < count )
                {
                    temp = count;
                }
                if ( !papa )
                {
                    count--;
                }
                papa = true;
                    
            }
            h.add(s.charAt(i));
            //System.out.println(temp);
        }
        if ( temp == -1 )
        {
            temp = count;
        }
        return temp;
    }
}