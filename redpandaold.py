import sys,os,re,platform,subprocess,random

os.system("")

args = sys.argv[1:]
tokens = []
keywords = []
libraries = []
variables = {}
functions = {}
implementedlibraries = []
objects = []

# Begin declaring colors

CEND      = '\33[0m' # Normal colors
CBOLD     = '\33[1m' # Bold
CITALIC   = '\33[3m' # Italic
CURL      = '\33[4m' # URL formatting
CBLINK    = '\33[5m' # Blinking text
CBLINK2   = '\33[6m' # Blinking text, this is faster, but it seems to be the same speed on windows
CSELECTED = '\33[7m' # Highlighted text.

CBLACK  = '\33[30m' # Black text
CRED    = '\33[31m' # Red text
CGREEN  = '\33[32m' # Green text
CYELLOW = '\33[33m' # Yellow text
CBLUE   = '\33[34m' # Blue text
CVIOLET = '\33[35m' # Violet text
CBEIGE  = '\33[36m' # Beige text
CWHITE  = '\33[37m' # White text (may be different from normal text color, depending on settings/terminal)

CBLACKBG  = '\33[40m' # Black background
CREDBG    = '\33[41m' # Red background
CGREENBG  = '\33[42m' # Green background
CYELLOWBG = '\33[43m' # Yellow background
CBLUEBG   = '\33[44m' # Blue background
CVIOLETBG = '\33[45m' # Violet background
CBEIGEBG  = '\33[46m' # Beige background
CWHITEBG  = '\33[47m' # White background

CGREY    = '\33[90m' # Dark gray text
CRED2    = '\33[91m' # Light red text
CGREEN2  = '\33[92m' # Light green text
CYELLOW2 = '\33[93m' # Light yellow text
CBLUE2   = '\33[94m' # Light blue text
CVIOLET2 = '\33[95m' # Light violet text
CBEIGE2  = '\33[96m' # Light beige text (NOT BEIGE IN COMMAND PROMPT)
CWHITE2  = '\33[97m' #'Light' white text, if that makes sense. Don't ask how it works

# End declaring colors

class PythonErrors: # Define errors
    pass

class PandaErrors: # Define custom errors
    class Error:
        def __init__(self,name,details,traceback):
            traceback = traceback
            name = name
            details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class InvalidLibraryError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class InvalidOperatorError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class MissingOperatorError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class BorkenCodeModifError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class InvalidVarTypesError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class MissingVarTypesError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")
    class EOFScanningStrLError:
        def __init__(self,name,details,traceback):
            self.traceback = traceback
            self.name = name
            self.details = details
        def activate(self):
            print(f"{CRED2}{self.traceback}{CEND}")
            print(f"{CRED2}{self.name}: {self.details}{CEND}")

class utils: # Define utilities
    class libraries:
        def isLib(name):
            validLibraries = ["console","numberpanda"]

            named = name.split("\n") # MAKE SURE IT'S ONLY ONE WORD
            check = named[0]

            print(f"To check: \"{check}\"")

            if check in validLibraries: return check
            return None

    def info():
        system = ""
        try:
            if platform.win32_ver:
                system = "win32"
        except:
            try:
                if mac_ver:
                    system = "mac"
            except:
                try:
                    if libc_ver:
                        system = "libc"
                except:
                    system = "undetermined"
        return {"version":"1.0","release":"Pre-Alpha","system":system,"machine":platform.machine()}
    def docs(sub=""):
        try:
            os.system('start docs{0}'.format(sub))

            print("{0}Notice: If you get an error, it's due to a {1} bug.{2}".format(CRED2,bugstatus,CEND))
        except:
            pass
    def shell():
        print(f"Red Panda {utils.info()['release']} {utils.info()['version']} ({utils.info()['machine']}) on a {utils.info()['system']} system")
        print("Type \"help\" to enter the help utility.")
        exitshell = 0
        while not exitshell:
            command = input(f"{CGREY}S {CRED2}>>> {CEND}")
            if command == "exit":
                print("Exit() or CTRL+Z and Return to exit.")
                print(f"{CYELLOW}Warning: an error may occur due to the CTRL+Z, this is a result of python.")
            if command.lower() == "exit()":
                exit()
            if command.lower() == "help":
                utils.help(True)
            if command.lower() == "secretcommand -" + str(random.randint(1,999)):
                print('''
███▓▓▓▓▓▓▓▓╣╢╣╣╣╣╣╣╢╣╣╣╢╢╢╣╢▓▓╣╣╣╢╫▓▓▓▓▓╣▓▓▓▓▓▓▓▓▓▓███▓▓████████████▓▓██████████
█▓▓▓▓▓▓▓▓▓▓░░░╙╙▓▓▓▓▓▓▓▓▓╣╣╢╢▓▓▓╣╣▒▒╢▓▓▓▓▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓████████████████████
▓▓█▓▓▓▓▓▓▒░░░▒░░░░╣╢╢╫▓▓▓╢╢╢╢▓▓▓╣╣╢╣╢╢▒▓▓▓▓▓▓▓▓▓█▀▀▀▀▓▓▓▓▓▓▓████████████████████
▓▓▓▓▓▓▓▓▓▒▒▒▒╬╣▒░░░▓▓╣╢╣╣╢╣▒╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢▒▒░░░░░░░▓▓▓▓█████████████████████
██▓▓▓▓╣╢▓╣▒▒▒╬▓╣▒▒░▒▓▓╣╣╢╫╣╫╣╣╢╣╢╢╣╢╣╢▒╣▒▒▒▒▒▒╫▓▒▒▒▒▒▒▒▒▓▓██████▓███████████████
██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓╣▓╢╢╬╢╢╫╢╢╣╣╣╢╣╢╢╢╣╢╢▒▒╢╢▒╢▓▒▒▒▓██▓▓▓▓▓▓▓▓▓▓▓▓██████████
██████████▒▒░▒▒╢╢▓▓▓▓╢▓╣╣╣╣╣╣▓╢╫╣╣╣╢╣╣╣╣╣╣╣╢╜╨▒▒▒╣▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓██
████▓▓██▓▒▒▒▒▒╢▓▓▓▓▓▓╣▓▓▓╣╫╣╢╣╣▓╣╣▒▒░▒▓▓▓╢▓▓░░╢▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████
████████▓▒▒▒▒╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▒╢▓▓@▓▓▓▓▓▓▓▓▓▒╢╣╣▒▒▒▓▓▓▓███▓█████▓▓█▓▓████████
████████▓╣▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▀▒╢╜╢▒▓█▓▓╣╣╢▒▒▓▓▓███▓████▓▓▓████████████
▓███████▓▒▒╫▓▓▓▓▓▓▓▓▓▓╢▓▓▓▓▒▒╫▓▓▓▓▓▓▓▓▒▒░░░░░░╙▓▓▓▒▒▒╢▓▓▓▓▓▓▓▓▓████▓▓███████████
███╢╢████▓▓█▓╢▓▓█▓▓▓▓▓▓╫▓▒▒▒▓▓████▓▀▒░░░░░░╬▓▓W▒▓▓╣▒╢▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓███████
██▓▓▓▓▓███▓╣╢▓▓▓▓▓▓▓▓▓▓╣▒╢╢▓████▓▓▒▒░░░▒▒▒█████▒╫▓╣▒▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████
██▓▓▓▓▓▓▓╢╢╣▓▓▓▓▓██▓▓▓▓╣╢╢▓▓█████▓▒▒▒▒▒▒▒╢▓▓██▌▒╫▓▓╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓█▓
██▓▓▓▓▓▓╣╣╢▓▓▓▓▓████▓▓╢╣╢╫▓▓▓▓████▓▓▓▓▓▓▓▓▓██▓╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓██████████▓▓▓█
▓█▓▓▓▓▓▓▓╣╣▓▓▓▓▓████▓╣╣╣▓▓████████▓▒▒▓▓╣╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓███████████▓▓▓█
▓█▓▓▓▓▓▓╢▓╣▓▓██████▌▓▓▓▓▓███████▀▒█▓▓██████████▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓████████████▓█
▓██▓▓▓█▓▓▓▓╣██████╢▓▓▓▓███████╣▒███▓▓▓████████▓▓▓█▓▓▓▓▓▓▓▓▓██▓▓▓▓█████▓████▓████
▓██▓███╢▓▓▓▓█████▓▓▓▓▓▓▓▓▓█▓╣▒█████▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓██████▓▓▓▓▓█████
▓█████▓╣▓▓▓▓█████▓▓▓▓▓▓▓▓▓╣╢██████▓▓▓▓▓████▓▓▓▓▓▓╣╢▓▓▓▓▓▓▓▓▓▓▓██▓▓▓██▓▓▓▓▓▓▓▓▓▓█
▓▓██▓█▓╣▓▓▓▓████▓▓▓▓▓▓╢▓▓▓████████▓▓▓▓▓█▀▒▒▒▒▒▓▓▓▓▓╣╢▓▓▓▓▓▓▓█████████▓▓▓▓▓▓▓████
▓▓▓▓███▓▓▓╢▓███╢╣▓▓▓▓╣▓▓████████▓▓▓▓▓╢╢╣▒▓██▓▓██▓▓▓▓▓╣▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓████▓▓
▀▀▀▀▓▀▀▀▓╩╩▀▀▀╩▓▀▀▀▓▓▓█████▀▀▀▓▓▓▀▓▓▓╩▀▀▀▀▀▀▀▀▀▀▀▀▀╩╩▓╩▓▀▀▀▀▓▓▓▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
it changes each time so dont go telling others''')
            if command.lower() == "secretcommand":
                print("i was gonna add ascii art")
                print("but the ascii art didnt look good in command prompt")
                print("i mean, you did find a secret i guess?")
                print("\nRedPanda: \"psst, theres a way to enable the ascii art! can you find it?\"")
    def help(rtrn=False): # Help Utility
        print("Help utility entered.")
        print("Welcome to Red Panda!")
        print("Red panda is a programming language, made for fun.")
        print("")
        while True:
            print("Options:")
            print("[1] Documentation")
            print("[2] Library Reference")
            if rtrn:
                print("[3] Return")
            else:
                print("[3] Exit")
            print("")
            opt = input(f"{CGREY}H {CBLUE2}>>> {CEND}")
            if opt == "1":
                utils.docs("\\index.html")
            elif opt == "2":
                utils.docs("\\library\\index.html")
            elif opt == "3":
                break

class lexer:
    def __init__(self,text):
        self.text = text.replace("\n\n", "\n")
        self.list = list(text.replace("\n\n", "\n"))
        print("Creating analyzed text...")
        self.tokenize()
    def tokenize(self):
        print("Tokenizing...")
        self.stokens = [] # per-char tokens
        self.atokens = [] # per-word tokens
        self.preword = ""
        self.isdialog = False

        for i in self.text:
            self.preword = self.preword + i
            if i == "+":
                self.stokens.append("PLUS") # PLUS
            elif i == "-":
                self.stokens.append("SUBT") # SUBTRACT
            elif i == "*":
                self.stokens.append("MULT") # MULTIPLY
            elif i == "/":
                self.stokens.append("DIVI") # DIVIDE
            elif i == "(":
                self.stokens.append("LPAR") # LEFT PARENTHESIS
            elif i == ")":
                self.stokens.append("RPAR") # RIGHT PARENTHESIS
            elif i == "[":
                self.stokens.append("LSBR") # LEFT SQUARE BRACKET
            elif i == "]":
                self.stokens.append("RSBR") # RIGHT SQUARE BRACKET
            elif i == "{":
                self.stokens.append("LCBR") # LEFT CURLY BRACKET
            elif i == "}":
                self.stokens.append("RCBR") # RIGHT CURLY BRACKET
            elif i == "\"":
                self.stokens.append("DIAG") # DIALOG
                self.isdialog = not self.isdialog
            elif i == " " or i == "\n":
                if i == "\n": self.stokens.append("LNBK") # NEW LINE
                else:         self.stokens.append("WHSP") # WHITESPACE

                # BEGIN TOKENIZING 'ADVANCED' TOKENS



                print(self.preword)

                if i == "\n":
                    print("AAAAAAAAAAAAAAAAAAAA")

                if self.preword.endswith(") ") and not self.isdialog:
                    self.atokens.append(["FUNCTION",self.preword[:-1],self.isdialog])
                elif self.preword == "function " and not self.isdialog:
                    self.atokens.append(["FUNCDECL",self.preword[:-1],self.isdialog])
                elif self.preword == "lib " and not self.isdialog:
                    self.atokens.append(["IMPLMLIB",self.preword[:-1],self.isdialog])
                elif self.preword == "var " and not self.isdialog:
                    self.atokens.append(["BVARDECL",self.preword[:-1],self.isdialog])
                elif self.preword == "int " and not self.isdialog:
                    self.atokens.append(["VARTINTG",self.preword[:-1],self.isdialog])
                elif self.preword == "str " and not self.isdialog:
                    self.atokens.append(["VARTSTRI",self.preword[:-1],self.isdialog])
                elif self.preword == "bool " and not self.isdialog:
                    self.atokens.append(["VARTBOOL",self.preword[:-1],self.isdialog])
                elif self.preword == "float " and not self.isdialog:
                    self.atokens.append(["VARTFLOT",self.preword[:-1],self.isdialog])
                elif self.preword == "res " and not self.isdialog:
                    self.atokens.append(["VARTRESR",self.preword[:-1],self.isdialog])
                elif self.preword in ["= ", "+= ", "-= "] and not self.isdialog:
                    self.atokens.append(["OPERATOR",self.preword[:-1],self.isdialog])
                else:
                    rectokn = False
                    print("Preword: " + str(self.preword[:-1]))
                    try:
                        print(libraries[0])
                    except:
                        print("no libraries")
                    if self.atokens[-1][0] ==  "IMPLMLIB" and not self.isdialog:
                        self.atokens.append(["LIBRNAME",self.preword[:-1],self.isdialog])
                        libraries.append(self.preword[:-1])
                    elif self.atokens[-1][0].startswith("VART") or self.atokens[-1][0].startswith("VARM"):
                        self.atokens.append(["VARINAME",self.preword[:-1],self.isdialog])
                    elif i == "\n":
                        self.atokens.append(["LINEBRAK",self.preword[:-1],self.isdialog])
                    else:
                        self.atokens.append(["NRECTOKN",self.preword[:-1],self.isdialog])

                self.preword = ""

            else:
                self.stokens.append("RFRA") #REFER TO ADVANCED TOKENS

if len(args) < 2:
    if len(args) == 0:
        utils.shell()
        exit()
    else:
        if args[0] == "--help":
            utils.help(False)
            exit()
        else:
            print(CRED2 + "Error (RUNTIME): Not enough arguments given" + CEND)
            exit()

try:
    dl0 = args[0][1]
except IndexError as e:
    print(CRED + "Fatal (RUNTIME) args[0] is too small." + CEND)
    exit()
try:
    dl1 = args[1][1]
except IndexError as e:
    print(CRED + "Fatal (RUNTIME) args[1] is too small." + CEND)
    exit()

duringstatus = "during argument check."
try:
    if args[0][1] == ":":
        if len(args[0]) > 3:
            print(CBLUE2 + "DEBUG: args[0] is valid." + CEND)
            if args[1][1] == ":":
                if len(args[1]) > 3:
                    duringstatus = "while setting up tokenizing process."
                    print(CBLUE2 + "DEBUG: args[1] is valid." + CEND)
                    print("All required arguments are valid.")
                    print("Replacing space codes...")
                    args = [args[0].replace("%20"," "),args[1].replace("%20"," ")]
                    print("Generating tokens...")
                    duringstatus = "while tokenizing."
                    file = open(args[0],"r")

                    text = file.read()

                    file.close()

                    lex = lexer(text)
                    stk = lex.stokens
                    atk = lex.atokens

                    print(stk)
                    print(atk)
                    print(lex.list)
                    print("")
                    arectokens = len(lex.atokens) - lex.atokens.count("NRECTOKN")
                    srectokens = len(lex.stokens) - lex.stokens.count("RFRA")
                    print(f'{arectokens}/{len(lex.atokens)} atokens recognised.')
                    print(f'{srectokens}/{len(lex.stokens)} stokens recognised.')

                    print("Running program...")

                    duringstatus = "while running the program."

                    for i in range(len(lex.atokens)):
                        indexed = lex.atokens[i][0]
                        if indexed == "FUNCDECL":
                            print("it is")
                            print("next: {0}".format(lex.atokens[i+1][1]))
                        if indexed == "BVARDECL":
                            print("start var setting i guess\n")
                            if lex.atokens[i+1][0].startswith("VART"):
                                print(lex.atokens[i+1][1])
                                if lex.atokens[i+1][0] == "VARTSTRI":
                                    print(lex.atokens[i+1][0])
                                    if lex.atokens[i+2][0] == "VARINAME":
                                        print(lex.atokens[i+2][0])
                                        vname = lex.atokens[i+2][1]
                                        if lex.atokens[i+3][0] == "OPERATOR":
                                            print("we're good 4")
                                            if lex.atokens[i+3][1] == "=":
                                                looping = 1
                                                string = ""
                                                del string
                                                string = ""
                                                index = i+3
                                                while looping:
                                                    index += 1
                                                    print(string)
                                                    try:
                                                        if lex.atokens[index][2] == True:
                                                            string = string + " " + lex.atokens[index][1]
                                                        else:
                                                            looping = 0
                                                            string = string + " " + lex.atokens[index][1]
                                                    except:
                                                        PandaErrors.EOFScanningStrLError("EOFScanningStrError","an EOF was encountered while scanning a string.", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()
                                                string = string[1:]
                                                variables[vname] = string
                                                print(f"variable {vname}:{string} set")
                                            else:
                                                PandaErrors.InvalidOperatorError("InvalidOperatorError","an invalid operator was encountered.", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()
                                        else:
                                            PandaErrors.MissingOperatorError("MissingOperatorError","no operator was encountered.", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()
                                    else:
                                        PandaErrors.BorkenCodeModifError("NoVariableNameError","did you modify the code? basically, VARINAME was not found, which is impossible in the original code, therefore you must've modified the code to recieve this error. ANYWAYS, I just wrote this giant block of text just for an error and its still going. I should stop.", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()
                                elif lex.atokens[i+1][0] == "VARTINTG":
                                    if lex.atokens[i+2][0] == "VARINAME":
                                        vname = lex.atokens[i+2][1]
                                        if lex.atokens[i+3][0] == "OPERATOR":
                                            if lex.atokens[i+3][1] == "=":
                                                variables[vname] = int(lex.atokens[i+4][1])
                                elif lex.atokens[i+1][0] == "VARTFLOT":
                                    if lex.atokens[i+2][0] == "VARINAME":
                                        vname = lex.atokens[i+2][1]
                                        if lex.atokens[i+3][0] == "OPERATOR":
                                            if lex.atokens[i+3][1] == "=":
                                                variables[vname] = float(lex.atokens[i+4][1])
                                elif lex.atokens[i+1][0] == "VARTBOOL":
                                    if lex.atokens[i+2][0] == "VARINAME":
                                        vname = lex.atokens[i+2][1]
                                        if lex.atokens[i+3][0] == "OPERATOR":
                                            if lex.atokens[i+3][1] == "=":
                                                variables[vname] = bool(lex.atokens[i+4][1])
                                elif lex.atokens[i+1][0] == "VARTRESR":
                                    if lex.atokens[i+2][0] == "VARINAME":
                                        vname = lex.atokens[i+2][1]
                                        if lex.atokens[i+3][0] == "OPERATOR":
                                            if lex.atokens[i+3][1] == "=":
                                                if lex.atokens[i+4][0] == "IMPLMLIB":
                                                    if utils.libraries.isLib(lex.atokens[i+5][1]):
                                                        implementedlibraries.append([utils.libraries.isLib(lex.atokens[i+5][1]),vname])
                                else:
                                    PandaErrors.InvalidVarTypesError("InvalidVarTypesError",f"an invalid variable type was encountered. ({lex.atokens[index][1]})", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()
                            else:
                                PandaErrors.MissingVarTypesError("MissingVarTypesError","no variable type was encountered", f"{lex.atokens[i][1]} {lex.atokens[i+1][1]} {lex.atokens[i+2][1]} {lex.atokens[i+3][1]} {string}").activate()

                        if indexed == "IMPLMLIB":
                            print("start implementing lib ig\n")
                            print("a: \"" + lex.atokens[i+1][0].split("\n")[0] + "\"")
                            print("b: " + str(i))
                            print("\n")
                            if utils.libraries.isLib(lex.atokens[i+1][1].split("\n")[0]) != None:
                                canimport = True
                                for id in implementedlibraries:
                                    if utils.libraries.isLib(lex.atokens[i+1][1].split("\n")[0]) in id:
                                        canimport = False
                                if canimport: implementedlibraries.append([utils.libraries.isLib(lex.atokens[i+1][1].split("\n")[0]),utils.libraries.isLib(lex.atokens[i+1][1].split("\n")[0])])
                            else:
                                entry = lex.atokens[i+1][1].split("\n")[0]
                                PandaErrors.InvalidLibraryError("InvalidLibraryError",f"\"{entry}\" is an invalid library.", f"index {i} is invalid.").activate()
                        for ia in implementedlibraries:
                            try:
                                if "console" in ia:
                                    print("CANUSECONSOLELIB")
                                    print("importantyes: " + text.split(" ")[i])
                                    print()
                                    textindexed = " ".join(text.split(" ")[i].split("\n")[1:]).split(".")
                                    print("important: ---" + str(textindexed) + "===")
                                    if textindexed[0] == "console":
                                        if textindexed[1] == "log":
                                            if textindexed[2].startswith("print("):
                                                print("AAEAEEAEEEEEEEEEEEEEEE")
                            except Exception as e:
                                print(e)

                    print("Ran program.")
                    print("Libraries: " + str(implementedlibraries))
                    print("Variables: " + str(variables))
                else:
                    print(CRED2 + "Error (RUNTIME): Length of args[1] is not greater than 3." + CEND)
            else:
                print(CRED2 + "Error (RUNTIME): args[1] does not start with a drive letter." + CEND)
        else:
            print(CRED2 + "Error (RUNTIME): Length of args[0] is not greater than 3." + CEND)
    else:
        print(CRED2 + "Error (RUNTIME): args[0] does not start with a drive letter." + CEND)
except Exception as e:
    print(CRED + "Fatal (RUNTIME): Python gave an error " + duringstatus + " Error below." + CEND)
    raise e
