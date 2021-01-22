from doubly_linked_list import DoublyLinkedList


class Hashmap:
    def __init__(self):
        hashmap = [None] * 10
        capacity = 10

    def hashFunction(self, value):
        return value % 5

    def checkExist(self, value):
        hashValue = self.hashFunction(value)
        if self.hashmap[hashValue] == None:
            return False
        lst = self.hashmap[hashValue]
        cur = lst.head
        while cur != None:
            if cur == value:
                return True
            cur = cur.next
        return False

    def insertToHashmap(self, value):
        hashValue = self.hashFunction(value)
        if hashValue in self.hashmap:
            self.hashmap[hashValue].pushBack(value)
        else:
            newLinkList = DoublyLinkedList()
            newLinkList.pushBack(value)
            self.hashmap[hashValue] = newLinkList

    def removeFromHashmap(self, value):
        hashValue = self.hashFunction(value)
        if hashValue in self.hashmap:
            self.hashmap[hashValue].remove(value)
            if self.hashmap[hashValue].length == 0:
                self.hashmap[hashValue] = None


class Hashmap:
    def __init__(self):
        hashmap = [None] * 10
        capacity = 10
        del_flag = '0xalskdjghaksjdbgalweiglakjsebglkajse'

    def hashFunction(self, value):
        return value % 5

    def secondHashFucntion(self, value, step):
        return value + step

    def checkExist(self, value):
        hashValue = self.hashFunction(value)
        cur = self.hashmap[hashValue]
        if cur == None:
            return False
        step = 0

        while step < self.capacity and cur != None:
            hashValue = self.secondHashFucntion(hashValue, step)
            cur = self.hashmap[hashValue]
            if cur == value:
                return True
            elif not cur:
                return False
            step += 1
        return False

    def insertToHashmap(self, value):

        hashValue = self.hashFunction(value)
        if not self.hashmap[hashValue]:
            self.hashmap[hashValue] = value
        else:
            step = 0
            while step < self.capacity:
                hashValue = self.secondHashFucntion(hashValue, step)
                if not self.hashmap[hashValue]:
                    self.hashmap[hashValue] = value
                    break
                else:
                    step += 1

    def removeFromHashmap(self, value):

        hashValue = self.hashFunction(value)
        if not self.hashmap[hashValue]:
            return
        else:
            if self.hashmap[hashValue] == value:
                self.hashmap[hashValue] = self.del_flag
                return
            
            step = 0
            while step < self.capacity:
                hashValue = self.secondHashFucntion(hashValue, step)
                if not self.hashmap[hashValue]:
                    return
                elif self.hashmap[hashValue] == value:
                    self.hashmap[hashValue] = self.del_flag
                    break;
                else:
                    step += 1
