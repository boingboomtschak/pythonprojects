import sys
import binascii
#function definition begins
def getArgs (argv): #defines function to add -[letter] [input] pairs into dictionary
    args = {}
    while argv:
        if argv[0][0] == "-":
            args[argv[0]] = argv[1]
        argv = argv[1:]
    return args
def decodeR(string, tlist, out, rlevel=0):
    if tlist[1] is None and tlist[2] is None: #function is at a leaf
        for i in range(0, rlevel):
            del string[0]
        out.append(tlist[0])
    elif string[int(rlevel)] == "0":
        decodeR(string, tlist[1], out, rlevel=rlevel+1)
    elif string[int(rlevel)] == "1":
        decodeR(string, tlist[2], out, rlevel=rlevel+1)
    else:
        print("Exception while decoding string!")
        sys.exit()
def indexR(tlist, ndict, path=list()): #recursively indexes tree into dictionary with key:value as letter:path
    if tlist[1] is not None and tlist[2] is None:
        indexR(tlist[1], ndict, path=path+["0"])
    if tlist[1] is None and tlist[2] is not None:
        indexR(tlist[2], ndict, path=path+["1"])
    if tlist[1] is not None and tlist[2] is not None:
        indexR(tlist[1], ndict, path=path+["0"])
        indexR(tlist[2], ndict, path=path+["1"])
    if tlist[1] is None and tlist[2] is None:
        ndict[tlist[0]] = "".join(path)
def freqList(inputfile): #opens given file and counts frequencies of each character before storing them in a dictionary with key:value as letter:frequency
    filein = open(inputfile, mode="r")
    flist = {}
    for line in filein:
        for char in line:
            if char == "\n":
                pass
            elif char not in flist.keys():
                flist[char] = 1
            else:
                flist[char] = flist[char]+1
    filein.close()
    return flist
#function definition ends, class definition begins
class Encoder(object):
    def __init__(self):
        self.args = getArgs(sys.argv)
    def encode(self, string, tlist): #encodes string using a given tree and returns encoded string
        tdict = {}
        outstr = []
        indexR(tlist, tdict)
        for char in string:
            if char not in tdict.keys():
                outstr.append(char)
            else:
                outstr.append(tdict[char])
        return "".join(outstr)
    def decode(self, string, tlist): #decodes string using a given tree and returns decoded string
        strlist = list(string)
        outstr = []
        while len(strlist) > 0:
            decodeR(strlist, tlist, outstr)
        return "".join(outstr)
    def createTree(self, fdict): #creates tree from a given dictionary with key:value as letter:frequency
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
    def encodeFile(self, inputfile): #encodes given input file and writes to an output file (if given) or creates a new output file
        tree = self.createTree(freqList(self.args["-i"])) 
        fdict = freqList(self.args["-i"])
        fstr = []
        filein = open(inputfile, mode="r")
        if "-o" in self.args.keys(): #checks if output file is given and creates a new file if not
            fileout = open(self.args["-o"], "w")
        else:
            fileout = open("coded-"+self.args["-i"], "w+")
        if self.args["-v"] == "true":
            print("\033[1;4m"+"Frequency List: "+"\033[0m"+str(fdict))
            print("\033[1;4m"+"Huffman Tree: "+"\033[0m"+str(tree))
            print("\033[1;4m"+"Input: "+"\033[0m"+filein.name)
            print("\033[1;4m"+"Output: "+"\033[0m"+fileout.name)
        for key, value in fdict.items(): #takes freqList and stores as header of file
            fstr.append(str(key)+"~"+str(value))
        fileout.write("|".join(fstr)+"\n")
        for line in filein: #encodes file
            fileout.write(self.encode(line, tree))
        print("Encoded "+filein.name+" successfully, wrote output to "+fileout.name+".")
        filein.close()
        fileout.close()
    def decodeFile(self, inputfile): #decodes given input file and writes to an output file (if given) or creates a new output file
        filein = open(inputfile, mode="r")
        filelist = filein.readlines()
        if "-o" in self.args.keys(): #checks if output file is given and creates a new file if not
            fileout = open(self.args["-o"], "w")
        else:
            fileout = open("decoded-"+self.args["-i"], "w+")
        flist = filelist[0].strip("\n").split("|")
        fdict = {}
        for item in flist:
            temp = item.split("~")
            fdict[temp[0]] = temp[1]
        tree = self.createTree(fdict)
        if self.args["-v"] == "true":
            print("\033[1;4m"+"Frequency List: "+"\033[0m"+str(fdict))
            print("\033[1;4m"+"Huffman Tree: "+"\033[0m"+str(tree))
            print("\033[1;4m"+"Input: "+"\033[0m"+filein.name)
            print("\033[1;4m"+"Output: "+"\033[0m"+fileout.name)
        for line in filelist[1:]:
            fileout.write(self.decode(line.strip("\n"), tree)+"\n")
        print("Decoded "+filein.name+" successfully, wrote output to "+fileout.name+".")
        filein.close()
        fileout.close()
# class definition ends, execution begins
encoder = Encoder() #creates instance of Encoder class
if not encoder.args: #prints usage of program if no arguments specified
    print("""USAGE:
      -i <inputfile> | specifies input file for program to use, use .txt files (REQUIRED)
     -o <outputfile> | specifies output file for program to use, use .txt files (OPTIONAL)
  -a <encode/decode> | specifies action for program to take, only accepts encode or decode (REQUIRED)
     -v <true/false> | enables verbose-mode on program for debugging purposes (OPTIONAL)""")
elif encoder.args["-a"] == "encode":#takes action specified by user and encodes or decodes as given, does nothing if input is unexpected
    if '-i' in encoder.args: #checks if user specified input file
        print("Encoding "+encoder.args["-i"]+"with huffman encoding.")
        encoder.encodeFile(encoder.args["-i"])
    else:
        print("No input specified! Please run the program again and specify an input file with -i <inputfile.txt>")
elif encoder.args["-a"] == "decode":
    if '-i' in encoder.args: #checks if user specified input file
        print("Decoding "+encoder.args["-i"]+" with huffman encoding.")
        encoder.decodeFile(encoder.args["-i"])
    else:
        print("No input specified! Please run the program again and specify an input file with -i <inputfile.txt>")
else:
    print("Unexpected action, please specify either encode/decode with -a <encode/decode>")