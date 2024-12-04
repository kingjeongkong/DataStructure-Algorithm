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

  def delete_node(self, data):
    temp = self.head

    if temp and temp.data == data:
      self.head = temp.next
      temp = None
      return

    prev = None
    while temp and temp.data != data:
      prev = temp
      temp = temp.next

    if not temp:
      print(f"Node with data {data} not found.")
      return
    
    prev.next = temp.next
    temp = None

  def delete_at_position(self, position):
    temp = self.head

    if not temp:
      return
    
    if position == 0:
      self.head = temp.next
      return
    
    for i in range(position - 1):
      temp = temp.next
      if not temp:
        break

    if not temp or temp.next:
      print("Position is out of bounds.")
      return
    
    temp.next = temp.next.next
    temp.next = None

  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=' -> ')
      current = current.next
    print('None')

  def searching(self, data):
    current = self.head
    while current:
      if current.data == data:
        return True
      current = current.next
    return False
      
    