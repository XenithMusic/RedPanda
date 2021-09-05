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
shell = (len(args)==0)
print(shell)
if shell: quit = False

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

class PythonErrors: # Begin defining python related errors
    pass

class PandaErrors: # Begin defining redpanda related errors
    class Error:
        def __init__(self,name,description,color):
            print(color + name + ": " + description + CEND)
            if shell == False:
                exit()
    class TypeError(Error):
        def __init__(self,description):
            super().__init__("InvalidVariable",description,CRED2)

class utils:
    def help(rtrn=False): # Help Utility
        print("Help utility entered.")
        print("Welcome to RedPanda!")
        print("RedPanda is a programming language, made for fun.")
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
        return {"version":"0.1.0","release":"","meta":"","system":system,"machine":platform.machine()}
    def docs(sub=""):
        try:
            os.system('start docs{0}'.format(sub))

            print("{0}Notice: If you get an error, it's due to a {1} bug.{2}".format(CRED2,bugstatus,CEND))
        except:
            pass
if shell:
    print(f"Red Panda {utils.info()['version']}{utils.info()['release']}{utils.info()['meta']} ({utils.info()['machine']}) on a {utils.info()['system']} system")
    print("Type \"help\" to enter the help utility.")
    while not quit:
        cmd = input(CGREY + "S" + CRED2 + " >>> " + CEND)
        cmd = cmd.lower()
        if cmd == "exit":
            print("Exit() or CTRL+Z and Return to exit.")
            print(f"{CYELLOW}Warning: an error may occur due to the CTRL+Z, this is a result of python.")

        # TEMPORARY: Will remove soon in favor of a code interpreter

        if cmd == "exit()":
            exit()

        if cmd == "help":
            utils.help(True)
        if cmd == "secretcommand":
            print("i was gonna add ascii art")
            print("but the ascii art didnt look good in command prompt")
            print("i mean, you did find a secret i guess?")
            print("\nRedPanda: \"psst, theres a way to enable the ascii art! but i've heard it changes often... can you find it?\"")
        if cmd == "secretcommand -" + str(random.randint(1,999)):
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
else:
    print(args)
    path = args[0]
    if path.startswith("C:\\") or path.startswith("./"):
        file = open(path,'r')
        data = file.read().split(' ')
        text = []
        for i in range(len(data)):
            apnd = (data[i].split('\n'))
            text = text + apnd
        file.close()
        print("Running deep scan...")
        i = 0
        while i < len(text):
            if text[i].lower() == "function":
                i += 1
                functions[text[i][:-1]] = i
            i += 1
        i = 0
        print("Deep scan complete.")
        rundisableon = "{"
        runenableon  = "}"
        while i < len(text):
            current = text[i]
            print("{0}: {1}".format(i,text[i]))
            if current == "lib":
                i += 1
                if text[i] in ["console","system","math"]:
                    libraries.append(text[i])
            elif current == "var":
                i += 1
                print("var")
                if text[i] in ["res","str","int","float","bool"]:
                    print("variabletype")
                    type = text[i]
                    i += 1
                    name = text[i]
                    i += 1
                    if text[i] == "=":
                        print("operator")
                        ststr = True
                        cstr = ""
                        i += 1
                        print("next print should be:\n{0}".format(type))
                        if type == "str":
                            print(type)
                            while ststr:
                                if text[i].endswith("\""):
                                    ststr = False
                                cstr = cstr + " " + text[i]
                                i += 1
                            cstr = cstr[:-1]
                            variables[name] = cstr
                        if type == "bool":
                            if text[i] == "true":
                                variables[name] = True
                            elif text[i] == "false":
                                variables[name] = False
                            else:
                                PandaErrors.TypeError("Expected boolean at location " + str(i))
                        if type == "float":
                            print("its a float")
                            if float(text[i]) != round(float(text[i])):
                                variables[name] = float(text[i])
                            else:
                                PandaErrors.TypeError("Expected float at location " + str(i))
                        if type == "int":
                            print("its an integer")
                            try:
                                variables[name] = int(text[i])
                            except:
                                PandaErrors.TypeError("Expected integer at location " + str(i))
            else:
                i += 1
        print("\n\n\nVariables: {0}\nFunctions: {1}\nLibraries:{2}".format(variables,functions,libraries))
