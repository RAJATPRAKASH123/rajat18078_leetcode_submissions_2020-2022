// https://leetcode.com/problems/reverse-bits

class Solution:
  def reverseBits(self, n: int) -> int:
    if n ==0:
      return 1<<31
    t = int(log2(n) +1)
    ans = 0
    for i in range(t+1):
      temp = n & 1<<i
      if temp != 0:
        
        ans += 1 << (31-i)
      #print(ans)
    return ans
'''
public int reverseBits(int n) {
    if (n == 0) return 0;
    
    int result = 0;
    for (int i = 0; i < 32; i++) {
        result <<= 1;
        if ((n & 1) == 1) result++;
        n >>= 1;
    }
    return result;
}
'''