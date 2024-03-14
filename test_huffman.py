import unittest
from huffman import Huffman

class TestString(unittest.TestCase):
    def setUp(self):
        self.tree = Huffman('examples/example1.txt')

    # Return a string representation of the list of Huffman nodes.
    def list_to_string(self):
        trav = self.tree.head
        s = ''
        while trav is not None:
            if trav.next is not None:
                s += '(' + str(trav.val) + ', ' + str(trav.freq) + ') --> '
            else:
                s += '(' + str(trav.val) + ', ' + str(trav.freq) + ')'
            trav = trav.next
        return s

    def test_build_freq_table_file(self):
        self.tree.build_freq_table()
        assert self.tree.freq_table['e'] == 40
        assert self.tree.freq_table['t'] == 27
        assert self.tree.freq_table['s'] == 26
        assert self.tree.freq_table['a'] == 25
        assert self.tree.freq_table['i'] == 23
        assert self.tree.freq_table['o'] == 11

    def test_prepend_to_list(self):
        self.tree.prepend_to_list('a', 10)
        s = self.list_to_string()
        assert s == '(a, 10)'

    def test_prepend_to_list_longer(self):
        self.tree.prepend_to_list('a', 30)
        self.tree.prepend_to_list('b', 20)
        self.tree.prepend_to_list('c', 10)
        s = self.list_to_string()
        assert s == '(c, 10) --> (b, 20) --> (a, 30)'

    def test_build_tree(self):
        n1 = Huffman.HuffmanNode('c', 30)
        n2 = Huffman.HuffmanNode('b', 25, next=n1)
        n3 = Huffman.HuffmanNode('a', 10, next=n2)
        self.tree.head = n3

        self.tree.build_tree()
        root = self.tree.root
        assert root.freq == 65
        left = root.left
        assert left.val == 'c'
        assert left.freq == 30
        right = root.right
        assert right.freq == 35
        right_left = right.left
        assert right_left.val == 'a'
        assert right_left.freq == 10
        right_right = right.right
        assert right_right.val == 'b'
        assert right_right.freq == 25

    def test_build_tree_one_node(self):
        n1 = Huffman.HuffmanNode('c', 30)
        self.tree.head = n1

        self.tree.build_tree()
        root = self.tree.root
        assert root.val == 'c'
        assert root.freq == 30

    def test_encode(self):
        self.tree.encodings['e'] = '0'
        self.tree.encodings['t'] = '11'
        self.tree.encodings['s'] = '10'
        code = self.tree.encode('set')
        assert code == '10011'

    def test_decode(self):
        node_e = Huffman.HuffmanNode('e', 30)
        node_t = Huffman.HuffmanNode('t', 25)
        node_s = Huffman.HuffmanNode('s', 10)
        merged = Huffman.HuffmanNode('-', 35, left=node_s, right=node_t)
        self.tree.root = Huffman.HuffmanNode('-', 65, left=node_e, right=merged)

        plain = self.tree.decode('10011')
        assert plain == 'set'

    def test_all(self):
        self.tree.build()
        assert self.tree.encode('state') == '111001100010'
        assert self.tree.decode('01011000111') == 'oats'

    def test_encode_decode(self):
        self.tree.build()
        assert self.tree.decode(self.tree.encode('seats')) == 'seats'

    def test_lorem_ipsum(self):
        self.tree = Huffman('examples/example2.txt')
        self.tree.build()
        assert self.tree.decode(self.tree.encode('Lorem ipsum')) == 'Lorem ipsum'
