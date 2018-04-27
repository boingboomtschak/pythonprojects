#http://www.pythontutor.com/visualize.html#code=dict%20%3D%20%7B'%20'%3A%2081452,%20'T'%3A%20682,%20'H'%3A%20840,%20'E'%3A%2088,%20'O'%3A%20123,%20'U'%3A%207,%20'N'%3A%20170,%20'D'%3A%20205,%20'F'%3A%2087,%20'B'%3A%20445,%20'A'%3A%20365,%20'S'%3A%20597,%20'K'%3A%204,%20'R'%3A%2066,%20'V'%3A%2030,%20'I'%3A%201895,%20'L'%3A%20151,%20'r'%3A%2014365,%20't'%3A%2022011,%20'h'%3A%2015913,%20'u'%3A%207482,%20'C'%3A%20236,%20'o'%3A%2019253,%20'n'%3A%2016251,%20'a'%3A%2019375,%20'y'%3A%205037,%20'l'%3A%209575,%20'e'%3A%2029958,%20'b'%3A%203129,%20'f'%3A%205090,%20'c'%3A%205689,%20's'%3A%2014754,%20'M'%3A%20343,%20'.'%3A%203417,%20'k'%3A%201934,%20'm'%3A%206309,%20'v'%3A%202587,%20'i'%3A%2015237,%20'P'%3A%2071,%20'd'%3A%2010267,%20'p'%3A%203716,%20'W'%3A%20529,%20'x'%3A%20382,%20'g'%3A%204274,%20','%3A%203509,%20'w'%3A%205938,%20'q'%3A%20183,%20'-'%3A%20662,%20'%22'%3A%202771,%20'J'%3A%2032,%20'1'%3A%2018,%20'8'%3A%2014,%20'4'%3A%2010,%20'j'%3A%20125,%20'%3F'%3A%20518,%20%22'%22%3A%20438,%20'G'%3A%2075,%20'!'%3A%20182,%20'Y'%3A%20214,%20'2'%3A%209,%20'z'%3A%20121,%20'%28'%3A%205,%20'%29'%3A%205,%20'3'%3A%205,%20'%3B'%3A%2052,%20'7'%3A%209,%20'0'%3A%208,%20'%3A'%3A%2020,%20'%5B'%3A%201,%20'%5D'%3A%201,%20'6'%3A%205,%20'Q'%3A%208,%20'%C3%AA'%3A%202,%20'%C3%A0'%3A%201,%20'X'%3A%207,%20'5'%3A%201,%20'%C3%A9'%3A%203,%20'/'%3A%202%7D%0Adef%20createTree%28fdict%29%3A%20%23creates%20tree%20from%20a%20given%20dictionary%20with%20key%3Avalue%20as%20letter%3Afrequency%0A%20%20%20%20flist%20%3D%20%5B%5D%0A%20%20%20%20for%20key,%20value%20in%20fdict.items%28%29%3A%20%23reverses%20given%20dictionary%20from%20letter%3Afrequency%20to%20frequency%3Aletter%0A%20%20%20%20%20%20%20%20flist.append%28%5Bint%28value%29,%20key%5D%29%0A%20%20%20%20flist.sort%28%29%0A%20%20%20%20while%20len%28flist%29%20%3E%201%3A%20%23repeatedly%20runs%20Huffman%20tree%20algorithm%20until%20the%20list%20is%201%20item%20%28that%20item%20being%20the%20tree%29%0A%20%20%20%20%20%20%20%20if%20flist%5B0%5D%5B0%5D%20%3E%3D%20flist%5B1%5D%5B0%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D,%20None,%20None%29,%28flist%5B0%5D%5B1%5D,%20None,%20None%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20not%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D,%20None,%20None%29,%28flist%5B0%5D%5B1%5D%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20not%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D%29,%20%28flist%5B0%5D%5B1%5D,%20None,%20None%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20not%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20not%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D%29,%20%28flist%5B0%5D%5B1%5D%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20flist%5B1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20flist%5B1%5D%0A%20%20%20%20%20%20%20%20elif%20flist%5B1%5D%5B0%5D%20%3E%3D%20flist%5B0%5D%5B0%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B0%5D%5B1%5D,%20None,%20None%29,%28flist%5B1%5D%5B1%5D,%20None,%20None%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20not%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%20and%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B0%5D%5B1%5D,%20None,%20None%29,%28flist%5B1%5D%5B1%5D%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%20and%20not%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D%29,%20%28flist%5B0%5D%5B1%5D,%20None,%20None%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20not%20isinstance%28flist%5B0%5D%5B1%5D,%20str%29%20and%20not%20isinstance%28flist%5B1%5D%5B1%5D,%20str%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20flist.insert%280,%20%5Bint%28flist%5B0%5D%5B0%5D%2Bflist%5B1%5D%5B0%5D%29,%20%28None,%20%28flist%5B1%5D%5B1%5D%29,%20%28flist%5B0%5D%5B1%5D%29%29%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20flist%5B1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20flist%5B1%5D%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Exception%20during%20tree%20creation!%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%28%29%0A%20%20%20%20return%20flist%5B0%5D%5B1%5D%0Atree%20%3D%20createTree%28dict%29%0Adict%20%3D%20%7B%7D&cumulative=false&curInstr=705&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
import sys
dict = {' ': 81452, 'T': 682, 'H': 840, 'E': 88, 'O': 123, 'U': 7, 'N': 170, 'D': 205, 'F': 87, 'B': 445, 'A': 365, 'S': 597, 'K': 4, 'R': 66, 'V': 30, 'I': 1895, 'L': 151, 'r': 14365, 't': 22011, 'h': 15913, 'u': 7482, 'C': 236, 'o': 19253, 'n': 16251, 'a': 19375, 'y': 5037, 'l': 9575, 'e': 29958, 'b': 3129, 'f': 5090, 'c': 5689, 's': 14754, 'M': 343, '.': 3417, 'k': 1934, 'm': 6309, 'v': 2587, 'i': 15237, 'P': 71, 'd': 10267, 'p': 3716, 'W': 529, 'x': 382, 'g': 4274, ',': 3509, 'w': 5938, 'q': 183, '-': 662, '"': 2771, 'J': 32, '1': 18, '8': 14, '4': 10, 'j': 125, '?': 518, "'": 438, 'G': 75, '!': 182, 'Y': 214, '2': 9, 'z': 121, '(': 5, ')': 5, '3': 5, ';': 52, '7': 9, '0': 8, ':': 20, '[': 1, ']': 1, '6': 5, 'Q': 8, 'ê': 2, 'à': 1, 'X': 7, '5': 1, 'é': 3, '/': 2}
def createTree(fdict): #creates tree from a given dictionary with key:value as letter:frequency
    flist = []
    for key, value in fdict.items(): #reverses given dictionary from letter:frequency to frequency:letter
        flist.append([int(value), key])
    flist.sort()
    while len(flist) > 1: #repeatedly runs Huffman tree algorithm until the list is 1 item (that item being the tree)
        if flist[0][0] >= flist[1][0]:
            if isinstance(flist[0][1], str) and isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1], None, None),(flist[0][1], None, None))])
            elif not isinstance(flist[0][1], str) and isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1], None, None),(flist[0][1]))])
            elif isinstance(flist[0][1], str) and not isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1]), (flist[0][1], None, None))])
            elif not isinstance(flist[0][1], str) and not isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1]), (flist[0][1]))])
            del flist[1]
            del flist[1]
        elif flist[1][0] >= flist[0][0]:
            if isinstance(flist[0][1], str) and isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[0][1], None, None),(flist[1][1], None, None))])
            elif not isinstance(flist[1][1], str) and isinstance(flist[0][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[0][1], None, None),(flist[1][1]))])
            elif isinstance(flist[1][1], str) and not isinstance(flist[0][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1]), (flist[0][1], None, None))])
            elif not isinstance(flist[0][1], str) and not isinstance(flist[1][1], str):
                flist.insert(0, [int(flist[0][0]+flist[1][0]), (None, (flist[1][1]), (flist[0][1]))])
            del flist[1]
            del flist[1]
        else:
            print("Exception during tree creation!")
            sys.exit()
    return flist[0][1]
tree = createTree(dict)
