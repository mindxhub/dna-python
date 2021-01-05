from doubly_linked_list import DoublyLinkedList


class Hashmap:
    def __init__(self):
        hashmap = {}
        buckets = 0

    def hashFunction(self, value):
        return value % 5

    def checkExist(self, value, hashValue):
        if self.buckets == 0:
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
        if self.hashmap.has_key(hashValue):
            self.hashmap[hashValue].pushBack(value)
        else:
            newLinkList = DoublyLinkedList()
            newLinkList.pushBack(value)
            self.hashmap[hashValue] = newLinkList

    def removeFromHashmap(self, value):
        hashValue = self.hashFunction(value)
        if self.hashmap.has_key(hashValue):
            self.hashmap[hashValue].remove(value)
            if self.hashmap[hashValue].length == 0:
                self.hashmap.pop(hashValue, None)
