from __future__ import annotations
from typing import Union


class ChainHashTable:
    class Node:
        def __init__(self, key: str, val: Union[str, float], next: ChainHashTable.Node = None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, capacity: int = 8):
        self.__initiate(capacity)

    def __initiate(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__bucket = []
        for _ in range(capacity):
            self.__bucket.append(self.Node(None, None))

    def capacity(self) -> int:
        return self.__capacity

    def size(self) -> int:
        return self.__size

    def insert(self, key: str, val: Union[str, float]):
        """
        Insert a new key-value pair to a random hashed bucket.
        """
        node: self.Node = self.__bucket[self.__hash(key)]
        while node.next:
            node = node.next
            if node.key == key:
                node.val = val
                return
        node.next = self.Node(key, val)
        self.__size += 1
        if self.size() >= self.capacity() / 2:
            self.__table_doubling()

    def remove(self, key: str):
        """
        Remove a key-value pair if the key is found, else do nothing.
        """
        node: self.Node = self.__bucket[self.__hash(key)]
        while node and node.next:
            next_node = node.next
            if next_node.key == key:
                node.next = next_node.next
                self.__size -= 1
            node = next_node

    def search(self, key: str) -> Union[str, float, None]:
        """
        Find the value given a key in the HashTable. If the key is not found,
        return None.
        """
        node: self.Node = self.__bucket[self.__hash(key)]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def __hash(self, key: str) -> int:
        """
        Decide which bucket a key should belong to.
        """
        key: int = hash(key)
        return key % len(self.__bucket)

    def __table_doubling(self):
        # Copy current bucket
        temp_bucket = self.__bucket[:]
        self.__initiate(self.capacity() * 2)

        # Migrate old nodes
        len_temp_bucket = len(temp_bucket)
        for i in range(len_temp_bucket):
            n = temp_bucket[i]
            node = n.next
            while node:
                if node.key:
                    self.insert(key=node.key, val=node.val)
                node = node.next
