// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.mn=float("inf")


    def push(self, x: int) -> None:
        if(x<=self.mn):
            self.minStack.append(self.mn)
            self.mn=x
        self.stack.append(x)
    def pop(self) -> None:
        if(self.stack[-1]==self.mn):
            self.stack.pop()
            self.mn=self.minStack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        # if(stack):
        return self.stack[-1]
        # return 0

    def getMin(self) -> int:
        return self.mn

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()