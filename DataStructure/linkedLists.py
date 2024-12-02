class Node:
  def __init__(self, data):
    self.data = data
    self.next = None    # For singly linked list
    #self.prev = None   # For doubly linked list

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)

    if not self.head:
      self.head = new_node
      return
    
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def insert_after_node(self, prev_node_data, data):
    current = self.head
    while current and current.data != prev_node_data:
      current = current.next

    if not current:
      print(f"Node with data {prev_node_data} not found.")
      return
    
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node