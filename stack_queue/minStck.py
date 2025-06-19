class MinStack:

    def __init__(self):
        self.arr = []
        self.t = -1
        self.gm = None

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append([val, val])
            self.gm = val
        else:
            if val < self.gm:
                self.arr.append([val, val])
                self.gm = val
            else:
                self.arr.append([val, self.gm])
        self.t += 1

    def pop(self) -> None:
        if not self.arr:
            return
        self.arr.pop()
        self.t -= 1
        if self.arr:
            self.gm = self.arr[-1][1]
        else:
            self.gm = None

    def top(self) -> int:
        if not self.arr:
            return -1
        val = self.arr[self.t][0]
        return val

    def getMin(self) -> int:
        if not self.arr:
            return -1
        val = self.arr[self.t][1]
        return val


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(2)
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
