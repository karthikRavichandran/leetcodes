class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) < 2:
        #     return False
        has = {")":"(", "]":"[", "}":"{"}
        if s[0] in has:
            return False

        st = []

        for i in s:
            if i in has.values():
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                if st[-1] == has[i]:
                    st.pop()
                else:
                    return False
        if len(st) > 0:
            return False
        return True

if __name__ == '__main__':
    '''
    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    '''
    s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))