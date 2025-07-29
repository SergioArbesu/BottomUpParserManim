from manim import *
import os
import pathlib

def get_instructions():
    """
    format of the instructions file:
    one instruction per line
    one blank line
    the bnf

    Instructions must be Shift or Reduce + the rule used in the reduction
    ---
    int * int

    Shift
    Reduce T ::= int
    Reduce T ::= int * T

    E ::= T + E | T
    T ::= int * T | int | (E)
    ---

    returns a list with the instructions and the bnf
    """
    instructions = []
    path = pathlib.Path(os.getenv('INSTRUCTIONS', 'instructions.txt'))
    with open(path, 'r') as f:
        code = f.readline().strip()
        f.readline()
        line = f.readline().strip()
        while line != '':
            instructions.append(line)
            line = f.readline().strip()
        bnf = f.read().strip()
    return code, instructions, bnf


class ProgrammableSR(Scene):
    def construct(self):
        code, instructions, bnf = get_instructions()

        commands = VGroup()

        # Create BNF
        bnf = Text(bnf, font_size=24)
        bnf.to_edge(DR)
        box = SurroundingRectangle(bnf, buff=0.2)
        bnf_box = VGroup(bnf, box)

        self.play(AnimationGroup(
            Write(bnf_box)
        ))

        # first instruction
        command_old = Text(instructions[0], font_size=32)
        command_old.to_edge(DL)
        self.play(Write(command_old))
        #self.play(bar.animate.move_to(text[:3].get_right() + 0.2 * RIGHT))
        commands.add(command_old)

        for instruction in instructions[1:]:
            self.play(commands.animate.shift(UP))
            command = Text(instruction, font_size=32)
            command.to_edge(DL)
            self.play(AnimationGroup(
                Write(command),
                command_old.animate.set_opacity(0.5)
            ))
            commands.add(command)
            #self.play(bar.animate.move_to(text[:4].get_right() + 0.2 * RIGHT))
            command_old = command

        self.wait(2)
