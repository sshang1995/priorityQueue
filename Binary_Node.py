'''
' Class for nodes which will binary tree.
'''
class BinaryNode:
    '''
    ' Constructor. Creates a node with an element, a parent node, a left node,
    '   and a right node. No paramteres are required but all can be specified.
    '''
    def __init__(self, element = None, parent_node = None, left_child = None, right_child = None):
        self._element = element
        self._parent = parent_node
        self._left = left_child
        self._right = right_child

    @classmethod
    def print_tree(cls, node):
        # source: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

        lines, *_ = node.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        # source: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self._right is None and self._left is None:
            line = '%s' % self._element[0]
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self._right is None:
            lines, n, p, x = self._left.display_aux()
            s = '%s' % self._element[0]
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self._left is None:
            lines, n, p, x = self._right.display_aux()
            s = '%s' % self._element[0]
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._left.display_aux()
        right, m, q, y = self._right.display_aux()
        s = '%s' % self._element[0]
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    #------------------------------- accessors -------------------------------
    '''
    ' Returns a reference to the parent node
    '''
    def get_element(self):
        return self._element

    '''
    ' Returns a reference to the parent node
    '''
    def get_parent(self):
        return self._parent

    '''
    ' Returns a reference to the left child node
    '''
    def get_left(self):
        return self._left

    '''
    ' Returns a reference to the right child node
    '''
    def get_right(self):
        return self._right

    #------------------------------- mutators -------------------------------
    '''
    ' Sets the element of the node.
    ' NOTE: This will only work if the element has not previously been set/
    '       is currently None
    '''
    def set_element(self, new_element):
        if self._element is None:
            self._element = new_element

    '''
    ' Sets the parent node and returns the old "parent child" that this
    '   node used to point to
    '''
    def set_parent(self, new_parent):
        old_parent = self._parent
        self._parent = new_parent
        return old_parent

    '''
    ' Sets the left child node and returns the old "left child" that this
    '   node used to point to
    '''
    def set_left(self, new_left):
        old_left = self._left
        self._left = new_left
        return old_left

    '''
    ' Sets the right child node and returns the old "right child" that this
    '   node used to point to
    '''
    def set_right(self, new_right):
        old_right = self._right
        self._right = new_right
        return old_right

    #----------------------------- MAGIC METHOD -----------------------------
    def __str__(self):
        output =  "Element: " + str(self.get_element()) + ";   "
        output += "Has Parent: " + str(self.get_parent() is not None) + ";   "
        output += "Has Left: " + str(self.get_left() is not None) + ";   "
        output += "Has Right: " + str(self.get_right() is not None) + ";"
        return output

if __name__ == '__main__':
    b1 = BinaryNode(10)
    b2 = BinaryNode(20)
    b3 = BinaryNode(30)
    b5 = BinaryNode(50)
    b6 = BinaryNode(60)

    b1.set_left(b2)
    b2.set_parent(b1)
    
    b1.set_right(b3)
    b3.set_parent(b1)

    b2.set_right(b5)
    b5.set_parent(b2)
    
    b3.set_left(b6)
    b6.set_parent(b3)

    print(b1)
    print()
    print(b2)
    print()
    print(b3)
    print()
    print(b5)
    print()
    print(b6)
    print()
