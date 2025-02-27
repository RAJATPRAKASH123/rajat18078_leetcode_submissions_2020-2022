// https://leetcode.com/problems/online-stock-span

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] < price:
            self.stack.pop()
        res = self.count + 1 if not self.stack else self.count - self.stack[-1][1]
        self.stack.append((price, self.count))
        self.count += 1
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)