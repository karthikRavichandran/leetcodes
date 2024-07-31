

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        p = []
        k = tokens[::-1]
        while len(k) !=0:
            k1 = k[-1]
            # 
            # print(k)
            if k1 == '+':
                a = p.pop()
                b = p.pop()
                p.append(int(a)+int(b))
                k.pop()
            elif k1 == '/':
                a = p.pop()
                b = p.pop()
                p.append(int(b)/int(a))
                # print(p)
                k.pop()
            elif k1 == '-':
                a = p.pop()
                b = p.pop()
                p.append(int(b)-int(a))
                k.pop()
            elif k1 == '*':
                a = p.pop()
                b = p.pop()
                p.append(int(a)*int(b))
                k.pop()
            else:
                p.append(k.pop())

        return int(p[0])


if __name__ == '__main__':
    '''
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    

    Example 1:

    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    k = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    #output should be 22

    '''
    sol = Solution()
    k = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    #outshould be 22
    print(sol.evalRPN(k))



def my_try():
    k = ['2', '3', '5', '+', '/']
    k = ["4","13","5","/","+"]
    k = ["2","1","+","3","*"]
    p = []
    k = k[::-1]
    while len(k) !=0:
        k1 = k[-1]
        # 
        print(k)
        if k1 == '+':
            a = p.pop()
            b = p.pop()
            p.append(int(a)+int(b))
            k.pop()
        elif k1 == '/':
            a = p.pop()
            b = p.pop()
            p.append(int(b)/int(a))
            print(p)
            k.pop()
        elif k1 == '-':
            a = p.pop()
            b = p.pop()
            p.append(int(a)-int(b))
            k.pop()
        elif k1 == '*':
            a = p.pop()
            b = p.pop()
            p.append(int(a)*int(b))
            k.pop()
        else:
            p.append(k.pop())
            # print(k)
            # print(p)

    print(p)