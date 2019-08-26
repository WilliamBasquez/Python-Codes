import BST_1 as Tree
import math

"""
This code answers the question from the file "BST2"
"""

#Question 1
def lessThanK(T, k):
	if T:
		lessThanK(T.right, k)
		if k > T.item:
			print(T.item)
		lessThanK(T.left, k)
		
#Question 2
def printLeaves(T):
	if T:
		printLeaves(T.left)
		if T.isLeaf():
			print(T.item)
		printLeaves(T.right)
		
#Question 3
def biggestAtDepth(T, d):
	if T:
		if T.isLeaf() and d != 0:
			print(-math.inf)
			#return
		elif d == 0:
			print(T.item)
			return
		biggestAtDepth(T.right, d-1)

#Question 4
def printAtDepth(T, d):
	if T:
		if d == 0:
			print(T.item)
		printAtDepth(T.left, d-1)
		printAtDepth(T.right, d-1)

#Question 5
def heightOfK(T, k):
	height = 0
	temp = T

	while temp:
		if k == temp.item:
			return height
		elif k < temp.item:
			height+=1
			temp = temp.left
		else:
			height+=1
			temp = temp.right
	return -1

#Question 6
def sortedList(T):
	if T:
		sortedList(T.left)
		l.append(T.item)
		sortedList(T.right)
	return l

#Question 7
def createBalancedTree(L):
	if not L:
		return None
	
	mid = len(L)//2
	Head = Tree.BST(L[mid])
	Head.left = createBalancedTree(L[:mid])
	Head.right = createBalancedTree(L[mid+1:])
	return Head

#Question 8
def printByDepth(T):
	TreeHeight = Tree.treeHeight(T)
	for i in range(TreeHeight, -1, -1):
		printAtDepth(T, i)

if __name__ == "__main__":
	k = 100
	T = None
	#A = [4,2,3,1,6,5,7]
	l = []
	#A = [70,50,90,130,150,40,10,30,100]
	A = [70,50,90,130,150,40,10,30,100,180,45,60,140,42]
	B = sorted(A)
	for a in A:
		T = Tree.insert(T, a)
	Tree.printTree(T)
	print("\nQuestion 1: Given a reference to a tree's root, and an integer 'k', print the elements of the tree that are less than k")
	print("k:", k)
	lessThanK(T, k)
	print("\nQuestion 2: Given a reference to a tree's root, print all the elements that are stored at the leavesof the tree")
	printLeaves(T)
	print("\nQuestion 3: Given a reference to a tree's root, and a depth 'd', print the biggest element with depth 'd', or infinity if the tree does not have nodes at depth 'd'")
	biggestAtDepth(T,3)
	print("\nQuestion 4: Given a reference to a tree's root, and a depth 'd', print all the elements with depth 'd', or infinity if the tree does not have nodes at depth 'd'")
	printAtDepth(T, 0)
	print("\nQuestion 5: Given a reference to a tree's root, and an integer 'k', print the height of the node containing k, or -1 if k is not in the tree")
	print(heightOfK(T,8))
	print("\nQuestion 6: Given a reference to a tree's root, return a sorted list of the elements in the tree")
	print(sortedList(T))
	H = createBalancedTree(sorted(A))
	print("\nQuestion 7: Given a sorted list, build and return a balanced BST (as much as possible)")
	Tree.printTree(H)
	print("\nQuestion 8: Given a reference to a tree's root, print all items in the tree by depth")
	printByDepth(T)
