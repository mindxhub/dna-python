from doubly_linked_list import DoublyLinkedList


class Hashmap:
    def __init__(self):
        hashmap = [None] * 10

    def hashFunction(self, value):
        return value % 5

    def checkExist(self, value, hashValue):
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
