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
    class TestingError(Error):
        def __init__(self):
            super().__init__("Fatal","Cookies",CRED2)

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
        return {"version":"0.1.0","release":"-alpha","system":system,"machine":platform.machine()}
    def docs(sub=""):
        try:
            os.system('start docs{0}'.format(sub))

            print("{0}Notice: If you get an error, it's due to a {1} bug.{2}".format(CRED2,bugstatus,CEND))
        except:
            pass
if shell:
    while not quit:
        print(f"Red Panda {utils.info()['version']}{utils.info()['release']} ({utils.info()['machine']}) on a {utils.info()['system']} system")
        print("Type \"help\" to enter the help utility.")
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
