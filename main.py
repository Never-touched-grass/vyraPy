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
        if cmd != "access":
            print(cmd)
        elif cmd == "access":
            cmd = input("name:")
            for l in range(len(varNames)):
                if varNames[l] == cmd:
                    print(varVals[l])
                else:
                    print("var '" + cmd + "' doesn't exist.")
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
        cmd = input("condition:")
        parts = cmd.split()
        for k in range(len(varNames)):
            if varNames[k] == parts[0]:
                if parts[1] == "!=":
                    try: 
                            while varVals[k] != int(parts[2]):
                                print("Hello")
                                varVals[k] = int(varVals[k])
                                varVals[k] += 1
                            varVals[k] = str(varVals[k])
                    except ValueError:
                        print("ERROR: var '" + varNames[k] + "' is not an integer or floating point.")
    else:
        print("'" + cmd + "' is not a valid command.")
