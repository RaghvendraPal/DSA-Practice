class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stacklist = [0]*self.size

    def push(self, data):
        if not self.isFull():
            self.top+=1
            self.stacklist[self.top] = data
        else:
            print("Stack is Full")

    def pop(self):
        if self.top >= 0:
            self.stacklist[self.top] = 0
            self.top-=1
        else:
            return "Stack is Empty"

    def isEmpty(self):
        if self.top == -1:
            return "Stack is Empty"
        else:
            return "Stack is not Empty"

    def size(self):
        return self.top+1

    def isFull(self):
        if self.top+1 == self.size:
            return True
        return False

    def display(self):
        point = self.top

        while(point >= 0):
            print(self.stacklist[point])
            point -= 1

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
print(stack.display())
print(stack.pop())
# print(stack.stacklist)
print(stack.top)
print(stack.pop())
print(stack.stacklist)
print(stack.top)
print(stack.pop())
print(stack.stacklist)
print(stack.top)