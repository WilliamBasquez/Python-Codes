"""
This code answers the question from the file "BST1"
Class,'insert' and 'printTree' functions were provided by Dr. Olac Fuentes from UTEP
"""
class BST(object):
	def __init__(self, item, left = None, right = None):
		self.item = item
		self.left = left
		self.right = right

	def isLeaf(self):
		return self.left is None and self.right is None

def insert(T, newItem):
	if not T:
		T = BST(newItem)
	elif T.item > newItem:
		T.left = insert(T.left, newItem)
	else:
		T.right = insert(T.right, newItem)
	return T
	
def printTree(T, space = ''):
	if T:
		printTree(T.right, space + '   ')
		print(space,T.item)
		printTree(T.left, space + '   ')

#Question 2
def printTreeList(T):
	if T:
		printTreeList(T.left)
		print(T.item)
		printTreeList(T.right)

#Question 3
def findSmallest(T):
	if T:
		if T.left:
			return findSmallest(T.left)
		return T.item
		
#Question 4
def findBiggest(T):
	if T:
		if T.right:
			return findBiggest(T.right)
		return T.item
		
#Question 5
def search(T, k):
	if T:
		if k == T.item:
			print("k was found on the tree")
			return T
		elif k < T.item:
			return search(T.left, k)
		else:
			return search(T.right, k)
	return None
	
#Question 6
def numberOfNodes(T):
	if T:
		leftSide = numberOfNodes(T.left)
		rightSide = numberOfNodes(T.right)
		return leftSide + rightSide + 1
	return 0
	
#Question 7
def treeHeight(T):
	if not T:
		return -1
	if T.isLeaf():
		return 0
	leftTree = treeHeight(T.left)
	rightTree = treeHeight(T.right)
	return max(leftTree, rightTree)+1

if __name__ == "__main__":
	k = 60
	T = None
	A = [70,50,90,130,150,40,10,30,100]
	#A = [70,50,90,130,150,40,10,30,100,180,45,60,140,42]
	B = sorted(A)
	for a in A:
		T = insert(T, a)
	printTree(T)
	print("\nQuestion #2: Print a binary search tree in ascending order given a reference to its root")
	printTreeList(T)
	print("\nQuestion #3: Find the smallest item in a tree given a reference to its root")
	print(findSmallest(T))
	print("\nQuestion #4: Find the biggest item in a tree given a reference to its root")
	print(findBiggest(T))
	print("\nQuestion #5: Given a reference to a tree's root, and an integer 'k', return a reference to the node where 'k' is, else return None\nk:",k,' - ',search(T, k))
	#print(k,search(T, k))
	print("\nQuestion #6: Given a reference to a tree's root, return the number of nodes in the tree")
	print("There are",numberOfNodes(T),"nodes in the tree")
	print("\nQuestion #7: Given a reference to a tree's root, return the height of the tree")
	print(treeHeight(T))
