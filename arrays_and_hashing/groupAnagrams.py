from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alldict = defaultdict(list)

        for i in strs:
            k = list(i)
            k.sort()
            k="".join(k)
            alldict[k].append(i)
        ret = []
        for all_ in alldict:
            ret.append(alldict[all_])
        return ret


if __name__ == "__main__":

    '''
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Example 2:

    Input: strs = [""]
    Output: [[""]] 
    Example 3:

    Input: strs = ["a"]
    Output: [["a"]]
    '''
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()

    print(sol.groupAnagrams(strs))
