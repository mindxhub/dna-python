class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class QueueLinkedList:
    def __init__(self):
        self.head;
        self.tail;
        self.size = 0
    
    def enqueue(self, item):
        newNode = QueueNode(item)
        if (self.tail != None):
            self.tail.next = newNode
        self.tail = newNode
        if (self.head == None):
            self.head = self.tail
        self.size += 1
    
    def dequeue(self):
        if (self.head == None):
            return
        oldHead = self.head
        self.head = self.head.next
        if (self.head == None):
            self.tail = None
        self.size -= 1
        return oldHead

    def peek(self):
        if (self.head == None):
            return
        return self.head.value
    
    def isEmpty(self):
        return self.head == None
    
class QueueArray:
    def __init__(self):
        self.items = []
        self.allocated = 0
        self.count = self.count(self.items)
    
    def enqueue(self, item):
        self.items += [item]
        self.updateAlloc()
        self.count += 1
    
    def dequeue(self):
        if (self.count == 0):
            return None
        else:
            firstItem = self.items[0]
            self.count -= 1
            self.updateAlloc()
            self.items = self.items[1:]
            return firstItem

    def peek(self):
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