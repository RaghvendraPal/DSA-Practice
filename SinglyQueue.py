class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            temp = self.head
            self.head = temp.next
            if not self.head:
                self.tail = None
            del temp

    def display(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def isEmpty(self):
        if self.head == self.tail == None:
            return True
        return None



queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()

print("*"*50)
queue.dequeue()
queue.display()
print("*"*50)
queue.dequeue()
queue.display()
print("*"*50)
queue.dequeue()
queue.display()
print("*"*50)
queue.dequeue()
queue.display()
print("*"*50)
queue.dequeue()
queue.display()


