#implementation of a node data structure


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __str__(self):
        return self.value




#Instantiating nodes as the days of the week
monday = Node("Is the beginning of the week")
tuesday = Node("Is the second day of the week")
wednesday = Node("Is the middle of the week")
thursday = Node("Is the fourth day of the week")
friday = Node("Is the last day of the week")
saturday = Node("Is the weekend")

print(monday)
