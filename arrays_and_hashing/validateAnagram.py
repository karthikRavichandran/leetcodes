from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_ct = defaultdict(lambda: 0)
        t_ct = defaultdict(lambda: 0)

        for st in s:
            s_ct[st]+=1
        for st in t:
            t_ct[st]+=1
        if t_ct == s_ct:
            return True
        else:
            return False

if __name__=="__main__":
    '''
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false
 
    '''

    sol = Solution()
    s = "anagram"
    t = "nagaram"

    print(sol.isAnagram(s, t))
    s = "rat"
    t = "car"
    print(sol.isAnagram(s, t))