class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((val, min(val, curr_min)))

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Stack is Empty")
        return self.stack.pop()[0]

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Stack is Empty")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Stack is Empty")
        return self.stack[-1][1]
