#Implementation of a linkedlist using nodes

from nodes import Node, monday,tuesday,wednesday,thursday,friday, saturday

class LinkedList:

    '''initializing a linkedlist by creating a new node instance
     and making it the head node of the LList'''

    def __init__(self, value=None):
        self.head = Node(value)

    #method to insert at the beginning
    def insertAtStart(self,value):
        #newNode = Node(value)
        '''The above line will create a new node and insert
        it but in this case I have already created the nodes'''

        value.next = self.head
        self.head = value

    #traversing through the linkedlist and printing all the elements
    def printList(self):
        val = self.head
        while val:
            print(val.value)
            val = val.next

    #traversing a LinkedList to search for a value
    def searchValue(self, toSearch):
        node = self.head
        while node is not None:
            if node.value == toSearch.value:
                return True
            else:
                node = node.next
        return False

    #deleting an item from the linkedlist
    def deleteFromLinkedList(self, toDelete):
        node = self.head

        #if the head is to be deleted
        if node.value == toDelete.value:
            self.head = node.next

        #if not the head
        else:
          while node is not None:
            nextNode = node.next
            if nextNode.value == toDelete.value:
              node.next = nextNode.next
              break
            else:
              node = nextNode

    #inserting inbetween the linkedlist
    def insertInBetween(self, afterThisValue, toInsert):

        #case where the location is not in the linkedlist

        if not self.searchValue(afterThisValue):
            print("The location does not exist in the linkedlist")
            return

        toInsert.next = afterThisValue.next
        afterThisValue.next = toInsert

    #to insert at the end
    def insertAtEnd(self, newdata):

        if self.head is None:
            self.head = newdata
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newdata



#creating a new linkedlist
daysOfWeek = LinkedList()
days = [monday,tuesday,wednesday,thursday,friday]

#inserting all days of the week at the beginning of the node
#in this case I want to start from monday
for day in days[::-1]:
    daysOfWeek.insertAtStart(day)

#this will print the whole linkedlist starting from the last inserted node
daysOfWeek.printList()
print("")
print("")

#Returns "false since charles is not in the linkedlist"
charles = Node("Charles Baiden")
print(daysOfWeek.searchValue(charles))
print("")
print("")

#delete wednesday and print the resulting LinkedList
daysOfWeek.deleteFromLinkedList(wednesday)
daysOfWeek.printList()
print("")
print("")

#insert wednesday back
daysOfWeek.insertInBetween(tuesday, wednesday)
daysOfWeek.printList()
print("")
print("")

#insert saturday at the end
daysOfWeek.insertAtEnd(saturday)
daysOfWeek.printList()
