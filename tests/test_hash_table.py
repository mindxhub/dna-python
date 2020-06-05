import unittest

from src.hash_table import ChainHashTable


class TestChainHashTable(unittest.TestCase):
    def test_reference_init(self):
        ht = ChainHashTable(8)
        ht._ChainHashTable__bucket[0].val = 1
        self.assertFalse(ht._ChainHashTable__bucket[1].val == 1)

    def test_search(self):
        ht = ChainHashTable(8)
        ht.insert("3", "a")
        self.assertEqual(ht.search("3"), "a")
        ht.insert("3", "b")
        self.assertEqual(ht.search("3"), "b")
        ht.insert("11", "c")
        self.assertEqual(ht.search("11"), "c")
        # Key not exist
        self.assertEqual(ht.search("88"), None)

    def test_remove(self):
        ht = ChainHashTable(8)
        # Remove from empty hash table should return None
        self.assertEqual(ht.remove("8"), None)
        # Remove from empty should leave size == 0 rather than -1
        self.assertEqual(ht.size(), 0)

    def test_insert(self):
        ht = ChainHashTable(8)
        ht.insert("a", 1)
        ht.insert("b", 2)
        self.assertEqual(ht.size(), 2)
        ht.insert("b", 4)
        # Insert to existing key is overwriting so size should not increase
        self.assertEqual(ht.size(), 2)
        ht.insert("c", 5)
        self.assertEqual(ht.size(), 3)

    def test_normal_cases(self):
        ht = ChainHashTable(8)
        ht.insert("3", "a")
        self.assertEqual(ht.search("3"), "a")
        ht.insert("3", "b")
        self.assertEqual(ht.search("3"), "b")
        ht.insert("11", "c")
        self.assertEqual(ht.search("11"), "c")
        ht.insert("5", "d")
        ht.remove("11")
        ht.remove("82")
        self.assertEqual(ht.search("11"), None)
        self.assertEqual(ht.search("5"), "d")
        # Remove at end
        ht.insert("19", "e")
        ht.insert("27", "e")
        ht.remove("27")
        self.assertEqual(ht.search("27"), None)

    def test_table_doubling(self):
        INITIAL_SIZE = 4
        ht = ChainHashTable(INITIAL_SIZE)
        ht.insert("a", 1)
        self.assertEqual(ht.capacity(), INITIAL_SIZE)
        ht.insert("b", 2)
        self.assertEqual(ht.capacity(), 2 * INITIAL_SIZE)
        ht.insert("b", 3)
        self.assertEqual(ht.capacity(), 2 * INITIAL_SIZE)
        ht.insert("c", 4)
        self.assertEqual(ht.capacity(), 2 * INITIAL_SIZE)
        ht.insert("d", 5)
        self.assertEqual(ht.capacity(), 2 * 2 * INITIAL_SIZE)
        # Test if a key still maps to the same value
        self.assertEqual(ht.search("c"), 4)
        self.assertEqual(ht.search("b"), 3)


if __name__ == "__main__":
    unittest.main()
