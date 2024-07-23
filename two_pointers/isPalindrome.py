class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        # s = s.replace(" ","").replace(",", "").replace(":", "")
        print(s)
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True

if __name__ == '__main__':

    '''
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
    '''
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindrome(s))
        