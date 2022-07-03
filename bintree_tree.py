#! /usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child


    def get_node_with_parent(self, data): 
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 

        return (parent, current) 
   
    def longestPath(self, root):
        if root == None:
            return []

        # recursive call on root.left and root.right
        rightvect = self.longestPath(root.right_child)
        leftvect = self.longestPath(root.left_child)

        # Compare the size of the two vectors
        # and insert current node accordingly
        if len(leftvect) > len(rightvect):
            leftvect.append(root.data)
        else:
            rightvect.append(root.data)

        if len(leftvect) > len(rightvect):
            return leftvect

        return rightvect

    def printLeafNodes(self, root):
        all_nodes = []
        all_leaves =[]

        all_nodes.append(root)

        while len(all_nodes) != 0:
            curr = all_nodes.pop()

            if curr.left_child:
                all_nodes.append(curr.left_child)

            if curr.right_child:
                all_nodes.append(curr.right_child)

            elif not curr.left_child and not curr.right_child:
                all_leaves.append(curr.data)


        return all_leaves




# n1 = Node("root node")
# n2 = Node("left child node")
# n3 = Node("right child node")
# n4 = Node("left grandchild node")

# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4

# current = n1
# while current:
#     print(current.data)
#     current = current.left_child

# tree = Tree()
# tree.insert(5)
# tree.insert(2)
# tree.insert(7)
# tree.insert(9)
# tree.insert(1)

# for i in range(1, 10):
#     found = tree.search(i)
#     print("{}: {}".format(i, found))

