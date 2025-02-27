// https://leetcode.com/problems/group-anagrams

from collections import defaultdict
class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        n = len(arr)
        letters_word = defaultdict(list)
        
        for i in range(len(arr)):
            letters_word[''.join(sorted(arr[i]))].append(arr[i])
        return letters_word.values()
        
        
        
'''
arr : array of strings
- group the anagrams together
Anagram : word/phrase formed by rearranging the letters of a different word 
        or phrase, typically using all the original letters exactly once.


'''