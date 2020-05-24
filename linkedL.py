#Implementation of a linkedlist using nodes

from nodes import Node, monday,tuesday,wednesday,thursday,friday, saturday

class LinkedList:

    '''initializing a linkedlist by creating a new node instance
     and making it the head node of the LList'''

    def __init__(self, value=None):
        self.head = Node(value)

    #method to insert at the beginning
    def insert_at_start(self,value):
        #newNode = Node(value)
        '''The above line will create a new node and insert
        it but in this case I have already created the nodes'''

        value.next = self.head
        self.head = value

    #traversing through the linkedlist and printing all the elements
    def print_list(self):
        val = self.head
        while val:
            print(val.value)
            val = val.next

    #traversing a LinkedList to search for a value
    def search_value(self, toSearch):
        node = self.head
        while node is not None:
            if node.value == toSearch.value:
                return True
            else:
                node = node.next
        return False

    #deleting an item from the linkedlist
    def delete_from_linked_list(self, to_delete):
        node = self.head

        #if the head is to be deleted
        if node.value == to_delete.value:
            self.head = node.next

        #if not the head
        else:
          while node is not None:
            next_node = node.next
            if next_node.value == to_delete.value:
              node.next = next_node.next
              break
            else:
              node = next_node

    #inserting inbetween the linkedlist
    def insert_in_between(self, after_this_value, to_insert):

        #case where the location is not in the linkedlist

        if not self.search_value(after_this_value):
            print("The location does not exist in the linkedlist")
            return

        to_insert.next = after_this_value.next
        after_this_value.next = to_insert

    #to insert at the end
    def insert_at_end(self,new_data):

        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_data



#creating a new linkedlist
days_of_week = LinkedList()
days = [monday,tuesday,wednesday,thursday,friday]

#inserting all days of the week at the beginning of the node
#in this case I want to start from monday
for day in days[::-1]:
    days_of_week.insert_at_start(day)

#this will print the whole linkedlist starting from the last inserted node
days_of_week.print_list()
print("")
print("")

#Returns "false since charles is not in the linkedlist"
charles = Node("Charles Baiden")
print(days_of_week.search_value(charles))
print("")
print("")

#delete wednesday and print the resulting LinkedList
days_of_week.delete_from_linked_list(wednesday)
days_of_week.print_list()
print("")
print("")

#insert wednesday back
days_of_week.insert_in_between(tuesday, wednesday)
days_of_week.print_list()
print("")
print("")

#insert saturday at the end
days_of_week.insert_at_end(saturday)
days_of_week.print_list()
