# c--
c-- is a very interesting language. Like how c++ means c but 1 better, c-- means c but a lot worse. It's an interpreted language that skips the lexer and has you type the token formated code making it very hard to understand. The commands are bellow, be warned, you brain will hurt a lot. This is a joke langauge just for fun but try to use it if you want. Run the program and input the file (be careful, you can't use \n). There is next to no error detection in the code while running and there are probably many bugs.

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

 - <  [address 1] [address 2]     checks address 1 <  address 2, next line skipped if false
 - \>  [address 1] [address 2]     checks address 1 >  address 2, next line skipped if false
 - == [address 1] [address 2]     checks address 1 == address 2, next line skipped if false
 - != [address 1] [address 2]     checks address 1 != address 2, next line skipped if false
 - <= [address 1] [address 2]     checks address 1 <= address 2, next line skipped if false
 - \>= [address 1] [address 2]     checks address 1 >= address 2, next line skipped if false
 - ++ [address 1]                 adds 1 to the value at the address
 - -- [address 1]                 subs 1 from the value at the address
 - += [address 1] [address 2]     adds the value at address 2 to the value at address 1
 - -= [address 1] [address 2]     subs the value at address 2 from the value at address 1
 - *= [address 1] [address 2]     mults the value at address 1 and 2 together

# Other

Much more brain damaging commands and updates may be coming or I may drop the project after the amount of headaches it's caused.

