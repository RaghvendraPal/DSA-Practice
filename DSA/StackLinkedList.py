class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, size):
        self.head = None
        self.top = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.top += 1

    def pop(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.top -= 1
        del temp

    def isEmpty(self):
        if not self.head:
            return "Stack is Empty"
        else:
            return "Stack is not Empty"

    def size(self):
        return self.top

    def display(self):
        temp = self.head
        if not temp:
            return "Empty Stack"
        else:

            while(temp!=None):
                # print(temp)
                print(temp.data)
                temp = temp.next

stack = Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(30)

# print(stack.isEmpty())
# print(stack.size())
# print(stack.pop())
# print(stack.isEmpty())
# print(stack.size())
# print(stack.stacklist)
# print(stack.top)
stack.display()
print("*"*10)
print(stack.pop())
# print(stack.stacklist)
print(stack.top)
print(stack.pop())
# print(stack.stacklist)
print(stack.top)
print(stack.pop())
# print(stack.stacklist)
print(stack.top)
stack.display()