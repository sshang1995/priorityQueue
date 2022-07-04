from Binary_Node import *
from copy import copy


class LinkedHeap:

    def __init__(self):
        self.root = None  # this is a BinaryNode

    def _print_heap(self):
        if self.root:
            BinaryNode.print_tree(self.root)
        else:
            print("<None>")

    def _get_latest_insert_position(self, node_to_insert):
        '''

        :return: parent of the the position to insert the new node at
        '''
        queue = [self.root]
        if self.root is None:
            self.root = node_to_insert
        else:
            # breath first search insert to latest position
            while len(queue) > 0:
                curr_node = queue.pop(0)
                # print(f"current Node:{curr_node.get_element()}")
                # import pdb; pdb.set_trace()
                if not curr_node.get_left():
                    position_parent_to_insert = curr_node
                    return position_parent_to_insert

                if not curr_node.get_right():
                    position_parent_to_insert = curr_node
                    return position_parent_to_insert

                queue.append(curr_node.get_left())
                queue.append(curr_node.get_right())


    def insert(self, key, value=None):
        if not value:
            value = str(key)

        # print("Heap before insertion: ")
        # self._print_heap()

        node_to_insert = BinaryNode([key, value])
        # print(f"root:{self.root}")
        queue = [self.root]
        if self.root is None:
            self.root = node_to_insert
        else:
            # breath first search insert to latest position
            while len(queue) > 0:
                curr_node = queue.pop(0)
                # print(f"current Node:{curr_node.get_element()}")
                # import pdb; pdb.set_trace()
                if not curr_node.get_left():
                    # import pdb; pdb.set_trace()
                    curr_node.set_left(node_to_insert)
                    node_to_insert.set_parent(curr_node)
                    # TODO bubble up
                    # import pdb; pdb.set_trace()

                    self._upheap(node_to_insert)
                    # if we have just swapped the root, then we have a new root

                    #self.root = node_to_insert
                    self._print_heap()
                    # import pdb; pdb.set_trace()
                    return

                if not curr_node.get_right():
                    curr_node.set_right(node_to_insert)
                    node_to_insert.set_parent(curr_node)
                    # TODO bubble up
                    #self._upheap(node_to_insert)
                    return

                queue.append(curr_node.get_left())
                queue.append(curr_node.get_right())
        # print(f"finished inserting node key {key}.. (root: {self.root.get_element()}")

    def _upheap(self, current_node):

        parent = current_node.get_parent()
        while parent is not None and current_node.get_element()[0] < parent.get_element()[0]:

            # swap parent and currNode

            copyCurrNode = copy(current_node)
            copyParent = copy(parent)
            grand_parent = parent.get_parent()
            parent.set_parent(current_node)
            parent.set_left(current_node.get_left())
            parent.set_right(current_node.get_right())

            current_node.set_parent(copyParent.get_parent())
            # print(f'old parent: {copyParent}')
            # print(f"old parent left: {copyParent.get_left()}")
            # print(f'old parent right: {copyParent.get_right()}')
            if grand_parent is not None and grand_parent.get_left() is not None \
                    and grand_parent.get_left().get_element() == copyParent.get_element():

                grand_parent.set_left(current_node)

            elif grand_parent is not None and grand_parent.get_right() is not None \
                    and grand_parent.get_right().get_element() == copyParent.get_element():

                grand_parent.set_right(current_node)

            if copyParent.get_left() is not None and copyParent.get_left().get_element() == copyCurrNode.get_element():

                current_node.set_left(parent)
                current_node.set_right(copyParent.get_right())
            elif copyParent.get_right() is not None and copyParent.get_right().get_element() == copyCurrNode.get_element():

                current_node.set_right(parent)
                current_node.set_left(copyParent.get_left())

            parent = current_node.get_parent()

            if parent is None:
                self.root = current_node

    def peek(self):
        return self.root


if __name__ == '__main__':
    lp = LinkedHeap()
    # lp.insert(11)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(7)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(8)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(6)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(5)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(9)
    # print("Heap after insertion: ")
    # lp._print_heap()
    # lp.insert(4)
    # print("Heap after insertion: ")
    # lp._print_heap()

    lp.insert(11)
    print(lp.peek())
    lp._print_heap()

    lp.insert(7)
    print(lp.peek())
    lp._print_heap()

    lp.insert(8)
    print(lp.peek())
    lp._print_heap()

    lp.insert(6)
    print(lp.peek())
    lp._print_heap()

    import pdb; pdb.set_trace()
    lp.insert(5)
    print(lp.peek())
    lp._print_heap()

    lp.insert(9)
    print(lp.peek())
    lp._print_heap()

    lp.insert(4)
    print(lp.peek())
    lp._print_heap()
    # lp.printTree(lp.peek())
