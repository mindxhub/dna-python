class Array:
    def __init__(self):
        self.allocated = 0
        self.items = []
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


if __name__ == '__main__':
    arr = Array()
    arr.append(0)
    arr.append(4)
    arr.insert(3, 1)
    arr.insert(2, 1)
    arr.insert(1, 1)