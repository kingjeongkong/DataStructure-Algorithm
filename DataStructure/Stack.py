class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, data):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("stack is empty")
            return
        print("Stack (top -> bottom):", end=" ")
        
        for item in reversed(self.stack):
            print(item, end=" ")
        print()