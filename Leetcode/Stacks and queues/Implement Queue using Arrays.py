class ArrayQueue:
    def __init__(self):
        self.arr = [0] * 10
        self.start = -1
        self.end = -1
        self.curr_size = 0
        self.max_size = 10

    def push(self, x):
        if self.curr_size == self.max_size:
            print("queue is full")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.max_size
        self.arr[self.end] = x
        self.curr_size += 1

    def pop(self):
        if self.end == -1:
            print("queue is empty")
            exit(1)

        popped = self.arr[self.start]

        if self.curr_size == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.max_size
        self.curr_size -= 1
        return popped

    def peek(self):
        if self.start == -1:
            print("queue is empty")
            exit(1)
        return self.arr[self.start]

    def isEmpty(self):
        return self.curr_size == 0


if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(queue.pop(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayQueue":
            print("null", end=" ")
