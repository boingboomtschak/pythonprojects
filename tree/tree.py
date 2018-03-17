import sys
# ex: [top, left, right] for 5-3-7-6-8-1-4-2 [5,[3, [1, N, 2], 4], [7, 6, 8]]
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
    print(tree) #d
def insertTree(value, nlist): #function to insert a value into the tree
    nlist.append(value)
    treeCreate(nlist)
#function definition ends
numbers = input("Enter numbers for tree, separated by '-': \n")
numlist = [int(i) for i in numbers.split("-")]
print (numlist) #d
treeCreate(numlist)
insert = input("Enter an integer to insert into the tree.")
insertTree(int(insert), numlist)


