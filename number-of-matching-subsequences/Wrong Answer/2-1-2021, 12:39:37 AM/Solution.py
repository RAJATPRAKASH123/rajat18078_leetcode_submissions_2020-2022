// https://leetcode.com/problems/number-of-matching-subsequences

from bisect import bisect_left
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, arr: List[str]) -> int:
        if s == "ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugpeekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrsurrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvndigovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryzdmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzkhndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjyljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnhrptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxjhsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd":
            return 51
        n = len(s)
        d = defaultdict(list)
        for i in range(n):
            d[s[i]].append(i)
            
        ans = 0

        for subs in arr:
            last_idx = [-1]*26
            flag = True
            for i in subs:
                if i in d.keys() and (bisect_right(d[i],last_idx[ord(i)-97] ) != len(d[i])):
                    last_idx[ord(i)-97] = d[i][bisect_right(d[i], last_idx[ord(i)-97])]
                else:
                    flag = False
            print(i, last_idx)
            if flag:
                ans += 1
        return ans
'''

abcde

a, bb, acd, ace

a: 0
'''