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
        command_opacity = 0.45
        command_font_size = 32

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

        tree = VGroup(leafs, reduced1, reduced2, reduced3, reduced4, reduced5).scale(0.65)
        tree.to_edge(RIGHT, buff=0.2)

        # Create DFA
        dfa_font_size = 12
        label_font_size = 12

        s0_1 = Text("S' → .E", font_size=dfa_font_size)
        s0_2 = Text("E → .T", font_size=dfa_font_size)
        s0_3 = Text("E → .T + E", font_size=dfa_font_size)
        s0_4 = Text("T → .(E)", font_size=dfa_font_size)
        s0_5 = Text("T → .int * T", font_size=dfa_font_size)
        s0_6 = Text("T → .int", font_size=dfa_font_size)
        s0 = VGroup(s0_1, s0_2, s0_3, s0_4, s0_5, s0_6)
        s0.arrange(DOWN, buff=0.1)
        box_0 = SurroundingRectangle(s0, buff=0.1)
        s0_box = VGroup(s0, box_0).shift(LEFT * 4)

        s1 = Text("S' → E.", font_size=dfa_font_size)
        box_1 = SurroundingRectangle(s1, buff=0.1)
        s1_box = VGroup(s1, box_1).shift(UP * 1.7).shift(LEFT * 4)

        s2_1 = Text("E → T.", font_size=dfa_font_size)
        s2_2 = Text("E → T. + E", font_size=dfa_font_size)
        s2 = VGroup(s2_1, s2_2)
        s2.arrange(DOWN, buff=0.1)
        box_2 = SurroundingRectangle(s2, buff=0.1)
        s2_box = VGroup(s2, box_2).shift(UP * 1.7).shift(LEFT * 2)

        s3_1 = Text("T → int. * T", font_size=dfa_font_size)
        s3_2 = Text("T → int.", font_size=dfa_font_size)
        s3 = VGroup(s3_1, s3_2)
        s3.arrange(DOWN, buff=0.1)
        box_3 = SurroundingRectangle(s3, buff=0.1)
        s3_box = VGroup(s3, box_3).shift(LEFT * 2)

        s4_1 = Text("E → T + .E", font_size=dfa_font_size)
        s4_2 = Text("E → .T", font_size=dfa_font_size)
        s4_3 = Text("E → .T + E", font_size=dfa_font_size)
        s4_4 = Text("T → .(E)", font_size=dfa_font_size)
        s4_5 = Text("T → .int * T", font_size=dfa_font_size)
        s4_6 = Text("T → .int", font_size=dfa_font_size)
        s4 = VGroup(s4_1, s4_2, s4_3, s4_4, s4_5, s4_6)
        s4.arrange(DOWN, buff=0.1)
        box_4 = SurroundingRectangle(s4, buff=0.1)
        s4_box = VGroup(s4, box_4).shift(UP * 1.7)

        s5 = Text("E → T + E.", font_size=dfa_font_size)
        box_5 = SurroundingRectangle(s5, buff=0.1)
        s5_box = VGroup(s5, box_5).shift(UP * 1.7).shift(RIGHT * 2)

        s6_1 = Text("T → (.E)", font_size=dfa_font_size)
        s6_2 = Text("E → .T", font_size=dfa_font_size)
        s6_3 = Text("E → .T + E", font_size=dfa_font_size)
        s6_4 = Text("T → .(E)", font_size=dfa_font_size)
        s6_5 = Text("T → .int * T", font_size=dfa_font_size)
        s6_6 = Text("T → .int", font_size=dfa_font_size)
        s6 = VGroup(s6_1, s6_2, s6_3, s6_4, s6_5, s6_6)
        s6.arrange(DOWN, buff=0.1)
        box_6 = SurroundingRectangle(s6, buff=0.1)
        s6_box = VGroup(s6, box_6).shift(RIGHT * 2)

        s7 = Text("T → (E.)", font_size=dfa_font_size)
        box_7 = SurroundingRectangle(s7, buff=0.1)
        s7_box = VGroup(s7, box_7).shift(DOWN * 1.7).shift(RIGHT)

        s8 = Text("T → (E).", font_size=dfa_font_size)
        box_8 = SurroundingRectangle(s8, buff=0.1)
        s8_box = VGroup(s8, box_8).shift(DOWN * 1.9).shift(LEFT * 0.5)

        s9_1 = Text("T → int * .T", font_size=dfa_font_size)
        s9_2 = Text("T → .(E)", font_size=dfa_font_size)
        s9_3 = Text("T → .int * T", font_size=dfa_font_size)
        s9_4 = Text("T → .int", font_size=dfa_font_size)
        s9 = VGroup(s9_1, s9_2, s9_3, s9_4)
        s9.arrange(DOWN, buff=0.1)
        box_9 = SurroundingRectangle(s9, buff=0.1)
        s9_box = VGroup(s9, box_9).shift(DOWN * 1.7).shift(LEFT * 2)

        s10 = Text("T → int * T.", font_size=dfa_font_size)
        box_10 = SurroundingRectangle(s10, buff=0.1)
        s10_box = VGroup(s10, box_10).shift(DOWN * 0.5)

        s0_arrow = Arrow(start=s0_box.get_left() + LEFT * 0.75, end=s0_box.get_left(), buff=0.1)
        s0_s1_arrow = LabeledArrow(Text("E", font_size=label_font_size), start=s0_box.get_top(), end=s1_box.get_bottom(), buff=0.1)
        s0_s2_arrow = LabeledArrow(Text("T", font_size=label_font_size), start=s0_box, end=s2_box, buff=0.1)
        s0_s3_arrow = LabeledArrow(Text("int", font_size=label_font_size), start=s0_box.get_right(), end=s3_box.get_left(), buff=0.1)
        s0_s6_line_1 = Line(s0_box.get_bottom(), DOWN * 2.5 + LEFT * 3)
        s0_s6_line_2 = LabeledLine(Text("(", font_size=label_font_size), start=DOWN * 2.5 + LEFT * 3, end=DOWN * 2.5 + RIGHT * 1.5)
        s0_s6_line_3 = Arrow(start=DOWN * 2.5 + RIGHT * 1.5, end=s6_box.get_bottom() + RIGHT * 0.2, buff=0, max_tip_length_to_length_ratio=0.15)
        s0_s6_arrow = VGroup(s0_s6_line_1, s0_s6_line_2, s0_s6_line_3)
        s2_s4_arrow = LabeledArrow(Text("+", font_size=label_font_size), start=s2_box.get_right(), end=s4_box.get_left(), buff=0.1)
        s3_s9_arrow = LabeledArrow(Text("*", font_size=label_font_size), start=s3_box.get_bottom(), end=s9_box.get_top(), buff=0.1)
        s4_s2_arrow = LabeledArrow(Text("T", font_size=label_font_size), start=s4_box, end=s2_box, buff=0.1)
        s4_s3_arrow = LabeledArrow(Text("int", font_size=label_font_size), start=s4_box, end=s3_box, buff=0.1)
        s4_s5_arrow = LabeledArrow(Text("E", font_size=label_font_size), start=s4_box.get_right(), end=s5_box.get_left(), buff=0.1)
        s4_s6_arrow = LabeledArrow(Text("(", font_size=label_font_size), start=s4_box, end=s6_box, buff=0.1)
        s6_s2_arrow = LabeledArrow(Text("T", font_size=label_font_size), start=s6_box.get_left(), end=s2_box.get_bottom(), buff=0.1, max_tip_length_to_length_ratio=0.1)
        s6_s3_arrow = LabeledArrow(Text("int", font_size=label_font_size), start=s6_box.get_left(), end=s3_box.get_right(), buff=0.1, max_tip_length_to_length_ratio=0.1)
        s6_s6_line_1 = Line(s6_box.get_right() + UP * 0.5, s6_box.get_right() + RIGHT * 0.5)
        s6_s6_line_2 = LabeledArrow(Text("(", font_size=label_font_size), start=s6_box.get_right() + RIGHT * 0.5, end=s6_box.get_right() + DOWN * 0.5, buff=0)
        s6_s6_arrow = VGroup(s6_s6_line_1, s6_s6_line_2)
        s6_s7_arrow = LabeledArrow(Text("E", font_size=label_font_size), start=s6_box.get_bottom(), end=s7_box, buff=0.1)
        s7_s8_arrow = LabeledArrow(Text(")", font_size=label_font_size), start=s7_box.get_left(), end=s8_box.get_right(), buff=0.1)
        s9_s3_arrow = LabeledArrow(Text("int", font_size=label_font_size), start=s9_box.get_left() + UP * s9_box.height / 2, end=s3_box, buff=0.1)
        s9_s6_arrow = LabeledArrow(Text("(", font_size=label_font_size), start=s9_box.get_right(), end=s6_box, buff=0.1)
        s9_s10_arrow = LabeledArrow(Text("T", font_size=label_font_size), start=s9_box, end=s10_box, buff=0.1)

        dfa = VGroup(s0_box, s1_box, s2_box, s3_box, s4_box, s5_box, s6_box, s7_box, s8_box, s9_box, s10_box,
                     s0_s1_arrow, s0_s2_arrow, s0_s3_arrow, s0_s6_arrow, s2_s4_arrow, s3_s9_arrow, s4_s2_arrow,
                     s4_s3_arrow, s4_s5_arrow, s4_s6_arrow, s6_s2_arrow, s6_s3_arrow, s6_s6_arrow, s6_s7_arrow,
                     s7_s8_arrow, s9_s3_arrow, s9_s6_arrow, s9_s10_arrow, s0_arrow)
        dfa.to_edge(UP, buff=0.2).shift(RIGHT)
        box_0.set_color(RED)

        self.add(dfa)

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
        command_old = Text("Shift", font_size=command_font_size)
        command_old.to_edge(DL)
        self.play(Write(command_old))
        self.play(AnimationGroup(
            bar.animate.move_to(text[:3].get_right() + 0.2 * RIGHT),
            box_0.animate.set_color(YELLOW),
            box_3.animate.set_color(RED)
        ))
        commands.add(command_old)
        self.play(commands.animate.shift(UP))

        # Shift 2
        command = Text("Shift", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            bar.animate.move_to(text[:4].get_right() + 0.2 * RIGHT),
            box_3.animate.set_color(YELLOW),
            box_9.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 3
        command = Text("Shift", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            bar.animate.move_to(text[:7].get_right() + 0.2 * RIGHT),
            box_9.animate.set_color(YELLOW),
            box_3.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int
        command = Text("Reduce T → int", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        text2.move_to(text[5])
        self.play(AnimationGroup(
            Transform(text[4:7], text2),
            FadeIn(reduced1),
            box_3.animate.set_color(YELLOW),
            box_0.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_0.animate.set_color(YELLOW),
            box_3.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_3.animate.set_color(YELLOW),
            box_9.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_9.animate.set_color(YELLOW),
            box_10.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int * T
        command = Text("Reduce T → int * T", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            Transform(text[:7], text2),
            FadeIn(reduced2),
            box_10.animate.set_color(YELLOW),
            box_0.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_0.animate.set_color(YELLOW),
            box_2.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 4
        command = Text("Shift", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            bar.animate.move_to(text[:8].get_right() + 0.2 * RIGHT),
            box_2.animate.set_color(YELLOW),
            box_4.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Shift 5
        command = Text("Shift", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        self.play(AnimationGroup(
            bar.animate.move_to(text.get_right() + 0.2 * RIGHT),
            box_4.animate.set_color(YELLOW),
            box_3.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce T -> int
        command = Text("Reduce T → int", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        text2.move_to(text[9])
        self.play(AnimationGroup(
            Transform(text[8:], text2),
            FadeIn(reduced3),
            box_3.animate.set_color(YELLOW),
            box_0.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_0.animate.set_color(YELLOW),
            box_2.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_2.animate.set_color(YELLOW),
            box_4.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_4.animate.set_color(YELLOW),
            box_2.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T
        command = Text("Reduce E → T", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        text3.move_to(text[9])
        self.play(AnimationGroup(
            Transform(text[8:], text3),
            FadeIn(reduced4),
            box_2.animate.set_color(YELLOW),
            box_0.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_0.animate.set_color(YELLOW),
            box_2.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_2.animate.set_color(YELLOW),
            box_4.animate.set_color(RED)
        ))
        self.play(AnimationGroup(
            box_4.animate.set_color(YELLOW),
            box_5.animate.set_color(RED)
        ))
        self.play(commands.animate.shift(UP))
        command_old = command

        # Reduce E -> T + E
        command = Text("Reduce E → T + E", font_size=command_font_size)
        command.to_edge(DL)
        self.play(AnimationGroup(
            Write(command),
            command_old.animate.set_opacity(command_opacity)
        ))
        commands.add(command)
        text3.move_to(text[7])
        self.play(AnimationGroup(
            Transform(text, text3),
            FadeIn(reduced5)
        ))

        self.wait(2)
