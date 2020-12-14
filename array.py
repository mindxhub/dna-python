class Array:
    def __init__(self, size):
        self.capacity = 1
        self.items = [None]*capacity
        self.count = self.count(items)

    def size(self):
        return count

    def capacity(self):
        return capacity

    def isEmpty(self):
        return count == 0

    def itemAt(self, index):
        return items[index]

    def append(self, item):
        if (count == 0):
            items[0] = item
        else:
            if (count == capacity):
                capacity *= 2
            items[count] = item
            self.count += 1
        
    def insert(self, item, index):
        if (index < 0 or index > count):
            return
        else:
            if (count == capacity):
                capacity *= 2
            items.insert(index, item)
            count += 1
    
    def pop(self):
        if (count == 0):
            return None
        else:
            if (self.count == capacity * 0.2 + 1):
                capacity /= 2
            count -= 1
            return pop(items)
    
    def removeAt(self, index):
        if (index < 0 or index >= self.count):
            return
        else:
            if (self.count == capacity * 0.2 + 1):
                capacity /= 2
            items.remove(index)
            count -= 1

    def count(self, lst):
        count = 0
        while count < len(lst):
            count += 1
        return count
