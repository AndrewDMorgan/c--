import time

mem = {}
line = 0
active = None


def Set(add: int, val: any):
    global mem
    mem[add] = val

def SetLine(l: int):
    global line
    line = int(l)-1  # accounting for the movement of the processor

def SetAct(val: any) -> None:
    global active
    active = val

def SetList(add, i, item) -> None:
    mem[add][i] = item


def Int(val) -> any:
    try:
        return int(val)
    except ValueError:
        return val


funcs = {
    "print": lambda txt: print(txt, end=''),
    "printl": lambda txt: print(txt),
    "set": lambda add, val: Set(Int(add), Int(val)),
    "setAdd": lambda add, add2: Set(Int(add), Int(mem[Int(add2)])),
    "get": lambda add: SetAct(Int(mem[Int(add)])),
    "goto": lambda l: SetLine(l),
    "<" : lambda addL, addR: int(mem[Int(addL)]) <  int(mem[Int(addR)]),
    ">" : lambda addL, addR: int(mem[Int(addL)]) >  int(mem[Int(addR)]),
    "==": lambda addL, addR: Int(mem[Int(addL)]) == Int(mem[Int(addR)]),
    "!=": lambda addL, addR: Int(mem[Int(addL)]) != Int(mem[Int(addR)]),
    "<=": lambda addL, addR: int(mem[Int(addL)]) <= int(mem[Int(addR)]),
    ">=": lambda addL, addR: int(mem[Int(addL)]) >= int(mem[Int(addR)]),
    "++": lambda add: Set(add, int(mem[Int(add)]) + 1),
    "--": lambda add: Set(add, int(mem[Int(add)]) - 1),
    "+=": lambda add, add2: Set(Int(add), int(mem[Int(add)]) + int(mem[Int(add2)])),
    "-=": lambda add, add2: Set(Int(add), int(mem[Int(add)]) - int(mem[Int(add2)])),
    "*=": lambda add, add2: Set(Int(add), int(mem[Int(add)]) * int(mem[Int(add2)])),
    "in": lambda add: Set(Int(add), input(">> ")),
    "newList": lambda name: Set(Int(name), []),
    "getItem": lambda name, index: SetAct(mem[Int(name)][Int(index)]),
    "addItem": lambda name, item: mem[Int(name)].append(Int(item)),
    "getSize": lambda name: SetAct(len(mem[Int(name)])),
    "setItem": lambda name, index, item: SetList(Int(name), Int(index), mem[Int(item)])
}

"""
commands:

active is the active value (so "get" will set to active)
to use active in a print do: print active    without any other text, same for set

general:

set    [address] [value]      sets the value at the adress to the value inputed
setAdd [address] [address]    sets the value at the adress to the value at the address
get    [address]              sets "active" to the value (put active in code to acess)
goto   [line]                 jumps to the line
in     [address]              assigns the inputted value (by the usr) to the address
print  [text]                 prints a line of text (can be multiple words but to use active just put active)
printl [text]                 same as print but adds a return (helpful for when using active)

lists

newList [address]                   creates a new list
addItem [address] [item]            adds an item
setItem [address] [index] [add 2]   sets an item at an index
getItme [address] [index]           gets the item at the index
getSize [address]                   gets the size of the item

comparing:

<  [address 1] [address 2]     checks address 1 <  address 2, next line skipped if false
>  [address 1] [address 2]     checks address 1 >  address 2, next line skipped if false
== [address 1] [address 2]     checks address 1 == address 2, next line skipped if false
!= [address 1] [address 2]     checks address 1 != address 2, next line skipped if false
<= [address 1] [address 2]     checks address 1 <= address 2, next line skipped if false
>= [address 1] [address 2]     checks address 1 >= address 2, next line skipped if false
++ [address 1]                 adds 1 to the value at the address
-- [address 1]                 subs 1 from the value at the address
+= [address 1] [address 2]     adds the value at address 2 to the value at address 1
-= [address 1] [address 2]     subs the value at address 2 from the value at address 1
*= [address 1] [address 2]     mults the value at address 1 and 2 together

"""



"""

// character setup with a check for it being called mom

set 2 mom

printl name:
in 0
printl age:
in 1

== 0 2
    goto 14

get 0
print The characters name is 
printl active

get 1
print The characters health is 
printl active

goto 15

printl hi mom!!


// moving a character based on command until the player types done

set x 0  // the x
set completeAction done
set leftAction l
set rightAction r
set maxRight 10

printl action (l/r, done)
in input
== input completeAction
    goto 1000  // leaving the loop
== input leftAction
    -- x  // moving left
== input rightAction
    ++ x  // moving right


set i -1

++ i
print   
< i x
    goto 14

get x
set i active

print []

++ i
print   
< i maxRight
    goto 21

printl

goto 4  // looping


// list like something

set i 0
set maxDepth 1000

++ i
get i
setAdd active i

get active
printl active

< i maxDepth
    goto 2



// math thing

set add +
set sub -
set mult *

printl first value
in 1
printl second value
in 2
printl +, -, or *
in input
== input add
    += 1 2
== input sub
    -= 1 2
== input mult
    *= 1 2

get 1
print Output: 
printl active


"""

# the tokens, a token is a token name + the args in a tuple
tokens = []

# the code
print("code >> ", end='')
i = input()
code = open(i).read()

#code = []
#code = ["set add +", "set sub -", "set mult *", "printl first value", "in 1", "printl second value", "in 2", "printl +, -, *", "in input", "== input add", "+= 1 2", "== input sub", "-= 1 2", "== input mult", "*= 1 2", "get 1", "print Output: ", "printl active"]
#code = ["set 2 mom", "printl name:", "in 0", "printl age:", "in 1", "== 0 2", "goto 14", "get 0", "print The characters name is ", "printl active", "get 1", "print The characters health is ", "printl active", "goto 15", "printl Hi mom!!!"]
#code = ["set 0 0", "set 10 done", "set 11 l", "set 12 r", "printl action (l/r, done)", "in 1", "== 1 10", "goto 10000", "== 11 1", "-- 0", "== 12 1", "++ 0", "get 0", "printl active", "goto 4"]
#code = ["set x 0", "set completeAction done", "set leftAction l", "set rightAction r", "set maxRight 10", "printl action (l/r, done)", "in input", "== input completeAction", "goto 1000", "== input leftAction", "-- x", "== input rightAction", "++ x", "set i -1", "++ i", "print   ", "< i x", "goto 14", "get x", "set i active", "print []", "++ i", "print   ", "< i maxRight", "goto 21", "printl", "goto 4"]
#code = ["set i 0", "set maxDepth 1000", "++ i", "get i", "setAdd active i", "get active", "printl active", "< i maxDepth", "goto 2"]

# running the code
def Runner(codeLine: str) -> None:
    global line
    try:
        # breaking the line into the command and args
        oLine = codeLine
        com, *args = codeLine.split(" ")

        # replacing args of active with the value of active
        for i in range(len(args)):
            if args[i] == "active":
                args[i] = active

        # checking if the command is a print or something else
        if com == "print":
            text = oLine[6:]
            if text == "active":
                text = active
            funcs[com](text)
        elif com == "printl":
            text = oLine[7:]
            if text == "active":
                text = active
            funcs[com](text)
        else:
            # running the command
            valid = funcs[com](*args)
            if not valid and valid != None:
                line += 1
    except Exception:
        print(f"\nError on line {line}\n{codeLines[line]}")
        raise


# breaking the code into lines
codeLinesOld = code.split("\n")
codeLines = []
for l in codeLinesOld:
    text = l.split("//")[0]
    if text != "":
        while text[0] == " ":
            text = text[1:]
        
        if text[:5] != "print":
            while text[len(text)-1] == " ":
                text = text[:-1]

        codeLines.append(text)

# running the code
start = time.time()
while line < len(codeLines):
    Runner(codeLines[line])
    line += 1

end = time.time()
print(f"\nCompleted in {end - start} seconds")

