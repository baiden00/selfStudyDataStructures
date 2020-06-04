from nodes import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.next = self.top_item
      self.top_item = item
      self.size += 1
      print("Adding {} to the book stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.next
      self.size -= 1
      print("Removing " + item_to_remove.get_value())
      return item_to_remove.value
    print("No books here.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.value
    print("No books on the stack")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0

  def get_size(self):
    return self.size

# Defining an empty book stack with limit six
book_stack = Stack(6)

#Adding books until the stack is full
book_stack.push("book #1")
book_stack.push("book #2")
book_stack.push("book #3")
book_stack.push("book #4")
book_stack.push("book #5")
book_stack.push("book #6")

# No room for another book
book_stack.push("book #7")

#Checking the book on top of the stack
print("The first book to remove is " + book_stack.peek())

i = 0
while i < 6:
    book_stack.pop()
    i+=1

#Will print no books here
book_stack.pop()
