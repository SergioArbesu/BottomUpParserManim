from manim import *
import os
import pathlib

def get_instructions() -> tuple[str, list[str], str]:
    """
    format of the instructions file:
    one line of code
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
        bnf = Text(bnf, font_size=36)
        bnf.to_edge(DR)
        box = SurroundingRectangle(bnf, buff=0.2)
        bnf_box = VGroup(bnf, box)

        # Create code
        code_font_size = 48
        text = VGroup()
        for elem in code.split():
            text.add(Text(elem, font_size=code_font_size))
        text.arrange(RIGHT, buff=0.4)
        text.shift(RIGHT * 1)

        # Create bar
        bar = Text('|', font_size=code_font_size, color=YELLOW)
        bar.move_to(text[0].get_left() + 0.2 * LEFT)

        self.play(AnimationGroup(
            Write(bnf_box),
            Write(text),
            Write(bar)
        ))

        # first instruction
        if instructions[0] != 'Shift':
            raise ValueError('First instruction must always be Shift')
        command_old = Text(instructions[0], font_size=32)
        command_old.to_edge(DL)
        self.play(Write(command_old))
        self.play(bar.animate.move_to(text[0].get_right() + 0.2 * RIGHT))
        commands.add(command_old)

        shift_index = 1  # the index of the next element that will be shifted into the stack
        for instruction in instructions[1:]:
            self.play(commands.animate.shift(UP))
            command = Text(instruction, font_size=32)
            command.to_edge(DL)
            self.play(AnimationGroup(
                Write(command),
                command_old.animate.set_opacity(0.45)
            ))
            commands.add(command)
            if instruction == 'Shift':
                # move the bar
                self.play(bar.animate.move_to(text[shift_index].get_right() + 0.2 * RIGHT))
                shift_index += 1
            else:
                # apply the reduction
                instruction = instruction.split()
                rule_length = len(instruction) - 3
                code_match = text[shift_index - rule_length : shift_index]
                result = Text(instruction[1], font_size=code_font_size)
                result.move_to(code_match)
                self.play(ReplacementTransform(code_match, result))
                # tricking manim into turning all the elements into only one
                # instead of turning each element into one of the result's characters
                text[shift_index - rule_length : shift_index] = Text('a')
                shift_index -= rule_length - 1
                text[shift_index - 1] = result
                self.play(AnimationGroup(
                    text.animate.arrange(RIGHT, buff=0.4).shift(RIGHT * 1),
                    bar.animate.move_to(text[shift_index - 1].get_right() + 0.2 * RIGHT)
                ))
            command_old = command

        self.wait(2)
