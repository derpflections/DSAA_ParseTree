import itertools

class GraphTree():
    def __init__(self, name, parent, *data):
        self.name = name
        self.parent = parent
        self.data = data
        self.children = []
        self.is_root = False

    def __repr__(self):
        return 'Node '+repr(self.name)

    def dic(self):
        retval = {self: []}
        for i in self.children:
            retval[self].append(i.dic())
        return retval

    def display(self):
        if not self.children:
            return self.name

        child_strs = [child.display() for child in self.children]
        child_widths = [self.block_width(s) for s in child_strs]

        display_width = max(len(self.name),
                            sum(child_widths) + len(child_widths) - 1)

        child_midpoints = []
        child_end = 0
        for width in child_widths:
            child_midpoints.append(child_end + (width // 2))
            child_end += width + 1

        brace_builder = []
        for i in range(display_width):  # Updated xrange to range
            if i < child_midpoints[0] or i > child_midpoints[-1]:
                brace_builder.append(' ')
            elif i in child_midpoints:
                brace_builder.append('+')
            else:
                brace_builder.append('-')
        brace = ''.join(brace_builder)

        name_str = '{:^{}}'.format(self.name, display_width)
        below = self.stack_str_blocks(child_strs)

        return name_str + '\n' + brace + '\n' + below

    def has_children(self):
        return bool(self.children)

    def get_parent(self):
        return self.parent

    def add_child(self, name, *data):
        child = GraphTree(name, self, *data)
        self.children.append(child)
        return child

    def block_width(self, block):
        try:
            return block.index('\n')
        except ValueError:
            return len(block)

    def stack_str_blocks(self, blocks):
        builder = []
        block_lens = [self.block_width(bl) for bl in blocks]
        split_blocks = [bl.split('\n') for bl in blocks]

        for line_list in itertools.zip_longest(*split_blocks, fillvalue=None):  # Updated izip_longest to zip_longest
            for i, line in enumerate(line_list):
                if line is None:
                    builder.append(' ' * block_lens[i])
                else:
                    builder.append(line)
                if i != len(line_list) - 1:
                    builder.append(' ')  # Padding
            builder.append('\n')

        return ''.join(builder[:-1])
