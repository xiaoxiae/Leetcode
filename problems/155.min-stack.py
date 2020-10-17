class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.min_values = []

    def push(self, x: int) -> None:
        self.values.append(x)

        if len(self.min_values) == 0 or self.min_values[-1] > x:
            self.min_values.append(x)
        else:
            self.min_values.append(self.min_values[-1])

    def pop(self) -> None:
        self.min_values.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
