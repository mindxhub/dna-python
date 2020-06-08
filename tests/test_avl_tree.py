import unittest

from src.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):
    def test_normal_cases(self):
        avl = AVLTree(10)
        self.assertEqual(avl.head.val, 10)
        avl.insert(3)
        self.assertEqual(avl.head.left.val, 3)
        self.assertEqual(avl.head.height, 2)
        avl.insert(11)
        self.assertEqual(avl.head.right.val, 11)
        avl.insert(5)
        self.assertEqual(avl.head.left.right.val, 5)
        avl.insert(13)
        self.assertEqual(avl.head.right.right.val, 13)

    def test_insert_rotate_left_left(self):
        avl = AVLTree(2)
        avl.insert(1)
        avl.insert(4)
        avl.insert(5)
        self.assertEqual(avl.head.height, 3)
        avl.insert(6)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.right.val, 5)
        self.assertEqual(avl.head.right.left.val, 4)
        self.assertEqual(avl.head.right.right.val, 6)

    def test_insert_rotate_right_right(self):
        avl = AVLTree(10)
        avl.insert(12)
        avl.insert(8)
        avl.insert(4)
        self.assertEqual(avl.head.height, 3)
        avl.insert(2)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.left.val, 4)
        self.assertEqual(avl.head.left.left.val, 2)
        self.assertEqual(avl.head.left.right.val, 8)

    def test_insert_rotate_left_right(self):
        # Case 1
        avl = AVLTree(10)
        avl.insert(11)
        avl.insert(8)
        avl.insert(4)
        self.assertEqual(avl.head.height, 3)
        avl.insert(5)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.left.val, 5)
        self.assertEqual(avl.head.left.left.val, 4)
        self.assertEqual(avl.head.left.right.val, 8)

        # Case 2
        avl = AVLTree(2)
        avl.insert(1)
        avl.insert(6)
        avl.insert(4)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.right.val, 6)
        self.assertEqual(avl.head.right.left.val, 4)
        avl.insert(5)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.right.val, 5)
        self.assertEqual(avl.head.right.left.val, 4)
        self.assertEqual(avl.head.right.right.val, 6)

    def test_insert_rotate_right_left(self):
        avl = AVLTree(10)
        avl.insert(5)
        avl.insert(14)
        avl.insert(19)
        avl.insert(16)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.right.val, 16)
        self.assertEqual(avl.head.right.left.val, 14)
        self.assertEqual(avl.head.right.right.val, 19)

    def test_insert_rotate_root(self):
        avl = AVLTree(10)
        avl.insert(11)
        avl.insert(8)
        avl.insert(4)
        avl.insert(9)
        self.assertEqual(avl.head.height, 3)
        avl.insert(2)
        self.assertEqual(avl.head.height, 3)
        self.assertEqual(avl.head.val, 8)
        self.assertEqual(avl.head.left.val, 4)
        self.assertEqual(avl.head.left.left.val, 2)
        self.assertEqual(avl.head.right.val, 10)
        self.assertEqual(avl.head.right.left.val, 9)
        self.assertEqual(avl.head.right.right.val, 11)

    def test_remove(self):
        avl = AVLTree(10)
        # Remove value without changing structure
        avl.insert(5)
        avl.insert(13)
        avl.remove(5)
        self.assertEqual(avl.head.left, None)
        # Remove value that does not exist
        avl.remove(8)
        avl.insert(5)
        self.assertEqual(avl.head.left.val, 5)
        self.assertEqual(avl.head.right.val, 13)
        # Remove value that causes left right rotation on the other branch
        avl.insert(7)
        avl.remove(13)
        self.assertEqual(avl.head.val, 7)
        self.assertEqual(avl.head.left.val, 5)
        self.assertEqual(avl.head.right.val, 10)
        # Remove value that causes right rotation on other branch
        avl.insert(2)
        avl.insert(6)
        avl.insert(12)
        avl.insert(1)
        avl.remove(12)
        self.assertEqual(avl.head.val, 5)
        self.assertEqual(avl.head.left.val, 2)
        self.assertEqual(avl.head.left.left.val, 1)
        self.assertEqual(avl.head.left.right, None)
        self.assertEqual(avl.head.right.val, 7)
        self.assertEqual(avl.head.right.left.val, 6)
        self.assertEqual(avl.head.right.right.val, 10)
        # Remove value that causes right rotation on current branch
        avl.insert(9)
        avl.remove(6)
        self.assertEqual(avl.head.right.val, 9)
        self.assertEqual(avl.head.right.left.val, 7)
        self.assertEqual(avl.head.right.right.val, 10)
        self.assertEqual(avl.head.height, 3)

    def test_bst(self):
        avl = AVLTree(2)
        self.assertEqual(avl.head.val, 2)
        avl.insert(4)
        self.assertEqual(avl.head.right.val, 4)
        avl.insert(1)
        self.assertEqual(avl.head.left.val, 1)
        avl.insert(5)
        self.assertEqual(avl.head.height, 3)
        # Test remove leaf
        avl.remove(5)
        self.assertEqual(avl.head.height, 2)
        self.assertEqual(avl.head.right.right, None)
        # Test remove intermediate node
        avl.insert(5)
        avl.remove(4)
        self.assertEqual(avl.head.right.val, 5)
        # Test remove intermediate node with both left and right
        avl.insert(7)
        avl.insert(10)
        avl.remove(5)
        self.assertEqual(avl.head.right.val, 7)
        self.assertEqual(avl.head.right.right.val, 10)
        # Test remove intermediate node with long descendants
        avl.insert(0)
        avl.insert(4)
        avl.insert(8)
        avl.insert(12)
        avl.remove(7)
        self.assertEqual(avl.head.height, 4)
        self.assertEqual(avl.head.right.val, 8)
        self.assertEqual(avl.head.right.right.left, None)


if __name__ == "__main__":
    unittest.main()
