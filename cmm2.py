import time

""" code syntax:
< >           gets memory (is all global)
=             assignment
+             adds
-             subtracts
*             multiplies
==            ==
>=            >=
>             >
<             <
<=            <=
and           and
or            or
not           not
call          calls a function
func          creates a func
jmp           jumps to a line
retrn         returns to last jump
end           ends the program
done          ends an if
if            an if statement
<print>        print function
<sleep>        sleep function (milliseconds)
<995-999>     parameters for built-ins (in order from 995 - 999)
"""

# sets the line
line = 0  # starting the on first line
jmpBack = []  # the list of values from jumps to jump back to from retrns
def SetLine(newLine: int) -> None:
    global line
    line = newLine


# the memory including funcs and different types of variables (all stored as ints)
memory = {
    "print": lambda : print(memory["995"]),
    "sleep": lambda : time.sleep(memory["995"]*0.001)
}


# opening the code
codeLinesOld = open(input("Program File >> ")).read().split("\n")

# getting the code in a better formated way
code = []
# looping through the lines and processing them
for l in codeLinesOld:
    # remvoing comments
    text = l.split("//")[0]
   
    # checking if the line is empty
    if text != "":
        # removing indentation
        while text != "" and text[0] == " ":
            text = text[1:]
        
        if text != "":
            # removing end spaces
            while text[len(text)-1] == " ":
                text = text[:-1]

    # adding the line
    code.append(text)

# breaking the code into tokens
tokenizedCode = [codeLine.split(" ") for codeLine in code]


# gets the adress
def GetAdd(memAdd: str) -> int:
    return memAdd[:-1][1:]


# gets the value of an addres or number
def GetVal(addresVal: int) -> int:
    if addresVal[0] == "<":
        return memory[GetAdd(addresVal)]
    return int(addresVal)


# computes the math using recursion and also the substitution of memory values in <address>
def ComputeMath(codeLine: list) -> str:
    # looping through the tokens
    for charNum, token in enumerate(codeLine):
        # reading the syntax
        
        # checking for math & logic (read left to right, no PANDOS)
        if token in ["+", "-", "*", "==", ">", "<", "<=", ">="]:
            value = eval(f"{GetVal(codeLine[charNum - 1])} {token} {GetVal(codeLine[charNum + 1])}")
            
            # removing the old values
            del codeLine[charNum - 1]
            del codeLine[charNum - 1]
            
            # adding the new value in a simplifyed form
            codeLine[charNum - 1] = str(value)
            
            # formating beyon here
            return ComputeMath(codeLine)
        # checking for memory and subsituting in for it
        elif len(token) > 2 and token[0] == "<" and GetAdd(token) in memory and codeLine[0] != "call" and codeLine[min(charNum + 1, len(codeLine) - 1)] != "=":
            codeLine[charNum] = str(memory[GetAdd(token)])
            return ComputeMath(codeLine)

    # returning the value after evaluating and's, or's, and not's    
    return RunChecks(codeLine)


# runs checks on and's, or's, and not's
def RunChecks(codeLine: list) -> list:
    # running through ands and ors
    for charNum, token in enumerate(codeLine):
        # checking for the proper tokens
        if token in ["and", "or"]:
            value = eval(f"{GetVal(codeLine[charNum - 1])} {token} {GetVal(codeLine[charNum + 1])}")
            
            # removing the old values
            del codeLine[charNum - 1]
            del codeLine[charNum - 1]
            
            # adding the new value in a simplifyed form
            codeLine[charNum - 1] = str(value)
            
            # formating beyon here
            return RunChecks(codeLine)
        elif token == "not":
            value = eval(f"{token} {GetVal(codeLine[charNum + 1])}")
            
            # removing the old values
            del codeLine[charNum]
            
            # adding the new value in a simplifyed form
            codeLine[charNum] = str(value)
            
            # formating beyon here
            return RunChecks(codeLine)
    
    # finishing the process
    return codeLine


# computes the setting of memory
def ComputeMem(codeLine: list, lineNum: int) -> None:
    global line
    # looping through the simplifyed tokens
    for charNum, token in enumerate(codeLine):
        # checking for memory being set
        if token == "=":
            add = GetAdd(codeLine[charNum - 1])
            if codeLine[charNum + 1] == "func":
                # setting that address to a jmp call to the current line
                memory[add] = lambda : SetLine(lineNum)
                
                # jumping to the end of the function
                exited = 1
                while exited > 0:
                    line += 1
                    if "retrn" in tokenizedCode[line]:
                        exited -= 1
                    elif "func" in tokenizedCode[line]:
                        exited += 1
                
                # going to the line after the retrn
                line += 1
            else:
                memory[add] = int(codeLine[charNum + 1])
        elif token == "if":
            # checking if the if is false
            if not eval(codeLine[charNum + 1]):
                # jumping to the end of the if so its not run
                exited = 1
                while exited > 0:
                    line += 1
                    if "done" in tokenizedCode[line]:
                        exited -= 1
                    elif "if" in tokenizedCode[line]:
                        exited += 1
                
                # going to the line after the done
                line += 1


# running other syntaxes
def RunOther(codeLine: list) -> None:
    global line
    # looping through the simplifyed tokens
    for charNum, token in enumerate(codeLine):
        if token == "call":
            # getting the address
            add = GetAdd(codeLine[charNum + 1])

            # making sure the function isnt a built in one
            if add not in [1000]:
                # adding the line to the jumps list
                jmpBack.append(line)

            # call the function (going to the index unless its a built in)
            memory[add]()
        elif token == "retrn":
            # jumping back to the last jump
            length = len(jmpBack) - 1
            line = jmpBack[length]
            del jmpBack[length]
        elif token == "jmp":  # jumping lines
            line = int(codeLine[charNum + 1]) - 2


# running the code
codeLine = tokenizedCode[line].copy()
while "end" not in codeLine:
    try:
        codeLine = tokenizedCode[line].copy()
        # making sure there is code and its not blank
        if codeLine[0] != "":
            # doing the math
            mathComputed = ComputeMath(codeLine)  # computing math and filling in memory places
            ComputeMem(mathComputed, line)  # setting memory
            RunOther(mathComputed)  # running other syntaxes
        line += 1  # moving the line along
    
    # error handling
    except KeyError:  # memory errors
        raise BaseException(f"\n\n\nPossible memory error\nLiklely that the memory accessed was not created\nError on line { line + 1 }\n{ codeLinesOld[line] }\n\n")
    except BaseException:  # syntax and other errors
        raise BaseException(f"\n\n\n\nPossilbe syntax error\nError on line { line + 1 }\n{ codeLinesOld[line] }\n\n")


