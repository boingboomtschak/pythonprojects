from sys import argv
def getArgs (argv): #defines function to add -[letter] [input] pairs into dictionary
    args = {}
    while argv:
        if argv[0][0] == "-":
            args[argv[0]] = argv[1]
        argv = argv[1:]
    return args
myArgs = getArgs(argv)
if "-c" in myArgs.keys():
    if "-i" in myArgs.keys(): #checks basic usage of -c and -i and then runs main script
        codefile = open(myArgs["-c"], "r")
        code = {}
        for line in codefile: #parses code file and offloads information into dictionary "code"
            (key, val) = line.split(":")
            code[str(key)] = str(val).rstrip("\n") #adds code key:value pairs to dictionary and removes line breaks
        codefile.close()
        inputfile = open(myArgs["-i"], "r")
        if "-o" in myArgs.keys(): #checks if output file is specified and creates new file if not
            outputfile = open(myArgs["-o"], "w")
        else:
            outputfile = open("coded-"+myArgs["-i"], "w+")
        for line in inputfile: #goes through each line in input file and parses it with the code file, then writes it to the output file
            thisline = []
            for char in line:
                if char.lower() not in code.keys(): #if the character is not declared in the code file, the program writes it as is instead of throwing an error
                    thisline.append(str(char))
                else:
                    thisline.append(code[str(char).lower()]) 
            if "end" not in code: #searches for the "end" character, used at the end of each letter to separate letters
                outputfile.write("".join(thisline)) 
            else:
                outputfile.write(code["end"].join(thisline))
        print("Encoded "+myArgs["-i"]+" with "+myArgs["-c"]+" and wrote output to "+outputfile.name)
    else:
        print("Specify an input file with -i and run the script again.")
else:
    print ("Specify a code file with -c and run the script again.")
