
class BSTNode(object):
	def __init__(self, value = 0):
		self.value = value
		self.lNode = None
		self.rNode = None


class BST(object):
	def __init__(self, root=None):
		self.root = root

	def isEmpty(self):
		if self.root == None:
			return True
		else:
			return False

	def insert(self, value):
		newNode = BSTNode(value)
		if self.root == None:
			self.root = newNode
		else:
			currentNode = self.root

			while currentNode and currentNode.value != value:
				if currentNode.value > value:
					if currentNode.lNode == None:
						currentNode.lNode = newNode
				else:
					if currentNode.rNode == None:
						currentNode.rNode = newNode

	def _inorder(self, bst, values):
		if bst != None:
			self._inorder(bst.lNode, values)
			values.append(bst.value)
			self._inorder(bst.rNode, values)

	def printInorder(self):
		values = []
		self._inorder(bst.root, values)
		print(values)

	def find(self, value):
		currentNode = self.root
		while currentNode != None and currentNode.value != value:
			if currentNode.value > value:
				currentNode = currentNode.lNode
			else:
				currentNode = currentNode.rNode

		if currentNode != None:
			return currentNode

		return None

	def findMIN(self):
		minNode = self.root

		while minNode != None and minNode.lNode != None:
			minNode = minNode.lNode

		return minNode


	def findMAX(self)
		maxNode = self.root

		while maxNode != None and maxNode.rNode != None:
			maxNode = maxNode.rNode

		return maxNode


	def _delete(self, bst, value):
		if bst == None:
			return None

		if bst.value > value:
			bst.lNode = self._delete(bst.lNode, value)
		elif bst.value < value:
			bst.rNode = self._delete(bst.rNode, value)
		else:
			#Delete the node
			if bst.lNode == None and bst.rNode == None:
				bst = None
			elif bst.lNode == None:
				

		return bst


	def delete(self, value):
		deleteNode = self.find(value)

		if deleteNode == None:
			return False

		#The node is existed
		if deleteNode.lNode == None and deleteNode.rNode == None:



if __name__ == "__main__":
	values = [1, 4, 8, 9, 5, 6, 0, 2, 7, 99, 100, 22, -30, 34, 45]

	bst = BST()

	for value in values:
		bst.insert(value)

	bst.printInorder()
