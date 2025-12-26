class arraystack:
    def __init__(self, size=10):
        self.capacity = size
        self.arr = [0] * size
        self.topindex = -1

    def push(self, x):
        if self.topindex >= self.capacity - 1:
            print("stack overflow")
        else:
            self.topindex += 1
            self.arr[self.topindex] = x

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        value = self.arr[self.topindex]
        self.topindex -= 1
        return value

    def top(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        return self.arr[self.topindex]

    def isEmpty(self):
        return self.topindex == -1


if __name__ == "__main__":
    stack = arraystack()

    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "ArrayStack":
            print("null", end=" ")
        elif commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            if stack.isEmpty():
                print("True", end=" ")
            else:
                print("False", end=" ")
