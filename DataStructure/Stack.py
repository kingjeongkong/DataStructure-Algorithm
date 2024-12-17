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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self.size_count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_data = self.top.data
        self.top = self.top.next
        self.size_count -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def size(self):
        return self.size_count

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return

        current = self.top
        print("Stack (top -> bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

print("Testing Array-based Stack:")
array_stack = ArrayStack(5)

array_stack.push(1)
array_stack.push(2)
array_stack.push(3)
array_stack.display() 

print("Popped:", array_stack.pop()) 
print("Peek:", array_stack.peek())  
print("Size:", array_stack.size())  
array_stack.display()


print("\nTesting Linked List-based Stack:")
linked_stack = LinkedListStack()

linked_stack.push("A")
linked_stack.push("B")
linked_stack.push("C")
linked_stack.display() 

print("Popped:", linked_stack.pop()) 
print("Peek:", linked_stack.peek())   
print("Size:", linked_stack.size())   
linked_stack.display()


try:
    while True:
        linked_stack.pop()
except IndexError as e:
    print("\nError:", e)  