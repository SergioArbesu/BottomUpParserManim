# Shift-Reduce Animation

## How to run

Once your python virtual environment is created, run the following command to install all the required dependencies
```bash
pip install -r requirements.txt
```

To create an animation for the slides example, run the following command to create the animation
```bash
manim -pqh shiftReduce.py ShiftReduce
```
This animation will contain a parse tree

To create an animation with your own production rules and parsed text, first edit the [instructions.txt file](instructions.txt).

In it, write the text you will parse in the first line.

Separated by an empty line, write the set of instructions that will be performed during the parse.

Write
```bash
Shift
```
for shifts.

Write
```bash
Reduce T ::= int * T
```
for reductions.

Separated by another empty line, write your bnf rules.
```bash
E ::= T + E | T
T ::= int * T | int | (E)
```

After editing the instructions.txt file, run the following command to create the animation
```bash
manim -pqh programmableSR.py ProgrammableSR
```
This animation will not contain a parse tree

The ::= string in the instructions and bnf can be swapped with →, -> or any other string.

