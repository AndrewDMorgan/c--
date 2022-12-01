""" code syntax:

< >           gets memory (is all global)
=             assignment
+             adds
-             subtracts
*             multiplies
call          calls a function
func          creates a func
jmp           jumps to a line
retrn         returns to last jump
end           ends the program

<1000>        print function
<999>         print function arg input

"""

# sets the line
line = 0  # starting the on first line
jmpBack = []  # the list of values from jumps to jump back to from retrns
def SetLine(newLine: int) -> None:
    global line
    line = newLine

# the memory including funcs and different types of variables (all stored as ints)
memory = {
    1000: lambda : print(memory[999])
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


# Gets the tokens
def GetTokens(codeLine: str) -> list:
    return codeLine.split(" ")

# breaking the code into tokens
tokenizedCode = [GetTokens(codeLine) for codeLine in code]


# gets the adress
def GetAdd(memAdd: str) -> int:
    return memAdd[:-1][1:]


# gets the value of an addres or number
def GetVal(addresVal: int) -> int:
    if addresVal[0] == "<":
        return memory[int(GetAdd(addresVal))]
    return int(addresVal)


# computes the math using recursion and also the substitution of memory values in <address>
def ComputeMath(codeLine: list) -> str:
    # looping through the tokens
    for charNum, token in enumerate(codeLine):
        # reading the syntax
        
        # checking for math (read left to right, no PANDOS)
        if token in ["+", "-", "*"]:
            #value = eval(f"{memory[GetAdd(codeLine[charNum - 1])]} {token} {memory[GetAdd(codeLine[charNum + 1])]}")
            value = eval(f"{GetVal(codeLine[charNum - 1])} {token} {GetVal(codeLine[charNum + 1])}")
            
            # removing the old values
            del codeLine[charNum - 1]
            del codeLine[charNum - 1]
            
            # adding the new value in a simplifyed form
            codeLine[charNum - 1] = str(value)
            
            # formating beyon here
            return ComputeMath(codeLine)
        elif token[0] == "<" and int(GetAdd(token)) in memory and codeLine[0] != "call" and codeLine[min(charNum + 1, len(codeLine) - 1)] != "=":
            codeLine[charNum] = str(memory[int(GetAdd(token))])
            return ComputeMath(codeLine)
    return codeLine


# computes the setting of memory
def ComputeMem(codeLine: list, lineNum: int) -> None:
    global line
    # looping through the simplifyed tokens
    for charNum, token in enumerate(codeLine):
        # checking for memory being set
        if token == "=":
            add = int(GetAdd(codeLine[charNum - 1]))
            if codeLine[charNum + 1] == "func":
                memory[add] = lambda : SetLine(lineNum)  # setting that to call the line its on
                # jumping to the end of the function
                while "retrn" not in tokenizedCode[line]:
                    line += 1
                line += 1  # going to the line after the retrn
            else:
                memory[add] = int(codeLine[charNum + 1])


# running other syntaxes
def RunOther(codeLine: list) -> None:
    global line
    # looping through the simplifyed tokens
    for charNum, token in enumerate(codeLine):
        if token == "call":
            # getting the address
            add = int(GetAdd(codeLine[charNum + 1]))

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


# running the code
codeLine = tokenizedCode[line].copy()
while "end" not in codeLine:
    codeLine = tokenizedCode[line].copy()
    # making sure there is code and its not blank
    if codeLine[0] != "":
        # doing the math
        mathComputed = ComputeMath(codeLine)  # computing math and filling in memory places
        ComputeMem(mathComputed, line)  # setting memory
        RunOther(mathComputed)  # running other syntaxes
    line += 1  # moving the line along


