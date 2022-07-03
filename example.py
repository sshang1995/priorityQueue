import sys


class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
		self.parent = None

class MinHeap:

	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = Node(-1 * sys.maxsize )
		self.FRONT = self.Heap

	# A utility function to do inorder tree traversal

	def isLeaf(self, node):
		if node.left == None and node.right == Node:
			return True
		return False

	# Function to swap two nodes of the heap
	def swap(self, node1, node2):
		node1.data, node2.data = node2.data, node1.data

	# Function to heapify the node at pos
	def minHeapify(self, node):

		# If the node is a non-leaf node and greater than any of its child
		if not self.isLeaf(node):
			if (node.data > node.left.data or node.data > node.right.data):

				# Swap with the left child and heapify the left child
				if node.left.data < node.right.data:
					self.swap(node, node.left)
					self.minHeapify(node.left)

				# Swap with the right child and heapify the right child
				else:
					self.swap(node, node.right)
					self.minHeapify(node.right)

	# Function to insert a node into the heap
	def insert(self, element):
		if self.size >= self.maxsize :
			return
		self.size+= 1
		self.bst_insert(self.FRONT, element)

		current = self.FRONT
		while current.parent != None and current.data < current.parent.data:
			self.swap(current, current.parent)
			current = current.parent

	# Function to print the contents of the heap
	def Print(self):
		self.inorder()

	# Function to build the min heap using
	# the minHeapify function

	def inorder(self, root):
		if root:
			inorder(root.left)
			print(root.val)
			inorder(root.right)

	def bst_insert(self, root, node):
		if root is None:
			root = node
		else:
			root.next = node

		self.FRONT = node

# Driver Code
if __name__ == "__main__":

	# r = Node(50)
	# bst_insert(r,Node(30))
	# bst_insert(r,Node(20))
	# bst_insert(r,Node(40))
	# bst_insert(r,Node(70))
	# bst_insert(r,Node(60))
	# bst_insert(r,Node(80))

	# # Print inoder traversal of the BST
	# inorder(r)

	print('The minHeap is ')
	minHeap = MinHeap(15)
	minHeap.insert(Node(5))
	minHeap.insert(Node(3))
	minHeap.insert(Node(17))
	minHeap.insert(Node(10))
	minHeap.insert(Node(84))
	minHeap.insert(Node(19))
	minHeap.insert(Node(6))
	minHeap.insert(Node(22))
	minHeap.insert(Node(9))
	minHeap.minHeap()

	minHeap.Print()
	print("The Min val is " + str(minHeap.remove()))