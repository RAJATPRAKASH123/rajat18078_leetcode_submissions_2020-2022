// https://leetcode.com/problems/reverse-string

class Solution {
public: // access specifiers
    
    void reverseRec(vector<char>& s, int i, int j){
        if ( i>= j){
            return;
        }
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        reverseRec(s, ++i, --j);
    }
    void reverseString(vector<char>& s) {
          int i = 0;
          int j = s.size() - 1;
          reverseRec(s, i, j );  
    }
};

/*
class Solution {
public:
    void reverseRec(vector<char>& s, int i, int j){
        if i >= j:
        return;
        // swap i and jth value
    }
    void reverseString(vector<char>& s) {
          int i = 0;
          int j = s.size() - 1;
          reverseRec(s, i, j );
    }
            
            
        }
*/
