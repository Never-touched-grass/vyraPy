import re
def easterEgg(egg):
    if egg != "cheex":
        cmd = input("If your happy and you know it:")
        if cmd == "clap your hands!":
            print("Your one lucky finder!")
    elif egg == "cheex":
        print("Clap em'")
ln = ""
code = ""
varNames = []
varVals = []
funcNames = []
funcCodes = []
wCodes = []
choice = ""
iVar = ""
iVal = ""
iOper = ""
cmd = ""
codeBlock = ""
fName = ""
eChoice = ""

while cmd != "break":
    cmd = input(">")

    if cmd == "print":
        cmd = input(":")
        if cmd != "access":
            print(cmd)
        elif cmd == "access":
            cmd = input("name:")
            for l in range(len(varNames)):
                if varNames[l] == cmd:
                    print(varVals[l])
                else:
                    print(f"var '{cmd}' doesn't exist.")

    elif cmd == "if":
        choice = input("num/var:")
        if choice == "num":
            choice = input("condition:")
            if eval(choice):
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
                        print("true" if varVals[i] == iVal else "false")
                    elif iOper == "!=":
                        print("true" if varVals[i] != iVal else "false")
                    elif iOper == "<":
                        print("true" if varVals[i] < iVal else "false")
                    elif iOper == ">":
                        print("true" if varVals[i] > iVal else "false")

    elif cmd == "var":
        cmd = input("name:")
        varNames.append(cmd)
        cmd = input("value:")
        varVals.append(cmd)

    elif cmd == "func":
        cmd = input("name:")
        funcNames.append(cmd)
        funcCodes.append([])
        while True:
            codeBlock = input("code:")
            if codeBlock == "endFunc":
                break
            funcCodes[-1].append(codeBlock)

    elif cmd == "callFunc":
        fName = input("name:")
        for j in range(len(funcNames)):
            if funcNames[j] == fName:
                for o in range(len(funcCodes[j])):
                    if funcCodes[j][o].startswith("print "):
                        line = funcCodes[j][o][6:]
                        out = re.findall(r'"(.*?)"', line)
                        print(out[0])
                    elif funcCodes[j][o].startswith("var "):
                        parts = funcCodes[j][o].split("=")
                        if len(parts) == 2:
                            varNames.append(parts[0].replace("var ", "").strip())
                            varVals.append(parts[1].strip())
                    elif funcCodes[j][o].startswith("printf access "):
                        vName = funcCodes[j][o].split(" ", 2)[-1]
                        if vName in varNames:
                            index = varNames.index(vName)
                            print(varVals[index])
                        else:
                            print(f"var '{vName}' doesn't exist.")

    elif cmd == "while":
        cond = input("condition:")
        parts = cond.split()
        for k in range(len(varNames)):
            if varNames[k] == parts[0]:
                try:
                    varVals[k] = int(varVals[k])
                    lp_bd = []
                    while True:
                        code = input("code:")
                        if code == "end":
                            break
                        lp_bd.append(code)
                    while eval(f"{varVals[k]} {parts[1]} {parts[2]}"):
                        for cl in lp_bd:
                            if cl.startswith("print "):
                                t = re.findall(r'"(.*?)"', cl)
                                print(t[0])
                            elif cl.startswith("callFunc "):
                                fPrts = cl.split()
                                for j in range(len(funcNames)):
                                    if funcNames[j] == fPrts[1]:
                                        for o in range(len(funcCodes[j])):
                                            if funcCodes[j][o].startswith("print "):
                                                fLine = funcCodes[j][o][6:]
                                                fOut = re.findall(r'"(.*?)"', fLine)
                                                print(fOut[0])
                                            elif funcCodes[j][o].startswith("var "):
                                                vParts = funcCodes[j][o].split("=")
                                                if len(vParts) == 2:
                                                    varNames.append(parts[0].replace("var ", "").strip())
                                                    varVals.append(parts[1].strip())
                                            elif funcCodes[j][o].startswith("printf access"):
                                                fvName = funcCodes[j][o].split(" ", 2)[-1]
                                                if fvName in varNames:
                                                    inx = varNames.index(fvName)
                                                    print(varVals[inx])
                                                else:
                                                    print(f"'{fvName}' doenst exist.")
                        varVals[k] += 1
                    varVals[k] = str(varVals[k])
                except ValueError:
                    print(f"ERROR: var '{varNames[k]}' is not an integer or floating point.")

    elif cmd == "edit":
        eChoice = input("func/var:")
        if eChoice == "var":
            eChoice = input("name:")
            for h in range(len(varNames)):
                if varNames[h] == eChoice:
                    newVal = input("new val:")
                    varVals[h] = newVal
        elif eChoice == "func":
            eChoice = input("name:")
            for n in range(len(funcNames)):
                if funcNames[n] == eChoice:
                    funcCodes[n].clear()
                    while True:
                        codeBlock = input("code:")
                        if codeBlock == "endFunc":
                            break
                        funcCodes[-1].append(codeBlock)
    elif cmd == "src":
        print("You are currently interacting with the source code.")
        print("varNames: list of variables you have created.")
        print("varVals: list of values for variables you have created.")
        print("cmd: the command.")
        print("wCodes: list of all lines added to while statements.")
        print("iVar, iOper, iVal: if statement variable, operator, and value.")
        print("funcCodes: list of lines entered into functions.")
        print("funcNames: list of function names.")
        print("These are the items with the major functions.")
        print("You must have a basic understanding of Python syntax to interact with source code.")
        print("Type 'end' to end the program.")
        while True:
            ln = input(":")
            if ln == "end":
                break
            try:
                eval(ln)
            except SyntaxError:
                print("ERROR!: Invalid statement.")
    else:
        print("'" + cmd + "' is not a valid command.")
