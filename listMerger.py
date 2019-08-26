class node(object):
	def __init__(self,item,next=None):
		self.item = item
		self.next = next

def createList(L):
	newList = None
	if len(L) != 0:
		newList = node(L[0], createList(L[1:]))
	return newList

def listMerger(h1, h2):
	if not h1:
		return h2
	if not h2:
		return h1
		
	result = None
	
	if h1.item < h2.item:
		result = node(h1.item, listMerger(h1.next,h2))
	else:
		result = node(h2.item, listMerger(h1,h2.next))
		
	return result
	
def listMergerIterative(h1,h2):
#My funcion
	tempH1, tempH2, newList = h1, h2, None

	while tempH1 and tempH2:
		if tempH1.item <= tempH2.item:
			newList = node(tempH1.item, newList)
			tempH1 = tempH1.next
		else:
			newList = node(tempH2.item, newList)
			tempH2 = tempH2.next
	
	while tempH1:
		newList = node(tempH1.item, newList)
		tempH1 = tempH1.next
	while tempH2:
		newList = node(tempH2.item, newList)
		tempH2 = tempH2.next
	
	curr, prev, aft = newList, None, None
	
	while curr:
		aft = curr.next
		curr.next = prev
		prev = curr
		curr = aft

	return prev

def printList(head):
	L = []
	while head != None:
		L.append(head.item)
		head = head.next
	return L
	
list1 = [1,5,7]
list2 = [1,3,4,6,10]

head1 = createList(list1)
head2 = createList(list2)

print(printList(head1))
print(printList(head2))
head3 = listMergerIterative(head1, head2)
print(printList(head3))
