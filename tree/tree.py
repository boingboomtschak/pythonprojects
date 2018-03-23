import sys
# ex: [top, left, right] for 5-3-7-6-8-1-4-2 [5,[3, [1, N, 2], 4], [7, 6, 8]]
#function definition begins
def compareR(value, tlist): #function to compare tree values recursively to add them to the tree.
    if tlist[0] > value and tlist[1] is None:
        tlist[1] = [value, None, None]
    elif tlist[0] > value and tlist[1] is not None:
        compareR(value, tlist[1])
    elif tlist[0] <= value and tlist[2] is None:
        tlist[2] = [value, None, None]
    elif tlist[0] <= value and tlist[2] is not None:
        compareR(value, tlist[2])
def treeCreate (nlist): #function to create the tree
    tree = [nlist[0],None,None]
    nlist = nlist[1:]
    for item in nlist:
        compareR(item, tree)
    return tree
def insertTree(value, nlist): #function to insert a value into the tree
    nlist.append(value)
    return treeCreate(nlist)
def indexTreeR(tlist, nlist): #recursively runs through tree values in order to add them to an ordered list
    if tlist[1] is not None and tlist[2] is None:
        indexTreeR(tlist[1], nlist)
        nlist.append(tlist[0])
    elif tlist[1] is None and tlist[2] is not None:
        nlist.append(tlist[0])
        indexTreeR(tlist[2], nlist)
    elif tlist[1] is not None and tlist[2] is not None:
        indexTreeR(tlist[1], nlist)
        nlist.append(tlist[0])
        indexTreeR(tlist[2], nlist)
    elif tlist[1] is None and tlist[2] is None:
        nlist.append(tlist[0])
def getListTree(tlist): #implements indexTreeR and returns ordered list for use in calculations
    nlist = []
    indexTreeR(tlist,nlist)
    return nlist
def searchTree(value, tlist): 
    nlist = getListTree(tlist)
    if value in nlist:
        return True
    else:
        return False
def removeTree(value, nlist):
    nlist.remove(value)
    return treeCreate(nlist)
def treeToString(tlist):
    return str(tlist)
#function definition ends
numbers = input("Enter numbers for tree, separated by '-': \n")
numlist = [int(i) for i in numbers.split("-")]
print ("Initial list: " + str(numlist)) #d
inttree = treeCreate(numlist)
print("Tree: " + treeToString(inttree)) #d
insert = input("Enter an integer to insert into the tree: \n")
inttree = insertTree(int(insert), numlist)
print("Tree with inserted value: " + treeToString(inttree))
numlist2 = getListTree(inttree)
print ("Sorted list output from tree: " + str(numlist2)) #d
remove = input("Enter an integer to remove from the tree: \n")
if searchTree(int(remove), inttree) is True:
    inttree = removeTree(int(remove), numlist)
print ("Tree with removed value: " + treeToString(inttree))
