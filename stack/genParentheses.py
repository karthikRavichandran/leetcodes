from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        ret = []

        def backtrack(openN, closeN):

            if openN == closeN == n:
                ret.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)    
        # print(ret)
        return ret
    
if __name__ == '__main__':
    '''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:

    Input: n = 1
    Output: ["()"]
    '''
    n=3
    sol = Solution()
    print(sol.generateParenthesis(n))

        