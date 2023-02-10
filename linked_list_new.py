class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
    # Function to insert a new node at the beginning
    def insertfirst(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertlast(self, new_data):
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode 
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
  
    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
  
  
# Driver program to test above functions
llist = LinkedList()
llist.insertlast(20)
llist.insertlast(4)
llist.insertlast(15)
llist.insertlast(85)
  
print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()