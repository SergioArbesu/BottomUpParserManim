from manim import *

class ShiftReduce(Scene):
    def construct(self):
        text = Text("int  *  int  +  int", font_size=48)
        text2 = Text("T", font_size=48)
        text3 = Text("E", font_size=48)
        text.to_edge(DOWN)
        text2.to_edge(DOWN)
        text3.to_edge(DOWN)

        commands = VGroup()

        # Create bar
        bar = Text("|", font_size=48, color=YELLOW)
        bar.move_to(text.get_left() + 0.2 * LEFT)

        # Create tree
        leafs = Text("int  *  int  +  int", font_size=48)

        self.play(AnimationGroup(
            Write(text),
            Write(bar)
        ))

        # Shift 1
        command_old = Text("Shift", font_size=32)
        command_old.to_edge(DL)
        self.play(Write(command_old))
        self.play(bar.animate.move_to(text[:3].get_right() + 0.2 * RIGHT))
        commands.add(command_old)
        self.play(commands.animate.shift(UP))

        # Shift 2
        command = Text("Shift", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(bar.animate.move_to(text[:4].get_right() + 0.2 * RIGHT))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 3
        command = Text("Shift", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(bar.animate.move_to(text[:7].get_right() + 0.2 * RIGHT))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int
        command = Text("Reduce T -> int", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text2.move_to(text[5])
        self.play(Transform(text[4:7], text2))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int * T
        command = Text("Reduce T -> int * T", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(Transform(text[:7], text2))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 4
        command = Text("Shift", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(bar.animate.move_to(text[:8].get_right() + 0.2 * RIGHT))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 5
        command = Text("Shift", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(bar.animate.move_to(text.get_right() + 0.2 * RIGHT))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int
        command = Text("Reduce T -> int", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text2.move_to(text[9])
        self.play(Transform(text[8:], text2))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T
        command = Text("Reduce E -> T", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text3.move_to(text[9])
        self.play(Transform(text[8:], text3))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T + E
        command = Text("Reduce E -> T + E", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text3.move_to(text[7])
        self.play(Transform(text, text3))

        self.wait()
