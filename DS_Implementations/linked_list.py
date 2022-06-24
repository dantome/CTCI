class linkedlist():
    def __init__(self, head):
        self.head = head

    def appendToTail(self, node):

        curr = self.head
        if curr == None:
            self.head = node
            return

        while curr.next != None:
            curr = curr.next

        # Now curr is pointing to the last node
        curr.next = node
        
    def removeNode(self, node):
        curr = self.head
        if curr == None:
            return "Error, linkedlist is empty"
        
        # Base Case
        if curr == node:
            self.head = curr.next
            return

        # Otherwise
        while curr.next:
            if curr.next == node:
                curr.next == curr.next.next

    def isEmpty(self):
        return True if self.head == None else False

class node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next






        