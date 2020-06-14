from collections import deque


#Stack implemetnation using deque
class Stack:

  def __init__(self, limit=100):
    self.items = deque()
    self.size = 0
    self.limit = limit

  def push(self, val):
    self.items.append(val)
    self.size+=1

  def max_len(self):
    return self.items.limit

  def pop(self):
    self.items.pop()
    self.size-=1

  def peek(self):
    return self.items[-1]

  def print_elements(self):
    for elem in self.items:
      print(elem)

  def sizeOf(self):
    return self.size

  def has_space(self):
    return self.size < self.limit


stack = Stack()

for i in range(10):
  stack.push(i)

stack.push(10)

for i in range(5):
  stack.pop()
