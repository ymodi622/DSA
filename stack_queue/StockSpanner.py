class StockSpanner:
    def __init__(self):
        self.stack = []  # stack of [index, price]
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        # Remove all elements from stack with price <= current
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        if not self.stack:
            span = self.index + 1
        else:
            span = self.index - self.stack[-1][0]

        self.stack.append([self.index, price])
        return span


obj = StockSpanner()
price = [7, 2, 1, 3, 3, 1, 8]
res = []
for i in price:
    res.append(obj.next(i))
print(res)
