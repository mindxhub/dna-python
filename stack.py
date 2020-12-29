class StackNode:
    def __init__(self, value):
        self.value = value
        self.prev = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class StackLinkedList:
    def __init__(self):
        self.head
        self.tail
        self.size = 0
    
    def add(self, item):
        newNode = StackNode(item)
        if (self.tail != None):
            self.tail.next = newNode
        self.tail = newNode
        if (self.head == None):
            self.head = self.tail
        self.size += 1
    
    def pop(self):
        if (self.head == None):
            return
        oldTail = self.tail
        self.tail = self.tail.prev
        if (self.tail == None):
            self.head = None
        self.size -= 1
        return oldTail

    def front(self):
        if (self.head == None):
            return
        return self.head.value
    
    def isEmpty(self):
        return self.head == None
    
class StackArray:
    def __init__(self):
        self.items = []
        self.allocated = 0
        self.count = self.count(self.items)
    
    def add(self, item):
        self.items += [item]
        self.updateAlloc()
        self.count += 1
    
    def pop(self):
        if (self.count == 0):
            return None
        else:
            lastItem = self.items[self.count - 1]
            self.count -= 1
            self.updateAlloc()
            self.items = self.items[:-1]
            return lastItem

    def front(self):
        return self.queue[0]
    
    def isEmpty(self):
        return self.count == 0
    
    def updateAlloc(self):
        if (self.allocated == 0):
            self.allocated = 1
        elif (self.count == self.allocated):
            self.allocated *= 2
        elif (self.count < self.allocated*0.2):
            self.allocated /= 2
        else:
            return