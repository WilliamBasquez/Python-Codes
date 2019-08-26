"""
Created on Wed Jul 3, 10:32:46 2019
Gvinkc
Modified on Thu Aug 8, 20:26 2019
William Basquez
Hash Table with Chaining Exercises
"""
import math
class HashTable(object):
    #Builds a hash table of size 'size'
    #Bucket is a list of (initially empty) lists
    #Class functions follow
    def __init__(self, size):
        self.bucket = [[] for i in range(size)]
    def printTable(self):
        for b in range(len(self.bucket)):
            print(self.bucket[b])
def h(H, k):
    return k % len(H.bucket)

#Question 2
def insert(H, k):
    H.bucket[h(H, k)].append(k)

#Question 3
def find(H, k):
    index = -1
    pos = h(H, k)
    if pos > -1:
        if k in H.bucket[pos]:
            index = H.bucket[pos].index(k)
    return pos, index

#Question 4
def delete(H, k):
    pos = h(H, k)
    if k in H.bucket[pos]:
        H.bucket[pos].remove(k)

#Question 5
def loadFactor(H):
    elements = 0
    for i in range(len(H.bucket)):
        elements+=len(H.bucket[i])
    return elements//len(H.bucket)

#Question 6
def largestBucket(H):
    largest = 0
    for i in range(len(H.bucket)):
        if len(H.bucket[i]) > largest:
            largest = len(H.bucket[i])
    return largest

#Question 7
def check(H):
    rightPlace = True
    for index in range(len(H.bucket)):
        B = H.bucket[index]
        for b in B:
            if h(H, b) != index:
                rightPlace = False
                break
    return rightPlace

#Question 8
def insertUnique(H, k):
    pos = h(H, k)
    if k not in H.bucket[pos]:
        insert(H, k)

#Question 9
def insertBeginning(H, k):
    pos = h(H, k)
    if k not in H.bucket[pos]:
        H.bucket[pos].insert(0, k)

#Question 10
def findNMove(H, k):
    pos = h(H, k)
    if pos > -1:
        i = find(H, k)[1]
        if i > -1:
            H.bucket[pos][0], H.bucket[pos][i] = H.bucket[pos][i], H.bucket[pos][0]

if __name__ == "__main__":
    H = HashTable(7)
    L = [12,3,21,14,11,8,9,7,6,1,22,19,21,23,23]
    for k in L:
        insert(H, k)
    H.printTable()
    k = 123
    print("\nLooking for",k)
    find(H, k)
    print("\nDeleting existing item: 9")
    delete(H, 9)
    H.printTable()
    print("Deleting non-existing item: 10000")
    delete(H, 10000)
    print("\nHash Table load factor:",loadFactor(H))
    print("\nPrinting length of the largest list:",largestBucket(H))
    print("\nChecking if all items were inserted correctly")
    print(check(H))
    print("\nModifying insert to ignore duplicates")
    H2 = HashTable(7)
    for j in L:
        insertUnique(H2,j)
    H2.printTable()
    print("\nModifying insert to add new values at the beginning of the list instead of the end")
    H3 = HashTable(7)
    for a in L:
        insertBeginning(H3,a)
    H3.printTable()
    print("\nOnce an element was accessed, place it at the beginning of the list")
    findNMove(H2, 1)
    H2.printTable()