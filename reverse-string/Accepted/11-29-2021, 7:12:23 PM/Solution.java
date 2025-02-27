// https://leetcode.com/problems/reverse-string

class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        reverseRec(s, left, right);
    }
    public static void reverseRec(char[] s, int left, int right){
//         swapping left and right
        if (left >= right){
            return;
        }
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        reverseRec(s, left + 1, right - 1);
    }
}