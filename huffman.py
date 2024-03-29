from collections import deque

class Huffman:
    class HuffmanNode:
        def __init__(self, val, freq, next=None, left=None, right=None):
            self.val = val
            self.freq = freq
            self.next = next
            self.left = left
            self.right = right

    def __init__(self, file):
        with open(file, 'r') as f:
            self.data = f.read()
        self.freq_table = {}
        self.head = None
        self.root = None
        self.encodings = {}

    def build_freq_table(self):
        # Task 1: Implementing build_freq_table() method
        self.freq_table = {}
        for char in self.data:
            if char in self.freq_table:
                self.freq_table[char] += 1
            else:
                self.freq_table[char] = 1

    def build_tree(self):
        if not self.head:  # Handle empty linked list
            return

        if self.head.next is None:  # Handle linked list with only one node
            self.root = self.head
            return

        # Create a list of Huffman nodes from the linked list
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        while len(nodes) > 1:
            # Sort nodes by frequency
            nodes.sort(key=lambda x: x.freq)

            # Take the two nodes with the lowest frequency
            left = nodes.pop(0)
            right = nodes.pop(0)

            # Create a new node with combined frequency
            merged_freq = left.freq + right.freq
            merged_node = self.HuffmanNode(None, merged_freq, left=left, right=right)

            # Append the new node to the list
            nodes.append(merged_node)

        # The last remaining node is the root of the Huffman tree
        self.root = nodes[0]



    def encode(self, s):
        # Task 3: Implementing encode() method
        if not self.encodings:
            return None
        
        encoded_string = ''
        for char in s:
            if char not in self.encodings:
                return None
            encoded_string += self.encodings[char]
        return encoded_string

    def decode(self, code):
        if not self.encodings or not self.root:
            return None

        decoded_string = ''
        current_node = self.root
        for bit in code:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if current_node.val is not None:
                decoded_string += current_node.val
                current_node = self.root  # Reset to the root for the next character

        return decoded_string






    #
    # Note: you should NOT alter any of the following methods.
    # Doing so may hinder our ability to test your code.
    #

    # Create a new HuffmanNode and prepend it to the head of the linked list.
    def prepend_to_list(self, char, freq):
        new_node = Huffman.HuffmanNode(char, freq, next=self.head)
        self.head = new_node

    # Build the linked list of Huffman nodes from the frequency table.
    def build_list(self):
        sorted_freqs = sorted(self.freq_table.items(), key=lambda x:x[1], reverse=True)
        for char, freq in sorted_freqs:
            self.prepend_to_list(char, freq)

    # Insert a node into a sorted linked list referenced by self.head.
    # Helper method for build_tree().
    def insert_sorted(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        prev = None
        trav = self.head

        # find the place in the list where the new node belongs
        while trav is not None and trav.freq < new_node.freq:
            prev = trav
            trav = trav.next

        if trav is None:
            # new node goes last in the sorted list
            prev.next = new_node
        else:
            # new_node goes between prev and trav
            prev.next = new_node
            new_node.next = trav

    # Recursive helper method to set the encodings
    # from the Huffman tree.
    def __compute_encodings(self, node, code):
        if node.left is None and node.right is None:
            # at a leaf node -- set the encoding
            self.encodings[node.val] = code

        if node.left is not None:
            self.__compute_encodings(node.left, code + '0')
        if node.right is not None:
            self.__compute_encodings(node.right, code + '1')

    # Set the encodings from the Huffman tree.
    def compute_encodings(self):
        self.__compute_encodings(self.root, '')

    # Build a Huffman tree.
    def build(self):
        self.build_freq_table()
        self.build_list()
        self.build_tree()
        self.compute_encodings()
