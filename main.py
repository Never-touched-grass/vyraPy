import re
varNames = []
varVals = []
funcNames = []
funcCodes = []
choice = ""
iVar = ""
iVal = ""
iOper = ""
cmd = ""
codeBlock = ""
fName = ""
while cmd != "break":
    cmd = input(">")
    if cmd == "print" :
        cmd = input(":")
        print(cmd)
    elif cmd == "if":
        choice = input("num/var:")
        if choice == "num":
            choice = input("condition:")
            if eval(choice) == True:
                print("true")
            else:
                print("false")
        elif choice == "var":
            iVar = input("condition var:")
            iOper = input("operator:")
            iVal = input("value:")
            for i in range(len(varNames)):
                if varNames[i] == iVar:
                    if iOper == "==":
                        if varVals[i] == iVal:
                           print("true")
                        else:
                            print("false")
                    elif iOper == "!=":
                        if varVals[i] != iVal:
                            print("true")
                        else:
                            print("false")
                    elif iOper == "<":
                        if varVals[i] < iVal:
                            print("true")
                        else:
                            print("false")
                    elif iOper == ">":
                        if varVals[i] > iVal:
                            print("true")
                        else:
                            print("false")
    elif cmd == "var":
        cmd = input("name:")
        varNames.append(cmd)
        cmd = input("value:")
        varVals.append(cmd)
    elif cmd == "func":
        cmd = input("name:")
        funcNames.append(cmd)
        funcCodes.append([])
        while codeBlock != "endFunc":
            codeBlock = input("code:")
            funcCodes[0].append(codeBlock)
    elif cmd == "callFunc":
        fName = input("name:")
        for j in range(len(funcNames)):
            if funcNames[j] == fName:
                for o in range(len(funcCodes[j])): 
                    if funcCodes[j][o].startswith("print "):
                        line = funcCodes[j][o][6:]
                        out = re.findall(r'"(.*?)"', line)
                        print(out[0])
                    elif funcCodes[j][o].startsWith("var "):
                        print("Feature available soon.")
    else:
        print("'" + cmd + "' is not a valid command.")
