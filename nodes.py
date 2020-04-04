class Node:

  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def set_next(self, next):
    self.set_next = next

  def get_next(self):
    return self.next

  def get_value(self):
    return self.value


yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_next(dot) # yacko -> dot
dot.set_nextwacko) # dot -> wacko

#getting values from link nodes
dots_data = yacko.get_next().get_value()
wackos_data = dot.get_next().get_value()

print(dots_data)
print(wackos_data)
