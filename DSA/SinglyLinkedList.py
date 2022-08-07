# A simple Python program for traversal of a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None

    def AddElement(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return "Value Added"

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        print("Head Data : ",self.head.data)
        self.head = node


    def insertAfter(self, data, position):
        count = 1
        temp = self.head
        while(count<position):
            temp = temp.next
            count += 1
        node = Node(data)
        node.next = temp.next
        temp.next = node
        if temp == self.tail:
            self.tail = node
        

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def deleteNode(self, data):
        temp = self.head
        prev_next = None
        while(temp.data != data):
            prev_next = temp
            temp = temp.next

        if prev_next:
            prev_next.next = temp.next
        else:
            self.head = temp.next
        temp.next = None

    def deleteNodeR(self, data, point, prev_point):
        if not point:
            return
        if point.data == data and prev_point == None:
            self.head = point.next
            point.next = None
            return

        elif point.data == data and prev_point != None:
            prev_point.next = point.next
            point.next = None
            return
        else:
            prev_point = point
            point = point.next
            self.deleteNodeR(data, point, prev_point)

    def linklistR(self):
        temp = self.head
        self.head = None
        prev = None
        while (temp != None):
            self.head = temp
            temp = temp.next
            self.head.next = prev
            if not prev:
                self.tail = self.head
            prev = self.head



# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
    llist = LinkedList()
    llist.AddElement(20)
    llist.AddElement(30)
    llist.AddElement(40)
    llist.AddElement(50)
    llist.AddElement(60)
    llist.AddElement(70)
    llist.AddElement(90)
    llist.insertAfter(80, 6)
    # llist.insertAfter(800, 1)
    llist.push(10)
    llist.append(100)

    # llist.deleteNode(10)

    # llist.deleteNode(60)

    # llist.deleteNode(100)
    # llist.deleteNodeR(50, llist.head, None)
    # llist.deleteNodeR(90, llist.head, None)
    
    # llist.deleteNodeR(20, llist.head, None)

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second; # Link first node with second
    # second.next = third; # Link second node with the third node

    llist.printList()
    print("*"*50)
    print("Reverse")
    print("*"*50)
    llist.linklistR()
    llist.printList()
    llist.push(10)
    llist.append(100)
    print("*"*50)
    print("After Push")
    print("*"*50)
    
    llist.printList()
