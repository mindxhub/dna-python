class Node:
    def __init__(self, value):
        self.value = value
        self.before = None
        self.after = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return length

    def isEmpty(self):
        return length == 0

    def valueAt(self, index):
        if (index < 0 or index >= length):
            return None
        current = head
        count = 0
        while (current):
            if (count == index):
                return current.value
            count += 1
            current = current.after
        return None

    def pushFront(self, value):
        node = Node(value)
        if (length == 0):
            self.head = node
            self.tail = node
        else:
            self.head.before = node
            node.after = self.head
            self.head = node
        length += 1

    def popFront(self):
        if (length == 0):
            return None
        else:
            oldHead = self.head
            if (length == 1):
                self.head = None
                self.head = None
                return oldHead.value
            else:
                nextHead = oldHead.after
                nextHead.before = None
                self.head = nextHead
                return oldHead.value
        length -= 1

    def pushBack(self, value):
        node = Node(value)
        if (length == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.after = node
            node.before = self.tail
            self.tail = node
        length += 1

    def popBack(self):
        if (length == 0):
            return None
        else:
            oldTail = self.tail
            if (length == 1):
                self.head = None
                self.tail = None
                return oldTail.value
            else:
                nextTail = oldTail.before
                nextTail.after = None
                self.tail = nextTail
                return oldTail.value
        length -= 1

    def front(self):
        if (length == 0):
            return None
        return self.head.value

    def back(self):
        if (length == 0):
            return None
        return self.tail.value

    def insert(self, value, index):
        if (index < 0 or index > self.length):
            return
        elif (index == 0):
            self.pushFront(value)
        elif (index == length):
            self.pushBack(value)
        else:
            node = Node(value)
            count = 0
            current = head
            before = None
            after = None
            while (current):
                if (count == index):
                    before = current
                    after = current.after
                    break
                count += 1
            node.before = before
            before.after = node
            node.after = after
            after.before = node
        length += 1

    def removeAt(self, index):
        if (index < 0 or index > self.length):
            return
        elif (index == 0):
            self.popFront()
        elif (index == length):
            self.popBack()
        else:
            count = 0
            current = head
            before = None
            after = None
            while (current):
                if (count == index):
                    before = current
                    after = current.after
                    before.after = after
                    after.before = before
                    break;
                count += 1
        length -= 1
        
