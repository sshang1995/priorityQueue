import math
from Binary_Node import *


# from ArrayHeap import *

class LinkedHeap:

    def __init__(self):
        # self.binaryNode = BinaryNode()
        self.root = None
        self._data = []
        self.count = 0

    def insert(self, key, value=None):
        binaryNode = BinaryNode([key, value])

        self.root = self._traverseTolatestPosition(self.root)

        self.count += 1
        if self.root is None:
            self.root = binaryNode
        else:
            # print(f"updacoming insert value: {key}")
            # print(f'current_root before insert value: {self.root.get_element()[0]}')
            # print(f'current_root parent: {self.root.get_parent()}')
            if key < self.root.get_element()[0]:

                if self.root.get_left() is None:

                    old_root = self.root
                    self.root = binaryNode
                    self.root.set_left(old_root)
                    self.root.set_parent(old_root.get_parent())
                    old_root.set_parent(self.root)

                    # bubble up
                    parent = self.root.get_parent()
                    # print(f'current root: {self.root}')
                    # print(f'current root parent: {parent}')
                    while parent is not None and self.root.get_element()[0] < parent.get_element()[0]:
                        old_root = self.root
                        old_root.set_right(parent.get_right())
                        old_root.set_parent(parent.get_parent())
                        self.root = parent
                        self.root.set_left(old_root.get_left())
                        self.root.set_right(None)
                        self.root.set_parent(old_root)
                        old_root.set_left(self.root)

                        # old_parent = self.root.get_parent()
                        # parent.set_left(self.root.get_left())
                        # parent.set_right(None)
                        # parent.set_parent(self.root)
                        # self.root.set_left(parent)
                        # self.root.set_right(old_parent.get_right())
                        # self.root.set_parent(old_parent.get_parent())

                        # print(f"current root is 7:{self.root},current parent is 6: {self.root.get_parent()}")

                        parent = self.root.get_parent()
                # print(f'root parent: {parent}, root: {self.root}')

                elif self.root.get_right() is None:
                    old_root = self.root
                    # print(f"old root is 8: {old_root}")
                    # print(f"old root parent is 5: {old_root.get_parent()}")
                    # print(f"inset node is 4: {binaryNode}")
                    self.root = binaryNode  # 4
                    self.root.set_left(old_root.get_left())
                    self.root.set_right(old_root)
                    self.root.set_parent(old_root.get_parent())
                    # print(f'old root left should be 11:{old_root.get_left()}')
                    # print(f'old root parent should be 6:{old_root.get_parent()}')
                    # print(f'root right should be 7:{self.root.get_right()}')
                    old_root.set_parent(self.root)
                    old_root.set_left(None)
                    old_root.set_right(None)
                    # this level is done, need to set new root
                    # self.root = self.root.get_left()

                    # print(f'root:{self.root}')
                    # print(f'root right:{self.root.get_right()}, root left:{self.root.get_left()}')
                    # bubble up
                    parent = self.root.get_parent()
                    # print(f'current root: {self.root}')
                    # print(f'current root parent: {parent}')
                    while parent is not None and self.root.get_element()[0] < parent.get_element()[0]:
                        right = parent.get_right()
                        old_root = self.root
                        old_root.set_parent(parent.get_parent())
                        self.root = parent
                        self.root.set_left(old_root.get_left())
                        self.root.set_right(old_root.get_right())
                        # print(f'old root left is 11:{old_root.get_left()}')
                        # print(f'old root right is 7:{old_root.get_right()}')
                        # print(f'old root is 5:{old_root}')

                        self.root.set_parent(old_root)
                        old_root.set_left(self.root)
                        old_root.set_right(right)
                        # print(f'parent:{parent}, parent_right is 8: {right}')
                        # print(f'current root is 6: {self.root}')
                        # print(f'current root parent is 5: {self.root.get_parent()}')
                        # print(f'current root left is 11: {self.root.get_left()}, current root right is 7: {self.root.get_right()}')
                        # print("fuck you-------------------------------")
                        # print(f'root parent right is 8: {self.root.get_parent().get_right()}')

                        parent = self.root.get_parent()
                    # print(f'parent is 5:{parent}')


            else:
                # new element bigger than root
                if self.root.get_left() is None:
                    self.root.set_left(binaryNode)
                    binaryNode.set_parent(self.root)
                elif self.root.get_right() is None:
                    self.root.set_right(binaryNode)
                    binaryNode.set_parent(self.root)
                    # this level is done, need to set new root
                    self.root = self.root.get_left()

        return binaryNode

    # 	if self.root.get_left() is None:

    # 		self.root.set_left(binaryNode)

    # 	else if self.root.get_right() is None:

    # 		self.root.set_right(binaryNode)
    # 	else:
    # 		self.root = self.root.get_left()

    # self._data.append(binaryNode)
    # self._upheap(len(self._data) -1)

    def delete(self):
        # old_min = self.peek()
        # self._swap(0, len(self._data) -1)
        # del(self._data[len(self) - 1])
        # self._downheap(0)
        # return old_min

        # back to root
        while self.root.get_parent() is not None:
            self.root = self.root.get_parent()

        self.printTree(self.root)

    def peek(self):
        while self.root.get_parent() is not None:
            self.root = self.root.get_parent()
        print(f'current head: {self.root.get_element()[0]}')
        return self.root.get_element()[0]

    def is_empty(self):
        # return len(self._data) == 0
        return len(self) == 0

    def __len__(self):
        return len(self._data)

    # help methods

    def _traverseTolatestPosition(self, currentNode):
        # print(f'initial: {currentNode}')
        if currentNode is None:
            return currentNode

        curr_tree_height = math.floor(math.log(self.count + 1, 2) - 1)
        # print(f'height: {curr_tree_height}')

        # back to root
        while currentNode.get_parent() is not None:
            currentNode = currentNode.get_parent()

        # self.printTree(currentNode)

        # print(f'tree height: {curr_tree_height}')
        while curr_tree_height > 0:
            currentNode = currentNode.get_left()
            curr_tree_height -= 1

        # print(f'{currentNode}')
        # print(f'current height: {currentNode}')
        if currentNode.get_left() and currentNode.get_right():
            currentNode = currentNode.get_parent()
            currentNode = currentNode.get_right()
        # print(f'corrct node: {currentNode}')
        return currentNode

    def printTree(self, root, level=0):
        if root != None:
            self.printTree(root.get_left(), level + 1)
            print(' ' * 4 * level + '-> ' + str(root.get_element()[0]))
            self.printTree(root.get_right(), level + 1)


if __name__ == '__main__':
    lp = LinkedHeap()
    lp.insert(11)
    lp.peek()
    lp.insert(7)
    lp.peek()
    lp.insert(8)
    lp.peek()
    lp.insert(6)
    lp.peek()
    lp.insert(5)
    lp.peek()
    lp.insert(9)
    lp.peek()
    lp.insert(4)
    lp.peek()
# lp.delete()


# print(lp.insert(11))
# print(lp.insert(7))
# print(lp.insert(8))
# print(lp.insert(6))
# print(lp.insert(5))
# print(lp.insert(9))
# print(lp.insert(4))
