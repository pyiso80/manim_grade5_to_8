import numpy as np
import itertools
from manim import *
config.background_color="#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24

class FracMulIntro(Scene):
    left_alignment_point = Point().shift(LEFT*6)
    def construct(self):
        # self.play_mul(2,5,3,7)
        # self.clear()
        # self.play_mul("m", "n", "k", "l")
        self.play_mul_as_addition(7,5)

    def play_mul1(self, m=1, n=2, k=1, l=4, vertical_shift=0):
        op = MathTex(r'\times')
        eq_sign = MathTex("=")
        f1 = MathTex(f"\\frac{{{m}}}{{{n}}}")
        f2 = MathTex(f"\\frac{{{k}}}{{{l}}}")
        str1 = f"{m}\\times{k}"
        str2 = f"{n}\\times{l}"
        
        f3 = MathTex(f"\\frac{{{str1}}}{{{str2}}}")
        result = MathTex(f"\\frac{{{m*k}}}{{{n*l}}}")

        exp = VGroup(f1, op.copy(), f2).arrange(buff=MED_LARGE_BUFF)

        exp1 = VGroup(eq_sign.copy(), f3).arrange(buff=MED_LARGE_BUFF)
        exp1.next_to(exp, buff=MED_LARGE_BUFF)

        exp2 = VGroup(eq_sign.copy(), result).arrange(buff=MED_LARGE_BUFF)
        exp2.next_to(exp1, buff=MED_LARGE_BUFF)

        group = VGroup(exp, exp1, exp2).next_to(self.left_alignment_point).shift(UP*vertical_shift)
        self.play(Write(exp))
        self.wait()
        self.play(Write(exp1))
        self.wait()
        self.play(Write(exp2))
        self.wait()
        return group

    def play_mul(self, m="a", n="b", k="c", l="d", vertical_shift=0):
        op = MathTex(r'\times')
        eq_sign = MathTex("=")
        f1 = MathTex(f"\\frac{{{m}}}{{{n}}}")
        f2 = MathTex(f"\\frac{{{k}}}{{{l}}}")
        str1 = f"{m} \\times {k}"
        str2 = f"{n} \\times {l}"
        print(str1)
        
        f3 = MathTex(f"{{{str1}}}", r'\over', f"{{{str2}}}")
        result = MathTex(f"{{{m+k}}}", r'\over', f"{{{n+l}}}")

        exp = VGroup(f1, op.copy(), f2).arrange(buff=MED_LARGE_BUFF)

        exp1 = VGroup(eq_sign.copy(), f3).arrange(buff=MED_LARGE_BUFF)
        exp1.next_to(exp, buff=MED_LARGE_BUFF)

        exp2 = VGroup(eq_sign.copy(), result).arrange(buff=MED_LARGE_BUFF)
        exp2.next_to(exp1, buff=MED_LARGE_BUFF)

        group = VGroup(exp, exp1, exp2).next_to(self.left_alignment_point).shift(UP*vertical_shift)
        self.play(Write(exp))
        self.wait()
        self.play(Write(exp1))
        self.wait()
        self.play(Write(exp2))
        self.wait()
        return group

    def play_mul_as_addition(self, m=2, n=3):
        exp = MathTex(f"{{{m}}}", "\\times",  f"{{{n}}}")
        eqsign = MathTex("=")
        str1 = list(itertools.chain.from_iterable(zip([str(n)]*m, [r'+']*m)))
        exp1 = MathTex(*str1[0:2*m-1])
        VGroup(exp, eqsign, exp1).arrange(buff=MED_SMALL_BUFF).next_to(self.left_alignment_point)
        self.play(Write(exp))
        self.wait(0.5)
        self.play(Write(eqsign))
        self.play(Write(exp1), run_time=2)



