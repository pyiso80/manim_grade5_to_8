import numpy as np
from manim import *
config.background_color="#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24

class FracIntro1(Scene):
    left_alignment_point = Point().shift(LEFT*6)
    
    def construct(self):
        self.play_addition(m=1, n=2, k=1, l=4, a=2, b=4, c=1, d=4, p=2, q=1, op_str="+", vertical_shift=3)
        self.play_addition(m=2, n=5, k=1, l=3, a=6, b=15, c=5, d=15, p=3, q=5, op_str="-", vertical_shift=1)

        self.play_multiplication(1,2,2,5, -1)

        self.play_division(1,3,2,5,-3)  

    def play_addition(self, m, n, k, l, a, b, c, d, p, q, op_str, vertical_shift):

        """
        m/n = a/b, k/l=c/d and b=d

        f1, f2, f3, f4 are Tex symbols to represent m/n, k/l, a/b, c/d respectively

        f5, f6 are intermediate Tex symbols calculation to get a/b  and c/d from m/n and k/l respectively
        eg., pm/pn, qk/ql to get a/b, c/d
        """

        f1 = MathTex(f"{{{m}}}", r'\over', f"{{{n}}}")
        f2 = MathTex(f"{{{k}}}", r'\over', f"{{{l}}}")
        f3 = MathTex(f"{{{a}}}", r'\over', f"{{{b}}}")
        f4 = MathTex(f"{{{c}}}", r'\over', f"{{{d}}}")
        result = MathTex(f"{{{a+c}}}", r'\over', f"{{{d}}}")

        f5 = (
            MathTex(f"{{{p}}}", r'\times', f"{{{m}}}", r'\over', f"{{{p}}}", r'\times', f"{{{n}}}") 
            if p != 1 
            else  MathTex(f"{{{m}}}", r'\over', f"{{{n}}}"))
        f6 = (
            MathTex(f"{{{q}}}", r'\times', f"{{{k}}}", r'\over', f"{{{q}}}", r'\times', f"{{{l}}}") 
            if q != 1 
            else MathTex(f"{{{k}}}", r'\over', f"{{{l}}}"))

        # 1/2 + 1/4
        op = MathTex(op_str)
        eq_sign = MathTex("=")
        exp = VGroup(f1, op.copy(), f2).arrange(buff=MED_LARGE_BUFF)
        
        # = 1/2 + 1/4 ---> = 2x1/2x2 + 1/4
        exp1 = VGroup(eq_sign.copy(), f5, op.copy(), f6).arrange(buff=MED_LARGE_BUFF)
        exp1.next_to(exp, buff=MED_LARGE_BUFF)

        # = 2x1/2x2 + 1/4 => = 2/4 + 1/4
        exp2 = VGroup(eq_sign.copy(), f3, op.copy(), f4).arrange(buff=MED_LARGE_BUFF)
        exp2.next_to(exp1, buff=MED_LARGE_BUFF)

        # = 2/4 + 1/4 => = 4/3
        exp3 = VGroup(eq_sign.copy(), result).arrange(buff=MED_LARGE_BUFF)
        exp3.next_to(exp2, buff=MED_LARGE_BUFF)

        group = VGroup(exp, exp1, exp2, exp3).next_to(self.left_alignment_point).shift(UP*vertical_shift)
        self.play(Write(exp, lag_ratio=0.1))
        self.wait()
        self.play(Write(exp1, lag_ratio=0.1))
        self.wait()
        self.play(Write(exp2, lag_ratio=0.1))
        self.wait()
        self.play(Write(exp3, lag_ratio=0.1))
        self.play(Indicate(f1), Indicate(f3), Indicate(f5))
        return group

    def play_multiplication(self, m, n, k, l, vertical_shift):
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

    def play_division(self, m, n, k, l, vertical_shift):
        mul = MathTex(r'\times')
        div = MathTex(r'\divisionsymbol')
        eq_sign = MathTex("=")
        f1 = MathTex(f"\\frac{{{m}}}{{{n}}}")
        f2 = MathTex(f"\\frac{{{k}}}{{{l}}}")
        f2recp = MathTex(f"\\frac{{{l}}}{{{k}}}")
        
        str1 = f"{m}\\times{l}"
        str2 = f"{n}\\times{k}"
        f3 = MathTex(f"\\frac{{{str1}}}{{{str2}}}")
        result = MathTex(f"\\frac{{{m*l}}}{{{n*k}}}")

        exp_op = div.copy()
        exp = VGroup(f1, exp_op , f2).arrange(buff=MED_LARGE_BUFF)

        exp1_term1 = f1.copy()
        exp1_term2 = f2.copy()
        exp1_op = div.copy()
        exp1 = VGroup(eq_sign.copy(), exp1_term1, exp1_op, exp1_term2).arrange(buff=MED_LARGE_BUFF)
        exp1.next_to(exp, buff=MED_LARGE_BUFF)
        
        exp2 = VGroup(eq_sign.copy(), f3).arrange(buff=MED_LARGE_BUFF)
        exp2.next_to(exp1, buff=MED_LARGE_BUFF)

        exp3 = VGroup(eq_sign.copy(), result).arrange(buff=MED_LARGE_BUFF)
        exp3.next_to(exp2, buff=MED_LARGE_BUFF)

        group = VGroup(exp, exp1, exp2, exp3).next_to(self.left_alignment_point).shift(UP*vertical_shift)
        
        self.play(Write(exp))
        self.wait()
        self.play(Write(exp1))
        self.wait()
        
        self.play(ReplacementTransform(exp1_op, mul.copy().move_to(exp1_op)), 
                    ReplacementTransform(exp1_term2, f2recp.move_to(exp1_term2)))
        self.wait()
        self.play(Write(exp2))
        self.wait()
        self.play(Write(exp3))
        
        sr = SurroundingRectangle(group, stroke_width=2)
        self.play(ShowPassingFlash(
            sr.copy().set_color(BLUE),
            run_time=2,
            time_width=0.35
        ))
        self.wait()
        return group