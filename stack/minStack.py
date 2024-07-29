class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:

        if len(self.st) ==0:
            min_val = val
        elif self.st[-1][1] > val:
            min_val = val
        else:
            min_val = self.st[-1][1]

        val_to_push = [val, min_val]
        self.st.append(val_to_push)
        

    def pop(self) -> None:
        self.st = self.st[:-1]
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
        

if __name__ == "__main__":
    '''

    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    '''

    min_st = MinStack()
    print(min_st.push(-2))
    print(min_st.push(0))
    print(min_st.push(-3))
    print( min_st.getMin())
    print(min_st.pop())
    print(min_st.top())
    print(min_st.getMin())


