// https://leetcode.com/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.size += 1
        for i in range(self.size-1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue:
            self.size -= 1
            return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue:
            return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
-> 3 2 1 ->

3 2 1
'''

