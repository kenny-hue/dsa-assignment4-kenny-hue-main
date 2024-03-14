# Huffman Coding

You've been learning to use data structures to solve problems. In this assignment, you'll solve a practical problem: compressing and decompressing data.

You will create a program to compress and decompress data using Huffman coding. You will construct a data structure based on the characters in a file, then use that data structure to compress the data. You will then write the code to decompress the data using the Huffman coding from the encoding step.

For background information on constructing Huffman trees and encoding/decoding data, refer back to the lessons. There you will find information about the steps of the algorithm that you will be completing in this assignment.

## Starter Code

You are given the file `huffman.py`, which includes the partial implementation of a `Huffman` class. The `Huffman` class will contain code to build an encoding based on an input file, encode strings of characters into a compressed format, and decode compressed strings into plain text.

To begin, `huffman.py` contains the following code:

* The definition of a `HuffmanNode` nested class. This code has both a `next` pointer (to build the linked list in the algorithm) as well as `left` and `right` pointers (to build the tree in the algorithm).
* A constructor (`__init__`) for initializing instance variables needed by the `Huffman` class. This includes:
    * `self.data`: a string hold the data from the file used to construct the encoding
    * `self.freq_table`: a dictionary that will hold the frequencies of characters, e.g., `'e' --> 20`
    * `self.encodings`: a dictionary that will eventually map characters to their codes, e.g., `'e' --> '101'`
    * `self.head`: a reference to the head of the linked list used during tree construction
    * `self.root`: a reference to the root of the Huffman tree (once built)

It also contains implementations of the `build_list()`, `insert_sorted()`, `compute_encodings()`, and `build()` methods, which will be described below as they are needed. You should not modify any of these methods.

Finally, `huffman.py` contains stub implementations of four methods: `build_freq_table()`, `build_tree()`, `encode()`, and `decode()`. Your four main tasks are to implement these methods, as described below.

## Steps to Complete

The overall algorithm for Huffman encoding is as follows:

1. Build a frequency table of characters in the document (your Task 1)
2. Create a linked list of characters, sorted by their frequencies (done for you)
3. Create a Huffman tree by repeatedly removing nodes from the linked list, merging them, and inserting the result back into the linked list (your Task 2)
4. From the resulting tree, finding the encodings of each character (done for you)
5. Compressing a string using the encodings from the tree (your Task 3)
6. Decompressing a string using the tree (your Task 4)

As you can see, some parts of the algorithm are already implemented for you. Follow the steps below to implement the missing parts of the algorithm.

1. Task 1: implement the `build_freq_table()` method

    The `build_freq_method()` should take the string stored in `self.data` and use it to build a *frequency table* that maps individual characters to the number of times they appear in the document. To do so, the method should iterate over `self.data` and populate the `self.freq_table` dictionary, which was initialized as an empty dictionary in the constructor.

    Notes:

    * After the frequency table is built, the test cases related to the frequency table should pass.

2. Task 2: implement the `build_tree()` method.

    The `build_tree()` should create the Huffman tree from the sorted linked list. To do so, you should repeatedly remove the two *least frequent* nodes from the linked list, updating `self.head` as needed.

    You should then create a new `HuffmanNode` whose left and right children are the least-frequent and second-to-least frequent nodes, respectively. The frequency of the new node should be the sum of the frequencies of the two removed nodes. Finally, you should insert the "merged" node back into the list, maintaining sorted order.

    This method must set `self.root` to the `HuffmanNode` that serves as the root node of the Huffman tree before it exits.

    Notes:

    * You should write this method assuming that the linked list of characters and their frequencies has been correctly built, and that `self.head` is a reference to the first `HuffmanNode` in that list. All other nodes are connected using the `next` pointers.
    * However, it's possible that the list is empty (if there were no characters in the file) or the list has only one node (if there was only one character in the file). Your code should gracefully handle both of these cases.
    * When putting the new, merged node back into the linked list, you may want to make use of the `insert_sorted()` method, which we have provided for you.
    * The unit tests that evaluate this method can be performed independently (regardless of whether `build_freq_table()` is implemented).
    * It may help to remind yourself of the tree building algorithm from the lessons.

3. Task 3: implement the `encode()` method

    The `encode()` method should accept a string parameter `s` and should construct an encoded version of `s` using the Huffman tree, and then return it as a string of `'0'` and `'1'` characters.

    For example, if the encoding for `s` is `'111'` and the encoding for `'e'` is `'10'`, then `encode('see')` should return `'1111010'`.

    * You should write this method assuming that the `self.encodings` dictionary has been correctly initialized based on the Huffman tree. The `self.encodings` dictionary maps characters to their encoding strings, e.g., `self.encodings['e'] --> '10'`.
    * If the string `s` contains any characters that are not in the Huffman tree (and therefore not in the encodings), the method should return `None`.
    * The unit tests that evaluate this method can be performed independently (regardless of whether `build_freq_table()` or `build_tree()` is implemented).

4. Task 4: implement the `decode()` method

    The `decode()` method should accept a string parameter `code` that consists of `'0'` and `'1'` characters, decompress it using the Huffman tree to its decompressed, plain text version, and return it. For example, `decode('1111010') --> 'see'`.

    Notes:

    * You should write this method assuming that `self.root` references a correctly-built Huffman tree.
    * If `code` contains any characters other than `'0'` and `'1'`, the method should return `None`.
    * If `code` contains a sequence of `'0'`s and `'1'`s that don't correspond to a valid path in the Huffman tree, the method should return `None`.
    * You can write this method either iteratively or recursively.
    * The unit tests that evaluate this method can be performed independently (regardless of whether `build_freq_table()`, `build_tree()`, or `encode()` is implemented).

## Testing

In `test_huffman.py`, there are unit tests for each of the four methods described above. Each of the unit tests evaluates a method independently -- regardless of whether you have implemented the other methods in the assignment.

Additionally, there are tests that evaluate your code as a whole. These tests depend on each of the four methods being implemented correctly to work.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!
