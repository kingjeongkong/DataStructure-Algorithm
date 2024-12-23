class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print('Queue is empty')
            return
        print('Queue (front -> rear):', end=' ')
        i = self.front
        count = 0
        while count < self.size:
            print(self.queue[i], end=' ')
            i = (i + 1) % self.capacity
            count += 1
        print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        data = self.front.data
        self.front = self.front.next
        self.size -= 1

        if self.front is None:
            self.rear = None

        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue (front -> rear):", end=" ")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

