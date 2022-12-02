# c-- V2
c-- is a very interesting language. Like how c++ means c but 1 better, c-- means c but a lot worse. It's an interpreted language using multiple layers of proccesing. The commands are bellow, be warned, you brain will hurt a lot. This is a joke langauge just for fun but try to use it if you want. Run the program and input the file. There is next to no error detection in the code while running and there are probably many bugs.

# Features

The language uses new lines to identify the ends of lines (like python). It does not use indentation or brakets (although indents can help readibility), instead it uses syntaxes to mark the end of if's and functions. The language only supports int's currently. You use <> and a number to represent functions and values (when using no <> its marked as a number).

 * Basic variables
 * Functions + recurrsion
 * If's and logic (standered with or, and, not, >=, ect...)
 * Jumps to jump lines
 * Comments
 * Basic math (no order of operations)
 * Brain damage of course too

# Functions

## Built-ins
 - <995> to <999> are for built-in parameters (995 being the first param)
 - <1000> print function
 - <1001> sleep function (milleseconds)

## Math & Logic
 - *, -, +
 - ==, >=, <=, <, >
 - not, and, or
 - if

## Other
 - = assignment
 - call calls a function
 - func creats a function (<0> = func)
 - jmp jumps to a line
 - retrn returns from a function (defining its bounds)
 - end ends the program
 - done marks the end of an if

# Future

Note sure what will become of this to be honest. I might work on a basic ide/text editor with syntax highlighting for c-- V2 just to make it slightly more readable, I currently have a really bad terminal based one although a more graphical one would be nice (It's as easy to exit rn as vim).



# c-- V1
c-- is a very interesting language. Like how c++ means c but 1 better, c-- means c but a lot worse. It's an interpreted language that works by turning all syntaxes into built in functions with a strict layout of parameters. The commands are bellow, be warned, you brain will hurt a lot. This is a joke langauge just for fun but try to use it if you want. Run the program and input the file (be careful, you can't use \n). There is next to no error detection in the code while running and there are probably many bugs.

# Features

 * Basic variables
 * Basic logic
 * Loops & stuff using the goto (based on line number)
 * Lists & list operators
 * Comments
 * Usr input
 * Brain damage of course too

# Commands

The active keyword is filled in with the active value. In a print it has to be used alone.
The lines are based on lines of code after all blank lines are removed including comments.
If you comment on a print and add spaces before it the spaces will be rendered sense there is no type definitions.

## General

 - set    [address] [value]      sets the value at the adress to the value inputed
 - setAdd [address] [address]    sets the value at the adress to the value at the address
 - get    [address]              sets "active" to the value (put active in code to acess)
 - goto   [line]                 jumps to the line
 - in     [address]              assigns the inputted value (by the usr) to the address
 - print  [text]                 prints a line of text (can be multiple words but to use active just put active)
 - printl [text]                 same as print but adds a return (helpful for when using active)

## Lists

 - newList [address]                   creates a new list
 - addItem [address] [item]            adds an item
 - setItem [address] [index] [add 2]   sets an item at an index
 - getItme [address] [index]           gets the item at the index
 - getSize [address]                   gets the size of the item

## Logic

 - <  [address 1] [address 2]                checks address 1 <  address 2, next line skipped if false
 - \>  [address 1] [address 2]               checks address 1 >  address 2, next line skipped if false
 - == [address 1] [address 2]                checks address 1 == address 2, next line skipped if false
 - &= [num skip] [address 1] [address 2]     checks address 1 == address 2, next line skipped if false
 - != [address 1] [address 2]                checks address 1 != address 2, next line skipped if false
 - <= [address 1] [address 2]                checks address 1 <= address 2, next line skipped if false
 - \>= [address 1] [address 2]               checks address 1 >= address 2, next line skipped if false
 - ++ [address 1]                            adds 1 to the value at the address
 - -- [address 1]                            subs 1 from the value at the address
 - += [address 1] [address 2]                adds the value at address 2 to the value at address 1
 - -= [address 1] [address 2]                subs the value at address 2 from the value at address 1
 - *= [address 1] [address 2]                mults the value at address 1 and 2 together

## Other Funcs

- getRand [min] [max]     sets active to a random value between the min and max (or at the values)

# Other

Much more brain damaging commands and updates may be coming or I may drop the project after the amount of headaches it's caused.



