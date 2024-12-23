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

class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        data = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def get_size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - (self.front - self.rear - 1)
        
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue (front -> rear):", end=" ")
        i = self.front
        if self.front <= self.rear:
            while i <= self.rear:
                print(self.queue[i], end=" ")
                i += 1
        else:
            while i < self.capacity:
                print(self.queue[i], end=" ")
                i += 1
            i = 0
            while i <= self.rear:
                print(self.queue[i], end=" ")
                i += 1
        print()


print("Testing Array-based Queue:")
array_queue = ArrayQueue(5)

array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)
array_queue.display()  # Queue: 1 2 3

print("Dequeued:", array_queue.dequeue())  # Should print 1
print("Peek:", array_queue.peek())         # Should print 2
print("Size:", array_queue.get_size())     # Should print 2
array_queue.display()

# Testing LinkedListQueue
print("\nTesting Linked List-based Queue:")
linked_queue = LinkedListQueue()

linked_queue.enqueue("A")
linked_queue.enqueue("B")
linked_queue.enqueue("C")
linked_queue.display()  # Queue: A B C

print("Dequeued:", linked_queue.dequeue())  # Should print A
print("Peek:", linked_queue.peek())         # Should print B
print("Size:", linked_queue.get_size())     # Should print 2
linked_queue.display()

# Testing CircularQueue
print("\nTesting Circular Queue:")
circular_queue = CircularQueue(5)

for i in range(1, 6):  # Filling the queue
    circular_queue.enqueue(i)
circular_queue.display()

print("Dequeued:", circular_queue.dequeue())  # Remove 1
print("Dequeued:", circular_queue.dequeue())  # Remove 2

circular_queue.enqueue(6)  # Add 6 in the freed space
circular_queue.enqueue(7)  # Add 7 in the freed space

print("After circular operations:")
circular_queue.display()

# Testing error handling
try:
    circular_queue.enqueue(8)  # Should raise OverflowError
except OverflowError as e:
    print("\nError:", e)  # Should print "Queue is full"