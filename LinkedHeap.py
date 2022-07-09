from Binary_Node import *
from copy import copy


class LinkedHeap:

    def __init__(self):
        self.root = None  # this is a BinaryNode
        self.count = 0

    def insert(self, key, value=None):
        self.count += 1
        # if not value:
        #     value = str(key)
        node_to_insert = BinaryNode([key, value])
        insertion_parent = self._get_latest_insert_position()
        if not insertion_parent:
            self.root = node_to_insert
        else:
            if not insertion_parent.get_left():
                insertion_parent.set_left(node_to_insert)
                node_to_insert.set_parent(insertion_parent)
                # import pdb; pdb.set_trace()\
                # bubble up
                self._upheap(node_to_insert)

            elif not insertion_parent.get_right():
                insertion_parent.set_right(node_to_insert)
                node_to_insert.set_parent(insertion_parent)

                # bubble up
                self._upheap(node_to_insert)

    def delete(self):
        if self.count == 0:
            return

        # import pdb;
        # pdb.set_trace()
        deleted_root = self.root
        # get last node
        last_node = self._get_last_node()
        if not last_node:
            return

        # if last_node is root node, set root as None
        if last_node.get_element() == self.root.get_element():
            self.root = None
            self.count = 0
            return deleted_root.get_element()

        # swap root and last node
        copy_last_node = copy(last_node)
        copy_root = copy(deleted_root)
        # set last node to root position
        if copy_root.get_left() and copy_root.get_left().get_element() == copy_last_node.get_element():
            last_node.set_left(copy_root)
            deleted_root.get_left().set_parent(last_node)

            last_node.set_right(deleted_root.get_right())
            if deleted_root.get_right():
                deleted_root.get_right().set_parent(last_node)
        elif copy_root.get_right() and copy_root.get_right().get_element() == copy_last_node.get_element():
            last_node.set_right(copy_root)
            deleted_root.get_right().set_parent(last_node)

            last_node.set_left(deleted_root.get_left())
            if deleted_root.get_left():
                deleted_root.get_left().set_parent(last_node)
        else:
            if copy_root.get_left():
                last_node.set_left(deleted_root.get_left())
                deleted_root.get_left().set_parent(last_node)
            if copy_root.get_right():
                last_node.set_right(deleted_root.get_right())
                deleted_root.get_right().set_parent(last_node)

        last_node.set_parent(None)
        self.root = last_node

        # set old root node to last position
        if copy_last_node.get_parent() and copy_last_node.get_parent().get_element() == copy_root.get_element():
            copy_root.set_parent(self.root)
        else:
            copy_root.set_parent(copy_last_node.get_parent())

        if copy_last_node.get_parent() and copy_last_node.get_parent().get_left() and \
            copy_last_node.get_parent().get_left().get_element() == copy_last_node.get_element():

            copy_last_node.get_parent().set_left(copy_root)

        elif copy_last_node.get_parent() and copy_last_node.get_parent().get_right() and \
            copy_last_node.get_parent().get_right().get_element() == copy_last_node.get_element():

            copy_last_node.get_parent().set_right(copy_root)

        copy_root.set_left(None)
        copy_root.set_right(None)
        last_node = copy_root

        # delete last node
        curr_last_node = self._get_last_node()
        if curr_last_node.get_parent() and curr_last_node.get_parent().get_left() and \
            curr_last_node.get_parent().get_left().get_element() == curr_last_node.get_element():

            curr_last_node.get_parent().set_left(None)

        elif curr_last_node.get_parent() and curr_last_node.get_parent().get_right() and \
                curr_last_node.get_parent().get_right().get_element() == curr_last_node.get_element():
            curr_last_node.get_parent().set_right(None)

        curr_last_node.set_parent(None)

        self.count -= 1
        # bubble down current root node
        self._downheap(self.root)

        return last_node.get_element()

    def peek(self):
        return self.root.get_element()

    # ----------------help method--------------------
    '''
        move node with smaller key up, move parent down the tree
    '''
    def _upheap(self, current_node):

        parent = current_node.get_parent()
        # while the current node is not root and,
        # parent of the current node has a bigger value than the current node
        if parent and current_node.get_element()[0] < parent.get_element()[0]:
            # swap parent and current_node, return parent position which is a new position
            old_parent = self._swap(parent, current_node)
            if old_parent.get_parent().get_parent() is None:
                self.root = old_parent.get_parent()

            self._upheap(old_parent.get_parent())

    '''
        move bigger node down, move smaller node up
    '''
    def _downheap(self, root):
        if root.get_left():
            min_node = root.get_left()
            right_node = root.get_right()

            if right_node and right_node.get_element()[0] < min_node.get_element()[0]:
                min_node = right_node

            if root.get_element()[0] > min_node.get_element()[0]:
                root = self._swap(root, min_node)
                if root.get_parent().get_parent() is None:
                    self.root = root.get_parent()
                self._downheap(root)

    '''
        swap parent node and current node
    '''
    def _swap(self, parent, current_node):
        # make a copy of current node and parent before the swap
        copy_current_node = copy(current_node)
        copy_parent = copy(parent)

        grandparent = parent.get_parent()

        # set currentNode to parent position, remove parent position
        current_node.set_parent(grandparent)
        # set grandparent to new child (current_node)
        if grandparent is not None and grandparent.get_left() is not None \
                and grandparent.get_left().get_element() == copy_parent.get_element():

            grandparent.set_left(current_node)

        elif grandparent is not None and grandparent.get_right() is not None \
                and grandparent.get_right().get_element() == copy_parent.get_element():

            grandparent.set_right(current_node)

        # set curren_Node's left and right child
        if copy_parent.get_left() is not None and copy_parent.get_left().get_element() == copy_current_node.get_element():

            current_node.set_left(parent)
            current_node.set_right(copy_parent.get_right())
            # set right child's parent to current_node
            if copy_parent.get_right():
                copy_parent.get_right().set_parent(current_node)

        elif copy_parent.get_right() is not None and copy_parent.get_right().get_element() == copy_current_node.get_element():

            current_node.set_right(parent)
            current_node.set_left(copy_parent.get_left())
            # set left child's parent to current_node
            if copy_parent.get_left():
                copy_parent.get_left().set_parent(current_node)

        # set parent to child position
        parent.set_parent(current_node)
        parent.set_left(copy_current_node.get_left())
        parent.set_right(copy_current_node.get_right())

        # set grandsons point to current parent
        if copy_current_node.get_left():
            copy_current_node.get_left().set_parent(parent)

        if copy_current_node.get_right():
            copy_current_node.get_right().set_parent(parent)

        return parent

    '''
        get the last node in the tree
    '''
    def _get_last_node(self):
        queue = [self.root]
        total_nodes_count = copy(self.count)
        if total_nodes_count == 1:
            return self.root
        total_nodes_count -= 1
        while len(queue) > 0 and total_nodes_count >= 1:
            curr_node = queue.pop(0)
            if curr_node.get_left():
                if total_nodes_count > 1:
                    total_nodes_count -= 1
                else:
                    return curr_node.get_left()

            if curr_node.get_right():
                if total_nodes_count > 1:
                    total_nodes_count -= 1
                else:
                    return curr_node.get_right()

            if curr_node.get_left():
                queue.append(curr_node.get_left())
            if curr_node.get_right():
                queue.append(curr_node.get_right())

    '''
    :return: parent of the position to insert the new node at
    '''
    def _get_latest_insert_position(self):
        queue = [self.root]
        if self.root is None:
            return self.root
        else:
            # breath first search insert to latest position
            while len(queue) > 0:
                curr_node = queue.pop(0)
                if not curr_node.get_left():
                    position_parent_to_insert = curr_node
                    return position_parent_to_insert

                if not curr_node.get_right():
                    position_parent_to_insert = curr_node
                    return position_parent_to_insert

                queue.append(curr_node.get_left())
                queue.append(curr_node.get_right())

    '''
     print current heap tree
    '''
    def _print_heap(self):
        if self.root:
            self.root.print_tree(self.root)
        else:
            print("<None>")

if __name__ == '__main__':
    lp = LinkedHeap()
    print("Inserting 11")
    lp.insert(11)
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')


    print("Inserting 7")
    lp.insert(7)
    #lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()

    print("Inserting 8")
    lp.insert(8)
    #lp._print_heap()
    #lp.delete()
    #lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()

    print("Inserting 6")
    lp.insert(6)
    # lp._print_heap()
    # lp.delete()
    # lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()

    print("Inserting 5")
    lp.insert(5)
    # lp._print_heap()
    # lp.delete()
    # lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()

    print("Inserting 9")
    lp.insert(9)
    # lp._print_heap()
    # lp.delete()
    # lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()

    print("Inserting 4")
    lp.insert(4)
    lp._print_heap()
    deleted_node = lp.delete()
    print(deleted_node)
    lp._print_heap()
    print(f"current root: {lp.peek()}")
    print(f'get last node: {lp._get_last_node()}')
    #lp._print_heap()


    # import pdb; pdb.set_trace()

