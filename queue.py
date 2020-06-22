from nodes import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.value) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.next = item_to_add
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")

  def dequeue(self):
    if self.size > 0:
      item_to_remove = self.head
      if self.size == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next
      self.size -= 1
      return item_to_remove.value
    else:
      print("The queue is empty!")

  def peek(self):
    if self.size > 0:
      return self.head.value
    else:
      print("Nothing here")

  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()

  def is_empty(self):
    return self.size == 0


shopping_line = Queue(10)

shopping_line.enqueue("2 cartons of milk")
shopping_line.enqueue("one tv set")
shopping_line.enqueue("game console")
shopping_line.enqueue("acrylic paint")


print("------------\nThe first customer will be " + shopping_line.peek())
print("------------\nNow serving...\n------------")

shopping_line.dequeue()
shopping_line.dequeue()
shopping_line.dequeue()
shopping_line.dequeue()
shopping_line.dequeue()
