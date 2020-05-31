from __future__ import annotations
from typing import Union
import random


class Node:
    def __init__(self, key: str, val: Union[str, float], next: Node = None):
        self.key = key
        self.val = val
        self.next = next


class ChainHashTable:
    def __init__(self, capacity: int = 8):
        self.__capacity = capacity
        self.__size = 0
        self.__bucket = []
        for _ in range(capacity):
            self.__bucket.append(Node(None, None))

    def capacity(self) -> int:
        return self.__capacity

    def size(self) -> int:
        return self.__size

    def insert(self, key: str, val: Union[str, float]):
        """
        Insert a new key-value pair to a random hashed bucket.
        """
        node: Node = self.__bucket[self.__hash(key)]
        while node.next:
            node = node.next
            if node.key == key:
                node.val = val
                return
        node.next = Node(key, val)
        self.__size += 1
        if self.size() >= self.capacity() / 2:
            self.__table_doubling()

    def remove(self, key: str):
        """
        Remove a key-value pair if the key is found, else do nothing.
        """
        node: Node = self.__bucket[self.__hash(key)]
        while node and node.next:
            next_node = node.next
            if next_node.key == key:
                node.next = next_node.next
                if self.size() > 0:
                    self.__size -= 1
            node = next_node

    def search(self, key: str) -> Union[str, float, None]:
        """
        Find the value given a key in the HashTable. If the key is not found,
        return None.
        """
        node: Node = self.__bucket[self.__hash(key)]
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

    def __table_doubling(self) -> None:
        new_ht = ChainHashTable(self.capacity() * 2)
        for n in self.__bucket:
            node = n.next
            while node:
                if node.key:
                    new_ht.insert(key=node.key, val=node.val)
                node = node.next

        self.__bucket = new_ht.__bucket
        self.__size = new_ht.__size
        self.__cap = new_ht.__cap
