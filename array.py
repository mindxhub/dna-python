import unittest

class Array:
    def __init__(self):
        self.items = []
        self.allocated = 0
        self.count = self.count(self.items)

    def size(self):
        return self.count

    def capacity(self):
        return self.allocated

    def isEmpty(self):
        return self.count == 0

    def itemAt(self, index):
        if (self.count == 0 or index < 0 or index >= self.count):
            return None
        return self.items[index]

    def append(self, item):
        self.items += [item]
        self.updateAlloc()
        self.count += 1

    def insert(self, item, index):
        if (index < 0 or index > self.count):
            return
        else:
            if (index == self.count):
                self.append(item)
            else:
                self.updateAlloc()
                self.count += 1
                self.items = self.items[:index] + [item] + self.items[index:]

    def pop(self):
        if (self.count == 0):
            return None
        else:
            lastItem = self.items[self.count - 1]
            self.count -= 1
            self.updateAlloc()
            self.items = self.items[:-1]
            return lastItem

    def removeAt(self, index):
        if (index < 0 or index >= self.count):
            return
        else:
            self.count -= 1
            self.updateAlloc()
            self.items = self.items[:index] + self.items[index + 1:]

    def updateAlloc(self):
        if (self.allocated == 0):
            self.allocated = 1
        elif (self.count == self.allocated):
            self.allocated *= 2
        elif (self.count < self.allocated*0.2):
            self.allocated /= 2
        else:
            return

    def count(self, lst):
        count = 0
        while count < len(lst):
            count += 1
        return count

    def __str__(self):
        return '[' + ', '.join([str(e) for e in self.items]) + ']'

class TestArray(unittest.TestCase):
    
    arr = Array()
    
    def test_size(self):
        self.assertEqual(self.arr.size(), 0)

    def test_capacity(self):
        self.assertEqual(self.arr.capacity(), 0)

    def test_isEmpty(self):
        self.assertEqual(self.arr.isEmpty(), True)

    def test_itemAt(self):
        self.assertEqual(self.arr.itemAt(1), None)

    def test_append(self):
        arr = Array()
        arr.append(0)
        self.assertEqual(arr.size(), 1)
        self.assertEqual(arr.capacity(), 1)
        self.assertEqual(arr.itemAt(0), 0)

    def test_insert(self):
        arr = Array()
        arr.append(0)
        arr.insert(2, 1)
        self.assertEqual(arr.size(), 2)
        self.assertEqual(arr.capacity(), 2)
        self.assertEqual(arr.itemAt(1), 2)
        arr.insert(1, 1)
        self.assertEqual(arr.size(), 3)
        self.assertEqual(arr.capacity(), 4)
        self.assertEqual(arr.itemAt(1), 1)

    def test_pop(self):
        arr = Array()
        arr.append(0)
        arr.append(1)
        self.assertEqual(arr.pop(), 1)
        self.assertEqual(arr.size(), 1)
        self.assertEqual(arr.capacity(), 2)
        self.assertEqual(arr.itemAt(1), None)
        
    def removeAt(self):
        arr = Array()
        arr.append(0)
        arr.append(1)
        arr.append(2)
        self.removeAt(1)
        self.assertEqual(arr.size(), 2)
        self.assertEqual(arr.capacity(), 4)
        self.assertEqual(arr.itemAt(1), 2)
        
if __name__ == '__main__':
    unittest.main()