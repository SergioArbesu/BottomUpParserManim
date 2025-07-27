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
        bar = Text("|", font_size=48, color=RED)
        bar.move_to(text.get_left() + 0.2 * LEFT)

        # Create tree
        font_size_tree = 48
        color_lines = YELLOW
        leafs = Text("int  *  int  +  int", font_size=font_size_tree)
        leafs.shift(DR * 1.5)

        text_reduced1 = Text("T", font_size=font_size_tree)
        text_reduced1.move_to(leafs[4:7]).shift(UP * 1.5)
        line_reduced1 = Line(text_reduced1.get_bottom(), leafs[4:7].get_top(), buff=0.2, color=color_lines)
        reduced1 = VGroup(text_reduced1, line_reduced1)

        text_reduced2 = Text("T", font_size=font_size_tree)
        text_reduced2.move_to(leafs[2:5]).shift(UP * 3)
        line1_reduced2 = Line(text_reduced2.get_bottom(), leafs[2:5].get_top(), buff=0.2, color=color_lines)
        line2_reduced2 = Line(text_reduced2.get_bottom(), leafs[:3].get_top(), buff=0.2, color=color_lines)
        line3_reduced2 = Line(text_reduced2.get_bottom(), text_reduced1.get_top(), buff=0.2, color=color_lines)
        reduced2 = VGroup(text_reduced2, line1_reduced2, line2_reduced2, line3_reduced2)

        text_reduced3 = Text("T", font_size=font_size_tree)
        text_reduced3.move_to(leafs[8:]).shift(UP * 1.5)
        line_reduced3 = Line(text_reduced3.get_bottom(), leafs[8:].get_top(), buff=0.2, color=color_lines)
        reduced3 = VGroup(text_reduced3, line_reduced3)

        text_reduced4 = Text("E", font_size=font_size_tree)
        text_reduced4.move_to(text_reduced3).shift(UP * 1.5)
        line_reduced4 = Line(text_reduced4.get_bottom(), text_reduced3.get_top(), buff=0.2, color=color_lines)
        reduced4 = VGroup(text_reduced4, line_reduced4)

        text_reduced5 = Text("E", font_size=font_size_tree)
        text_reduced5.move_to(leafs[6:9]).shift(UP * 4.5)
        line1_reduced5 = Line(text_reduced5.get_bottom(), text_reduced2.get_top(), buff=0.2, color=color_lines)
        line2_reduced5 = Line(text_reduced5.get_bottom(), leafs[6:9].get_top(), buff=0.2, color=color_lines)
        line3_reduced5 = Line(text_reduced5.get_bottom(), text_reduced4.get_top(), buff=0.2, color=color_lines)
        reduced5 = VGroup(text_reduced5, line1_reduced5, line2_reduced5, line3_reduced5)

        #self.add(leafs, text_reduced1, line_reduced1, text_reduced2, line1_reduced2, line2_reduced2, line3_reduced2,
        #         text_reduced3, line_reduced3, text_reduced4, line_reduced4, text_reduced5, line1_reduced5, line2_reduced5,
        #         line3_reduced5)

        # Create BNF
        bnf = Text("E → T + E | T\nT → int * T | int | (E)", font_size=24)
        bnf.to_edge(DR)
        box = SurroundingRectangle(bnf, buff=0.2)
        bnf_box = VGroup(bnf, box)

        self.play(AnimationGroup(
            Write(text),
            Write(bar),
            Write(leafs),
            Write(bnf_box)
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
        command = Text("Reduce T → int", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text2.move_to(text[5])
        self.play(AnimationGroup(
            Transform(text[4:7], text2),
            FadeIn(reduced1)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int * T
        command = Text("Reduce T → int * T", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            Transform(text[:7], text2),
            FadeIn(reduced2)
        ))
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
        command = Text("Reduce T → int", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text2.move_to(text[9])
        self.play(AnimationGroup(
            Transform(text[8:], text2),
            FadeIn(reduced3)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T
        command = Text("Reduce E → T", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text3.move_to(text[9])
        self.play(AnimationGroup(
            Transform(text[8:], text3),
            FadeIn(reduced4)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T + E
        command = Text("Reduce E → T + E", font_size=32)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(0.5)
        ))
        commands.add(command)
        text3.move_to(text[7])
        self.play(AnimationGroup(
            Transform(text, text3),
            FadeIn(reduced5)
        ))

        self.wait(2)
