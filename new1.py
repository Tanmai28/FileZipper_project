import heapq # A useful tool for managing the nodes in a priority queue
from collections import Counter # Helps us count how many times each character appears
import os
from graphviz import Digraph  # For creating and visualizing the Huffman Tree

class HuffmanCoding:
    def __init__(self):
        # Initialize dictionaries to store the codes and their reverse mapping
        self.codes = {}
        self.reverse_mapping = {}

    # Node class to represent each character and its frequency in the Huffman tree
    class Node:
        def __init__(self, char, freq):
            self.char = char  # Character
            self.freq = freq  # Frequency of the character
            self.left = None  # Left child in the tree
            self.right = None  # Right child in the tree

        # Comparing nodes based on frequency
        def __lt__(self, other):
            return self.freq < other.freq

    # This function creates the Huffman tree using a priority queue (min-heap)
    def build_huffman_tree(self, frequencies):
        # Create a heap (priority queue) from the frequency table
        heap = [self.Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(heap)  # Make sure it's a valid heap

        # Combine the two nodes with the lowest frequencies until only one node is left (the root)
        while len(heap) > 1:
            left = heapq.heappop(heap)  # Pop the smallest
            right = heapq.heappop(heap)  # Pop the next smallest
            merged = self.Node(None, left.freq + right.freq)  # Create a new internal node
            merged.left = left  # Set the left child
            merged.right = right  # Set the right child
            heapq.heappush(heap, merged)  # Push the merged node back into the heap

        return heap[0]  # Return the root node (final merged node)

    # This function recursively generates the Huffman codes for each character
    def generate_codes(self, node, current_code=""):
        # Base case: if the node is None, do nothing
        if node is None:
            return
        # If we reach a leaf node (a node with a character), store its code
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        # Recursively go left and right, adding '0' and '1' to the current code respectively
        self.generate_codes(node.left, current_code + "0")
        self.generate_codes(node.right, current_code + "1")

    # This function compresses the input file using Huffman coding
    def compress(self, input_file, output_file):
        # Open the input file and read the text
        with open(input_file, 'r') as file:
            text = file.read()

        if not text:
            raise ValueError("File is empty.")  # Error handling for empty file

        # Create a frequency table for the text
        frequencies = Counter(text)
        # Build the Huffman tree based on frequencies
        root = self.build_huffman_tree(frequencies)
        # Generate the Huffman codes for each character in the text
        self.generate_codes(root)

        # Encode the text using the generated Huffman codes
        encoded_text = ''.join(self.codes[char] for char in text)
        # Convert the encoded text into bytes
        byte_data = self.convert_to_bytes(encoded_text)

        # Write the compressed data to the output file
        with open(output_file, 'wb') as file:
            file.write(byte_data)

        print(f"File compressed successfully. Compressed file saved as {output_file}.")
        return root  # Return the root node for later use in decompression

    # This function decompresses the given compressed file
    def decompress(self, input_file, output_file, root):
        # Read the compressed byte data from the input file
        with open(input_file, 'rb') as file:
            byte_data = file.read()

        # Convert the byte data back into a bit string
        bit_string = self.convert_to_bit_string(byte_data)
        # Decode the bit string into the original text using the Huffman tree
        decoded_text = self.decode_text(bit_string, root)

        # Write the decompressed text to the output file
        with open(output_file, 'w') as file:
            file.write(decoded_text)

        print(f"File decompressed successfully. Decompressed file saved as {output_file}.")

    # Converts a bit string to bytes for saving compressed data
    def convert_to_bytes(self, bit_string):
        byte_array = bytearray()
        for i in range(0, len(bit_string), 8):
            byte_array.append(int(bit_string[i:i + 8], 2))
        return bytes(byte_array)

    # Converts byte data back to a bit string
    def convert_to_bit_string(self, byte_data):
        bit_string = ''.join(format(byte, '08b') for byte in byte_data)
        return bit_string.rstrip('0')  # Remove padding zeros from the end

    # This function decodes the bit string back into the original text using the Huffman tree
    def decode_text(self, bit_string, root):
        decoded_text = []
        current_node = root
        for bit in bit_string:
            # Traverse the tree based on the current bit (0 = left, 1 = right)
            current_node = current_node.left if bit == '0' else current_node.right
            # If we reach a leaf node, add the character to the decoded text and reset to root
            if current_node.char is not None:
                decoded_text.append(current_node.char)
                current_node = root
        return ''.join(decoded_text)

    # This function visualizes the Huffman tree and saves it as a PNG image
    def visualize_tree(self, root, filename="huffman_tree"):
        if root is None:
            print("Error: Cannot visualize an empty tree.")
            return

        graph = Digraph(format="png")  # Create a Graphviz Digraph for visualization
        self._add_nodes(graph, root)  # Add the nodes to the graph
        graph.render(filename, view=True)  # Render and view the tree image
        print(f"Huffman tree visualized and saved as {filename}.png")

    # This function recursively adds nodes to the graph for visualization
    def _add_nodes(self, graph, node, parent_name=None):
        if node is None:
            return

        # Create a label for each node (internal nodes and leaf nodes)
        node_name = f"{node.char or 'Internal'}\n{node.freq}"
        graph.node(node_name)  # Add the node to the graph

        if parent_name:
            graph.edge(parent_name, node_name)  # Add an edge from the parent to this node

        # Recursively add left and right children
        self._add_nodes(graph, node.left, node_name)
        self._add_nodes(graph, node.right, node_name)

if __name__ == "__main__":
    # Create an instance of the HuffmanCoding class
    huffman = HuffmanCoding()

    # Specify the input and output file paths
    input_file = "C:\\Users\\LAKSHMI TANMAI\\Downloads\\inputFile.txt"
    compressed_file = 'compressed_file.huffman'

    try:
        # Compress the input file and get the root of the Huffman tree
        root = huffman.compress(input_file, compressed_file)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    # Visualize the Huffman tree
    huffman.visualize_tree(root)

    # Specify the output path for the decompressed file
    decompressed_file = 'decompressed_file.txt'
    # Decompress the file and save the result
    huffman.decompress(compressed_file, decompressed_file, root)
