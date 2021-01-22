import unittest

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
                self.length -= 1
                return oldHead.value
            else:
                nextHead = oldHead.after
                nextHead.before = None
                self.head = nextHead        
                self.length -= 1
                return oldHead.value

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
                self.length -= 1
                return oldTail.value
            else:
                nextTail = oldTail.before
                nextTail.after = None
                self.tail = nextTail
                self.length -= 1
                return oldTail.value
        
    def remove(self, value):
        if (self.length == 0):
            return
        else:
            cur = self.head
            while cur != None:
                if cur.value == value:
                    cur.before.next = cur.after
                    cur.after.before = cur.before
                    self.length -= 1
                cur = cur.next

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
        
class TestLinkedList(unittest.TestCase):
    
    def test_size(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.size(), 0)

    def test_isEmpty(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.isEmpty(), True)
        lst.pushFront(Node(1))
        self.assertEqual(lst.isEmpty(), False)
    
    def test_valueAt(self):
        lst = DoublyLinkedList()
        lst.pushFront(Node(0))
        self.assertEqual(lst.valueAt(0).value, 0)
        self.assertEqual(lst.valueAt(1), None)
    
    def test_pushPopFront(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.valueAt(1), None)
        lst.pushFront(Node(1))
        lst.pushFront(Node(0))
        self.assertEqual(lst.valueAt(1).value, 1)
        self.assertEqual(lst.popFront().value, 0)
        self.assertEqual(lst.valueAt(0).value, 1)
    
    def test_pushPopBack(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.valueAt(1), None)
        lst.pushBack(Node(0))
        lst.pushBack(Node(1))
        self.assertEqual(lst.valueAt(1).value, 1)
        self.assertEqual(lst.popBack().value, 1)
        self.assertEqual(lst.valueAt(0).value, 0)
    
    def test_front(self):
        lst = DoublyLinkedList()
        lst.pushFront(Node(0))
        self.assertEqual(lst.front().value, 0)
        
    def test_back(self):
        lst = DoublyLinkedList()
        lst.pushBack(Node(0))
        lst.pushBack(Node(1))
        self.assertEqual(lst.back().value, 1)
    
    def test_insert(self):
        lst = DoublyLinkedList()
        lst.insert(Node(1), 0)
        lst.insert(Node(0), 0)
        lst.insert(Node(2), 2)
        self.assertEqual(lst.front().value, 0)
        self.assertEqual(lst.valueAt(1).value, 1)
        self.assertEqual(lst.back().value, 2)
        
    def test_removeAt(self):
        lst = DoublyLinkedList()
        lst.insert(Node(1), 0)
        lst.insert(Node(0), 0)
        lst.insert(Node(2), 2)
        lst.removeAt(1)
        self.assertEqual(lst.front().value, 0)
        self.assertEqual(lst.valueAt(1).value, 2)
        
if __name__ == '__main__':
    unittest.main()