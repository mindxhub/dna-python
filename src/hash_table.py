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
        self.__bucket = [Node(None, None)] * n

    def insert(self, key: str, val: Union[str, float]) -> bool:
        node: Node = self.__bucket[self._hash(key)]
        while node.next:
            node = node.next
            if node.key == key:
                node.val = val
                return True
        node.next = Node(key, val)
        return True

    def remove(self, key: str) -> bool:
        node: Node = self.__bucket[self._hash(key)]
        while node and node.next:
            next_node = node.next
            if next_node.key == key:
                node.next = next_node.next
                return True
            node = next_node
        return False

    def search(self, key: str) -> float:
        node: Node = self.__bucket[self._hash(key)]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def _hash(self, key: str) -> int:
        key: int = self._convert_key_to_num(key)
        return key % len(self.__bucket)

    def _convert_key_to_num(self, key: str) -> int:
        # TODO: Update this function, for now it assumes all key can be
        # convert to number
        try:
            return int(key)
        except:
            return round(random.random() * 100)
