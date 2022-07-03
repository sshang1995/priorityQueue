from Binary_Node import *
from copy import copy

class LinkedHeap:

	def __init__(self):
		self.root = None
		self._data = []
		self.count = 0

	def insert(self, key, value = None):
		binaryNode = BinaryNode([key,value])
		#print(f"root:{self.root}")
		queue = [self.root]
		if self.root is None:
			self.root = binaryNode
		else:
			# breath first search insert to latest position
			while len(queue) > 0:
				curr_node = queue.pop(0)
				#print(f"current Node:{curr_node.get_element()}")

				if not curr_node.get_left():
					curr_node.set_left(binaryNode)
					#binaryNode.set_parent(curr_node)
					#TODO bubble up
					#self._upheap(binaryNode)
					return binaryNode
					

				if not curr_node.get_right():
					curr_node.set_right(binaryNode)
					#binaryNode.set_parent(curr_node)
					# TODO bubble up
					#self._upheap(binaryNode)
					return binaryNode

				queue.append(curr_node.get_left())
				queue.append(curr_node.get_right())

			#self._upheap(binaryNode)

			

	def _upheap(self, currNode):
		parent = currNode.get_parent()
		# print(f"currNode: {currNode.get_element()}")
		# print(f"parent: {parent.get_element()}")
		if parent is not None and currNode.get_element()[0] < parent.get_element()[0]:
			# swap parent and currNode
			copyCurrNode = copy(currNode)
			copyParent = copy(parent)
			# print(f"copy currNode: {copyCurrNode.get_element()}")
			# print(f"copy parent: {copyParent.get_element()}")
			parent.set_parent(currNode)
			parent.set_left(currNode.get_left())
			parent.set_right(currNode.get_right())

			currNode.set_parent(copyParent.get_parent())
			if copyParent.get_left().get_element() == copyCurrNode.get_element():

				currNode.set_left(parent)
				currNode.set_right(copyParent.get_right())
			else:
				currNode.set_right(parent)
				currNode.set_left(copyParent.get_right())

			# currNode.set_parent(parent.get_parent())
			# currNode.set_left(parent.get_left())
			# currNode.set_right(parent.get_right())

			# parent.set_parent(currNode)
			# parent.set_left(copyCurrNode.get_left())
			# parent.set_right(copyCurrNode.get_right())
			# print(f"new currNode: {currNode.get_element()}")
			# print(f"new parent: {parent.get_element()}")
			self._upheap(parent)


	def printTree(self, root, level=0):
		if root != None:
			self.printTree(root.get_left(), level + 1)
			print(' ' * 4 * level + '-> ' + str(root.get_element()[0]))
			self.printTree(root.get_right(), level + 1)

if __name__ == '__main__':
	lp = LinkedHeap()
	# lp.insert(11)
	# lp.insert(7)
	# lp.insert(8)
	# lp.insert(6)
	# lp.insert(5)
	# lp.insert(9)
	# lp.insert(4)

	

	print(lp.insert(11))
	print(lp.insert(7))
	print(lp.insert(8))
	print(lp.insert(6))
	print(lp.insert(5))
	print(lp.insert(9))
	print(lp.insert(4))
