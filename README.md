# FileZipper_project

The File Zipper Project is a tool that utilizes the Huffman Coding algorithm to compress text files, making them smaller for storage or transmission. This project is based on a lossless compression method, which ensures that the original file can be perfectly restored after decompression. Huffman Coding is particularly effective because it assigns shorter codes to more frequent characters and longer codes to less frequent characters, optimizing data storage.

**Project Overview**

The goal of the project is to:
1. Read a text file.
2. Compress the text file using Huffman coding.
3. Save the compressed data in a separate file.
4. Decompress the file back to its original form.
5. Visualize the Huffman tree, which is the basis for compression.

**Understanding Huffman Coding**

Huffman Coding is an optimal prefix coding algorithm, widely used in data compression. The key idea behind Huffman coding is to represent more frequent characters with shorter binary codes and less frequent characters with longer binary codes. This ensures efficient data representation.

The process of Huffman coding typically involves:

1. Calculating the frequency of each character in the input text.
2. Building a Huffman tree, which organizes characters based on their frequency.
3. Generating Huffman codes by traversing the tree.
4. Compressing the input text using the generated codes.
5. Saving the compressed data in a binary format.
6. Decompressing the binary data to recover the original text.

**Key Components of the Project**

1. **Priority Queue (Min-Heap)**: The Huffman tree is built using a priority queue (also known as a min-heap). This data structure ensures that nodes with the lowest frequencies are always processed first, which is crucial for constructing the tree optimally.

2. **Huffman Tree**: The tree structure represents the frequency of characters and their corresponding Huffman codes. The leaf nodes of the tree represent characters, while internal nodes represent merged frequencies.

3. **Bitstream**: The compressed data is stored as a series of bits, with each bit representing a character or part of a character’s Huffman code. This bitstream is then written to a file.

4. **Bit Manipulation**: During compression, text is converted into a bitstream, and during decompression, the bitstream is decoded using the Huffman tree to restore the original content.

**How the Solution Works**

**Step 1**: **Frequency Calculation**

The first step in compression is to calculate how often each character appears in the input text. This frequency table helps in constructing the Huffman tree, where characters with higher frequencies will have shorter codes.

**Step 2**: **Building the Huffman Tree**

The Huffman tree is built using a priority queue. Each node in the queue represents a character and its frequency. The algorithm repeatedly combines the two nodes with the lowest frequencies into a new internal node, which is pushed back into the queue. This process continues until only one node remains, which is the root of the Huffman tree.

**Step 3**: **Generating Huffman Codes**

Once the Huffman tree is built, we assign binary codes to each character by traversing the tree. Moving to the left child of the tree is represented by a '0', and moving to the right child is represented by a '1'. This traversal generates a unique binary code for each character.

**Step 4**: **Compressing the Data**

With the Huffman codes available, the input text is encoded by replacing each character with its corresponding binary code. The resulting bitstream represents the compressed form of the original text.

**Step 5**: **Writing the Compressed Data**

The compressed bitstream is then written to a file, but before doing so, it is converted from a series of bits to a byte array. This ensures that the data can be efficiently stored and transmitted.

**Step 6**: **Decompression**
To decompress the file:

The compressed file (which contains the byte array) is read.
The byte array is converted back into a bitstream.
The bitstream is decoded using the Huffman tree, restoring the original text.

Step 7: Visualization of the Huffman Tree
The Huffman tree can be visualized using a graphical representation. This helps in understanding how characters are encoded and how the tree structure optimizes the compression process. The visualization typically displays the characters along with their frequencies, showing the tree structure that was used for encoding.

**How the Project Works in Practice**
**Compression Process**:

The input text is read from a file.
The frequency of characters is calculated.
A Huffman tree is built using these frequencies.
The tree generates binary codes for each character.
The input text is encoded with these binary codes and saved as a compressed file.

**Decompression Process**:

The compressed file is read, and the bitstream is extracted.
The bitstream is decoded using the Huffman tree to retrieve the original text.
The decoded text is saved to a new file.

**Visualization**:

The Huffman tree is visualized as a diagram that illustrates the structure of the tree, showing how characters are assigned codes based on their frequencies. This helps to understand how the compression process works and how Huffman coding achieves efficient data storage.


**Conclusion**
The File Zipper Project using Huffman Coding demonstrates an efficient algorithm for compressing text files. By leveraging priority queues (min-heaps) and binary trees, this project not only reduces the size of text files but also ensures that the original content can be perfectly restored. Additionally, visualizing the Huffman tree provides an intuitive understanding of how the algorithm works.

