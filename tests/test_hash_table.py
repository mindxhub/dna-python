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

    def test_all(self):
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


if __name__ == "__main__":
    unittest.main()
