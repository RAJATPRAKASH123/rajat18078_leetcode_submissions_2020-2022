// https://leetcode.com/problems/permutation-sequence

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        k -= 1
        k %= fact
        perm = [str(i) for i in range(1, n+1)]
        while k > 0:
            to_swap = -1
            for i in range(n-1, 0, -1):
                if perm[i-1] < perm[i]:
                    to_swap = i - 1
                    break
            for i in range(n-1, -1, -1):
                if perm[i] > perm[to_swap]:
                    perm[i], perm[to_swap] = perm[to_swap], perm[i]
                    perm[to_swap+1:] = perm[to_swap+1:][::-1]
                    break
            k -= 1
        return "".join(perm)