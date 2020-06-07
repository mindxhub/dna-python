from __future__ import annotations
from typing import Union


class AVLTree:
    class Node:
        def __init__(
            self,
            val: float,
            left: AVLTree.Node = None,
            right: AVLTree.Node = None,
        ):
            self.val = val
            self.left = left
            self.right = right
            self.height: int = 1

        def __repr__(self):
            left = 'na'
            right = 'na'
            if self.left is not None:
                left = self.left.val
            if self.right is not None:
                right = self.right.val
            return (
                f"  {self.val}  \n"
                f" /  \\  \n"
                f"{left}   {right}")

    def __init__(self, val: float):
        self.head = self.Node(val)

    def insert(self, val: float):
        self.head = self.__insert(self.head, val)

    def __insert(self, root: AVLTree.Node, val: float):
        """
        Insert a new value into the tree while maintain the AVL structure.
        Insertion should takes O(logN) in time complexity.
        Needs recursion to update height of each node.
        """
        if root is None:
            return self.Node(val)
        if val < root.val:
            root.left = self.__insert(root.left, val)
        elif val > root.val:
            root.right = self.__insert(root.right, val)
        else:
            raise ValueError(f"Value {val} already exists!")

        root.height = (
            1 + 
            max(
                self.__get_height(root.left),
                self.__get_height(root.right)))

        balance = self.__get_balance(root)
        # Left left case
        if balance < -1 and self.__get_balance(root.right) == -1:
            root = self.__rotate_left(root)

        # Right right case
        if balance > 1 and self.__get_balance(root.left) == 1:
            root = self.__rotate_right(root)

        # Left right case
        if balance > 1 and self.__get_balance(root.left) == -1:
            root.left = self.__rotate_left(root.left)
            root = self.__rotate_right(root)

        # Right left case
        if balance < -1 and self.__get_balance(root.right) == 1:
            root.right = self.__rotate_right(root.right)
            root = self.__rotate_left(root)
        return root

    def __get_height(self, root: AVLTree.Node) -> int:
        if root is None:
            return 0
        return root.height

    def __get_balance(self, root: AVLTree.Node) -> int:
        if root is None:
            return 0
        return self.__get_height(root.left) - self.__get_height(root.right)

    def __rotate_left(self, root: AVLTree.Node):
        new_root = root.right
        left_old = new_root.left

        new_root.left = root
        root.right = left_old

        root.height = (
            1 +
            max(
                self.__get_height(root.left),
                self.__get_height(root.right)))

        new_root.height = (
            1 +
            max(
                self.__get_height(new_root.left),
                self.__get_height(new_root.right)))
        return new_root

    def __rotate_right(self, root: AVLTree.Node):
        new_root = root.left
        right_old = new_root.right

        new_root.right = root
        root.left = right_old

        root.height = (
            1 +
            max(
                self.__get_height(root.left),
                self.__get_height(root.right)))

        new_root.height = (
            1 +
            max(
                self.__get_height(new_root.left),
                self.__get_height(new_root.right)))
        return new_root

    def remove(self, val: float):
        """
        Remove a value from the tree while maintain the AVL structure.
        Removal should takes O(logN) in time complexity.
        """
        pass
