import random
class node(object):
	def __init__(self, item, next = None):
		self.item = item
		self.next = next

def getLength(head):
	length = 0
	temp = head
	while temp != None:
		length+=1
		temp = temp.next
	return length

def printList(head):
	if head:
		l = []
		temp = head
		while temp != None:
			l.append(temp.item)
			temp = temp.next		
		return l
	
def copy(head):
	if head is not None:
		newList = node(head.item, copy(head.next))
		return newList
		
def itemAt(head, i):
	if head is not None:
		if i == 0:
			return head.item
		return itemAt(head.next, i-1)

def count(head,x):
	temp = head
	times = 0
	while temp != None:
		if temp.item == x:
			times+=1
		temp = temp.next
	return times

def index(head,x):
	i = 0
	temp = head
	while temp != None:
		if temp.item != x:
			i+=1
		else:
			break
		temp = temp.next
	return i

def clear(head):
	head = None

def sublist(head, start, end):
	temp = head
	newHead = None
	l = []
	if start <= end and end < getLength(head):
		while temp != None:
			l.append(temp.item)
			temp = temp.next
		for i in range(end, start-1, -1):
			newHead = node(l[i], newHead)
		
		return newHead
	return head

def reverse(head):
	prev = None
	curr = head
	while curr:
		Next = curr.next
		curr.next = prev
		prev = curr
		curr = Next
	return prev

if __name__ == "__main__":
	#L = [random.randint(0,20) for i in range(6)]
	L = [2,4,1,5,3]
	a = None
	for l in L:
		a = node(l, a)
	#print(a.next.item)
	print(printList(a))
	#print(itemAt(a,10))
	#print(count(a,54))
	#print(index(a,4))
	#print(a.item)
	#a = clear(a)
	#print(printList(a))
	b = sublist(a, 5, 5)
	print(printList(b))
	print(printList(reverse(b)))
