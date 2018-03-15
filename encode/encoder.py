import sys
def getArgs (argv): #defines function to add -[letter] [input] pairs into dictionary
    args = {}
    while argv:
        if argv[0][0] == "-":
            args[argv[0]] = argv[1]
        argv = argv[1:]
    return args
class Encoder(object):
    def __init__(self):
        self.args = getArgs(sys.argv)
    def encode(self):
        if "-i" in self.args.keys(): #checks basic usage of -i to specify input file
            inputfile = open(self.args["-i"], "r")
            if "-o" in self.args.keys():#checks if output file is specified and creates new file if not
                outputfile = open(self.args["-o"], "w")
            else:
                outputfile = open("coded-"+self.args["-i"], "w+")
            for line in inputfile: #goes through each character in input file (line by line) and translates it into code if specified in the code dictionary
                thisline = []
                for char in line:
                    if char.lower() not in self.code.keys():
                        thisline.append(str(char))
                    else:
                        thisline.append(self.code[str(char).lower()]) 
                if "end" not in self.code:
                    outputfile.write("".join(thisline))
                else:
                    outputfile.write(self.code["end"].join(thisline))
            print("Encoded "+self.args["-i"]+" with "+self.args["-c"]+" and wrote output to "+outputfile.name) #prints used input/code files and result file
        else:
            print("Specify an input file with '-i' and run the script again.")
            sys.exit()
    def decode(self):
        if "-i" in self.args.keys():
            inputfile = open(self.args["-i"], "r")
            if "-o" in self.args.keys():
                outputfile = open(self.args["-o"], "w")
            else:
                outputfile = open("coded-"+self.args["-i"], "w+")
            for line in inputfile:
                if "end" not in self.code:
                    inline = list(line)
                else:
                    inline = line.split(self.code["end"])
                outline = []
                for item in inline:
                    if item.lower() not in self.rcode.keys():
                        outline.append(str(item))
                    else:
                        outline.append(self.rcode[str(item).lower()])
                outputfile.write("".join(outline))
            print("Decoded "+self.args["-i"]+" with "+self.args["-c"]+" and wrote output to "+outputfile.name)     
        else:
            print("Specify an input file with '-i' and run the script again.")
    def definecode(self):
        if "-c" in self.args: #checks basic usage of -c to specify code file
            codefile = open(self.args["-c"], "r")
            self.code = {}
            for line in codefile: #parses code file and offloads information into dictionary "code"
                (key, val) = line.split(":")
                self.code[str(key)] = str(val).rstrip("\n")
            codefile.close()
            self.rcode = dict([v,k] for k,v in self.code.items())
        else:
            print("Specify a code file with '-c' and run the script again.")
            sys.exit()
encoder = Encoder()
encoder.definecode()
if "-a" in encoder.args.keys():
    if encoder.args["-a"] == "e":
        encoder.encode()
    elif encoder.args["-a"] == "d":
        encoder.decode()
    else:
        print("Unknown action! Specify an action ('e' or 'd') for the encoder with '-a' and try again")
else:
    print("Specify an action for the encoder with '-a' and try again.")
