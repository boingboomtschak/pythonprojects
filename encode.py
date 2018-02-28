from sys import argv
def getArgs (argv): #defines function to add -[letter] [input] pairs into dictionary
    args = {}
    while argv:
        if argv[0][0] == "-":
            args[argv[0]] = argv[1]
        argv = argv[1:]
    return args
myArgs = getArgs(argv)
print (myArgs) #debug
print (myArgs["-c"])
if "-c" in myArgs.keys():
    if "-i" in myArgs.keys(): #checks basic usage of -c and -i and then runs main script
        codefile = open(myArgs["-c"], "r")
        code = {}
        for line in codefile: #parses code file and offloads information into dictionary "code"
            (key, val) = line.split(":")
            code[str(key)] = str(val).rstrip("\n")
        codefile.close()
        inputfile = open(myArgs["-i"], "r")
        if "-o" in myArgs.keys(): #checks if output file is specified and creates new file if not
            outputfile = open(myArgs["-o"], "w")
        else:
            outputfile = open("coded-"+myArgs["-i"], "w+")
        for line in inputfile:
            thisline = []
            for char in line:
                if char == "\n":
                    pass
                elif char == " ":
                    thisline.append("/")
                else:
                    thisline.append(code[str(char).lower()])
            outputfile.write(' '.join(thisline))
    else:
        print("Specify an input file with -i and run the script again.")
else:
    print ("Specify a code file with -c and run the script again.")