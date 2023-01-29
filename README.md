# problem-0-A-computer-
This project is used to covert assembly code to machine code and execute it.
This code is an implementation of an assembler, which converts assembly language to machine language.
The Assembler class has a method called assemble, which takes an assembly code as a string and returns
a list of encoded machine code. The class also has a dictionary called instruction_map, which maps instruction mnemonics
to instruction numbers, and a symbol table, which stores labels and variables. 
The script can also be ran as a module, the section that runs when the script is run as the main script encodes 
an assembly program passed as a string and returns it in the form of a list. 

The contact information for the project is Joseph Musya, 
email address: muciajoe@gmail.com.

# Running the code
There are two different codes, assembler and simulator.
The assembler can be executed indivudually since it generates the machine code.
On the other hand, simulator code relies on the assembler and is therefore imported 
in the simulator script

*Windows computer*
> python assemble.py
> python simulator.py
*UNIX system*
*Replace the python3 with the current version in your computer*
> python3 assemble.py
> python3 simulator.py
