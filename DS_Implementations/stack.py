# Implement a stack using a list

class stack():

    def __init__(self):
        self.stack = []
    
    def pop(self):
        self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peak(self):
        return None if len(self.stack) == 0 else self.stack[len(self.stack)-1]

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def printStack(self):
        print(self.stack)


testStack = stack()
testStack.push(100)
print(testStack.peak())
print(testStack.isEmpty())
testStack.printStack()