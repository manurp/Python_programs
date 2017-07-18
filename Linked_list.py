class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(Node):
	"""docstring for LinkedList"""
	def __init__(self, data):
		# super(Node, self).__init__(data)
		self.head = Node(data)

	def addToHead(self,data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def printList(self):
		cursor = self.head
		while cursor != None:
			print(cursor.data)
			cursor = cursor.next

ll = LinkedList(5)
ll.addToHead(3)
ll.addToHead(8)
ll.printList()
		