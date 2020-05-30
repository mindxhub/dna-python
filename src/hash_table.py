from __future__ import annotations
from typing import Union
import random


class Node:
    def __init__(self, key: str, val: Union[str, float], next: Node = None):
        self.key = key
        self.val = val
        self.next = next


class ChainHashTable:
    def __init__(self, n: int):
        self.__bucket = []
        for _ in range(n):
            self.__bucket.append(Node(None, None))

    def insert(self, key: str, val: Union[str, float]) -> None:
        """
        Insert a new key-value pair to a random hashed bucket.
        """
        node: Node = self.__bucket[self._hash(key)]
        while node.next:
            node = node.next
            if node.key == key:
                node.val = val
        node.next = Node(key, val)

    def remove(self, key: str):
        """
        Remove a key-value pair if the key is found, else do nothing.
        """
        node: Node = self.__bucket[self._hash(key)]
        while node and node.next:
            next_node = node.next
            if next_node.key == key:
                node.next = next_node.next
            node = next_node

    def search(self, key: str) -> Union[str, float, None]:
        """
        Find the value given a key in the HashTable. If the key is not found,
        return None.
        """
        node: Node = self.__bucket[self._hash(key)]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def _hash(self, key: str) -> int:
        """
        Decide which bucket a key should belong to.
        """
        key: int = hash(key)
        return key % len(self.__bucket)
