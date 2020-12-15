class Node:
    def __init__(self, value):
        self.value = value
        self.before = None
        self.after = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def valueAt(self, index):
        if (index < 0 or index >= self.length):
            return None
        current = self.head
        count = 0
        while (current):
            if (count == index):
                return current.value
            count += 1
            current = current.after
        return None

    def pushFront(self, value):
        node = Node(value)
        if (self.length == 0):
            self.head = node
            self.tail = node
        else:
            self.head.before = node
            node.after = self.head
            self.head = node
        self.length += 1

    def popFront(self):
        if (self.length == 0):
            return None
        else:
            oldHead = self.head
            if (self.length == 1):
                self.head = None
                self.head = None
                return oldHead.value
            else:
                nextHead = oldHead.after
                nextHead.before = None
                self.head = nextHead
                return oldHead.value
        self.length -= 1

    def pushBack(self, value):
        node = Node(value)
        if (self.length == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.after = node
            node.before = self.tail
            self.tail = node
        self.length += 1

    def popBack(self):
        if (self.length == 0):
            return None
        else:
            oldTail = self.tail
            if (self.length == 1):
                self.head = None
                self.tail = None
                return oldTail.value
            else:
                nextTail = oldTail.before
                nextTail.after = None
                self.tail = nextTail
                return oldTail.value
        self.length -= 1

    def front(self):
        if (self.length == 0):
            return None
        return self.head.value

    def back(self):
        if (self.length == 0):
            return None
        return self.tail.value

    def insert(self, value, index):
        if (index < 0 or index > self.length):
            return
        elif (index == 0):
            self.pushFront(value)
        elif (index == self.length):
            self.pushBack(value)
        else:
            node = Node(value)
            count = 0
            current = self.head
            before = None
            after = None
            while (current):
                if (count == index):
                    before = current.before
                    after = current
                    break
                current = current.after
                count += 1
            node.before = before
            before.after = node
            node.after = after
            after.before = node
        self.length += 1

    def removeAt(self, index):
        if (index < 0 or index > self.length):
            return
        elif (index == 0):
            self.popFront()
        elif (index == self.length - 1):
            self.popBack()
        else:
            count = 0
            current = self.head
            before = None
            after = None
            while (current):
                if (count == index):
                    before = current.before
                    after = current.after
                    before.after = after
                    after.before = before
                    break;
                current = current.after
                count += 1
        self.length -= 1
        
if __name__ == '__main__':
    lst = DoublyLinkedList()
    lst.pushFront(Node(2))
    lst.pushFront(Node(0))
    lst.pushBack(Node(5))
    lst.insert(Node(1), 1)
    lst.insert(Node(3), 3)
    lst.insert(Node(4), 4)
    lst.removeAt(3)