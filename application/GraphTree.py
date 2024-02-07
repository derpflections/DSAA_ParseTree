# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

import itertools

class GraphTree(): #done by Wei Qi
    """
        A class to represent a node in a tree structure for graphical visualization.

        Attributes:
            name (str): The name of the node.
            parent (GraphTree): The parent node of the current node. None indicates that the node is the root.
            data (tuple): Additional data associated with the node.
            children (list): A list of GraphTree instances representing the children of the node.
            is_root (bool): A flag indicating if the node is the root node of the tree.

        Methods:
            __init__(self, name, parent, *data): Initializes a new GraphTree instance.
            __repr__(self): Returns a string representation of the GraphTree instance, primarily for debugging.
            dic(self): Generates a nested dictionary representation of the tree.
            display(self): Returns a string representing the hierarchical structure of the tree.
            has_children(self): Checks if the node has any children.
            get_parent(self): Returns the parent of the current node.
            add_child(self, name, *data): Adds a new child to the current node.
            block_width(block): Calculates the display width of a string block.
            stack_str_blocks(blocks): Vertically stacks string representations of child nodes.
    """
    # Constructor method for initializing a new instance of the GraphTree class.
    # The `*data` parameter allows for an arbitrary number of arguments to be passed, which are stored in a tuple.
    def __init__(self, name, parent, *data):
        self.name = name  # Name of the node.
        self.parent = parent  # Parent node reference. None indicates a root node.
        self.data = data  # Additional data passed to the node.
        self.children = []  # List to store child nodes.
        self.is_root = False  # Flag to indicate if the node is the root node.

    # Representation method to provide a string representation of the node, mainly for debugging purposes.
    def __repr__(self):
        return 'Node ' + repr(self.name)

    # Method to generate a dictionary representation of the tree with the current node as the root.
    # The method recursively calls `dic` on child nodes to build a nested dictionary structure.
    def dic(self):
        retval = {self: []}
        for i in self.children:
            retval[self].append(i.dic())
        return retval

    # Method to visually display the tree structure as a string.
    # It constructs a hierarchical representation using the names of nodes and visual connectors.
    def display(self):
        if not self.children:
            return self.name

        # Generating string representations for each child and calculating their display widths.
        child_strs = [child.display() for child in self.children]
        child_widths = [self.block_width(s) for s in child_strs]

        # Calculating the width required to display the current node based on its name and the combined width of its children.
        display_width = max(len(self.name),
                            sum(child_widths) + len(child_widths) - 1)

        # Calculating midpoints for children to align connectors ('+' and '-') correctly.
        child_midpoints = []
        child_end = 0
        for width in child_widths:
            child_midpoints.append(child_end + (width // 2))
            child_end += width + 1

        # Building the connector string between the current node and its children.
        brace_builder = []
        for i in range(display_width):
            if i < child_midpoints[0] or i > child_midpoints[-1]:
                brace_builder.append(' ')
            elif i in child_midpoints:
                brace_builder.append('+')
            else:
                brace_builder.append('-')
        brace = ''.join(brace_builder)

        # Center-aligning the node's name over the connector line.
        name_str = '{:^{}}'.format(self.name, display_width)
        # Stacking the child node strings below the current node.
        below = self.stack_str_blocks(child_strs)

        return name_str + '\n' + brace + '\n' + below

    # Method to check if the current node has any children.
    def has_children(self):
        return bool(self.children)

    # Method to get the parent of the current node.
    def get_parent(self):
        return self.parent

    # Method to add a child node to the current node.
    # It creates a new instance of GraphTree as the child and appends it to the children list.
    def add_child(self, name, *data):
        child = GraphTree(name, self, *data)
        self.children.append(child)
        return child

    # Helper method to calculate the display width of a string block, which is essential for alignment in the display.
    def block_width(self, block):
        try:
            return block.index('\n')  # The width is up to the first newline character.
        except ValueError:
            return len(block)  # If no newline, the width is the length of the string.

    # Method to vertically stack string representations of child nodes, ensuring correct alignment.
    def stack_str_blocks(self, blocks):
        builder = []
        block_lens = [self.block_width(bl) for bl in blocks]
        split_blocks = [bl.split('\n') for bl in blocks]

        # Loop through each line of the split blocks, adding spaces for alignment and padding between blocks.
        for line_list in itertools.zip_longest(*split_blocks, fillvalue=None):  # Handling variable number of lines.
            for i, line in enumerate(line_list):
                if line is None:
                    builder.append(' ' * block_lens[i])
                else:
                    builder.append(line)
                if i != len(line_list) - 1:
                    builder.append(' ')  # Padding between blocks.
            builder.append('\n')

        return ''.join(builder[:-1])  # Joining all parts together except for the last newline.
