from cgitb import text
from manim import *
import numpy as np
import copy as cp

config.background_color="#FDF6E3" # OLD PAPER: "#E0C9A6", PAPER WHITE: #F9FBFF, moleskin: FFF8DC
BACKGROUND = "#FFFBEF"
G_FIG_FILL_COLOR1 = "#EE204D" # LIGHT CORAL: "#F08080" #TEAL LEAD: #05EDFF #PINE: #6EB183

G_FIG_STROKE_COLOR1= "#0B0B0B" #Main, # TORONTO: #526B9B, 
G_FIG_STROKE_COLOR2= "#A9A9A9" #Dimmed
LINE_COLOR1 = "#0B0B0B"
NUM_LINE_COLOR1 = "#0B0B0B"
G_FIG_STROKE_W1=1.5
IND_COLOR1 = "#FF2600"
FLASH_COLOR1 = "#B22222"
IND_STROKE_W1 = 1.25
TEX_COLOR1 = "#212121"
BR_COLOR1 = "#424242"

CROSS_COLOR = LINE_COLOR1

SECTORS = "sectors"
SEC_LBLS = "sec_lbls"
SEC_GP_LBLS ="sec_gp_lbls"
SEC_BISECTORS = "sec_bisectors"
SEC_GP1_BISECTORS = "sec_gp1_bisectors"
SEC_GP2_BISECTORS = "sec_gp2_bisectors"
GP_OF_ALL = "gp_of_all"
LEFT_ALIGN_PT = Point().shift(LEFT*6)

THE_UNIT = 3

V_SLICES = "v_slices"
H_DIVS = "h_divs"
UNIT_SQ = "unit_sq"

UNIT_FRAC_PCS = "unit_frac_pcs"
EQ_P_O_P = "eq_parts_of_frac"

MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24

MANIM_NUM_LINE1 = "manim_num_line1"
MANIM_NUM_LINE2 = "manim_num_line1"
LINE_ONLY = "line_only"
W_TICKS = "w_ticks"
F_TICKS = "f_ticks"
W_LBLS = "w_lbls"
F_LBLS = "f_lbls"
W_SEGS = "w_segs"
F_SEGS = "f_segs"
POSITIVE_SIDE = "left_part"
NEGATIVE_SIDE = "right_part"

class FracMulIntro3(Scene):

    def construct(self):
        Rectangle.set_default(fill_color=G_FIG_FILL_COLOR1, fill_opacity=0
            , stroke_color=G_FIG_STROKE_COLOR1, stroke_width=G_FIG_STROKE_W1)
        Line.set_default(color=G_FIG_STROKE_COLOR1, stroke_width=G_FIG_STROKE_W1)
        MathTex.set_default(color=TEX_COLOR1, font_size=34)
        Text.set_default(color=TEX_COLOR1, font_size=34)
        DecimalNumber.set_default(color=TEX_COLOR1, font_size=34)
        AnnularSector.set_default(color=G_FIG_FILL_COLOR1,
            stroke_color=G_FIG_STROKE_COLOR1,
            stroke_width= G_FIG_STROKE_W1)
        Brace.set_default(color=BR_COLOR1)
        Line.set_default(color=LINE_COLOR1)
        NumberLine.set_default(color=NUM_LINE_COLOR1)

        self.play_number_line_intro(6, 7, 4, 5)
        self.wait()

    def play_number_line_intro(self, k, l, m, n):
            num_line = self.create_rational_number_line(
                denominator = n,
                unit = MY_UNIT_SIZE * 3,
                left_end = 0,
                right_end = 2, 
                frac_font_sz=24, 
                frac_seg_stroke_width=6)
            
            #display plain line
            self.play(GrowFromCenter(num_line.get(LINE_ONLY).move_to(ORIGIN), run_time= 2))
            self.play(FadeIn(VGroup(*num_line.get(W_TICKS)), shift = DOWN, lag_ratio = 0.1),
                        run_time = 2)
            self.play(ApplyWave(VGroup(*num_line.get(W_TICKS)), run_time = 2))
            self.play(FadeIn(*num_line.get(W_LBLS), shift=DOWN), lag_ratio=0.2)

            self.play(FadeIn(VGroup(*num_line.get(F_TICKS)), shift = DOWN, lag_ratio = 0.5),
                        run_time = 2)
            self.play(ApplyWave(VGroup(*num_line.get(F_TICKS)), run_time = 2))
            self.play(FadeIn(*num_line.get(F_LBLS), shift=DOWN, lag_ratio=0.5))

            self.play(FadeOut(*num_line.get(F_LBLS)[m+1:], *num_line.get(F_LBLS)[:m]))

            num_line2 = self.create_rational_number_line(
                denominator = l*n,
                unit = MY_UNIT_SIZE * 3,
                left_end = 0,
                right_end = 2, 
                frac_font_sz=24, 
                frac_seg_stroke_width=6)
            
            for e in num_line2.get(F_TICKS):
                e.stroke_width = 1
                e.set_z_index(-1)
            f_tick2 = num_line2.get(F_TICKS)
            self.play(FadeIn(VGroup(*f_tick2), shift = DOWN),
                                lag_ratio = 0.6, run_time = 2)
            self.play(ApplyWave(VGroup(*f_tick2), run_time = 2))

            # m/n divided into l equal parts
            eq_pop = [Cross(scale_factor=0.075, stroke_width=1.75, stroke_color=CROSS_COLOR)\
                            .move_to(t) 
                        for t in f_tick2[0::4]]
            self.play(FadeIn(*eq_pop[:l+1], lag_ratio=0.5))

            br_pop = BraceBetweenPoints(eq_pop[0].get_center(),
                                        eq_pop[l].get_center(), 
                                        direction=UP,
                                        buff=0.15)
            tex_pop = self.get_frac_tex_l_pop(l, m, n)
            self.add(tex_pop.next_to(br_pop, direction=UP))
            self.play(FadeIn(br_pop, tex_pop))

            self.play(FadeOut(br_pop, *eq_pop[2:l+1], *tex_pop, num_line.get(F_LBLS)[m]))

            #k parts when m/n is divided into l equal parts
            br_res = BraceBetweenPoints(eq_pop[0].get_center(),
                                        eq_pop[k].get_center(), 
                                        direction=UP,
                                        buff=0.15)

            exp = self.get_frac_tex_mul_step1(k, l, m, n)
            equal = MathTex('=', color=TEX_COLOR1)
            exp2 = self.get_frac_tex_simple(k*m, l*n)
            tex_res = VGroup(exp, equal, exp2) \
                        .arrange().next_to(br_res, direction=UP, buff=0.15)

            k_parts = [e.copy() for e in eq_pop[:k+1]]
            self.play(Write(VGroup(*exp.submobjects[:3])),
                        FadeIn(*k_parts, lag_ratio=0.5, run_time=0.75)) # k x m
            self.play(Write(VGroup(equal, exp2[0])))
            
            eq_pop2 = num_line.get(F_TICKS)[:n+1]
            self.play(AnimationGroup(*[ e.animate().shift(UP*0.4 )for e in eq_pop2],
                        lag_ratio = 0.1),
                        run_time=3)
            self.play(FadeIn(exp.submobjects[3], shift=RIGHT), 
                Write(exp[4:]),
                AnimationGroup(*[ e.animate().shift(DOWN*0.4 )for e in eq_pop2],
                                lag_ratio = 0.5),
                                run_time=3)

            one_ov_n = num_line.get(F_TICKS)
            brs_1_ov_n = [BraceBetweenPoints(one_ov_n[0].get_center(),
                                        one_ov_n[1].get_center(), 
                                        direction=UP,
                                        buff=0.15) for _ in range(n)]
            self.add(VGroup(*brs_1_ov_n).arrange(buff=0, center=False))

            self.play(FadeIn(exp2[1], shift=RIGHT),Write(exp2[2]))
            self.wait(3)

            self.wait()


    def create_rational_number_line(
        self,
        denominator = 3,
        unit = MY_UNIT_SIZE,
        right_end = 3,
        left_end = -3,
        tip_seg_factor = 1,
        frac_font_sz = MY_FRAC_FONT_SIZE,
        frac_seg_stroke_width = 4):

        #### just for generating ticks, and points on the number line, not for display
        w_numline = NumberLine(
            [left_end, right_end, 1],
            unit_size = unit,
            include_ticks = True, 
            include_tip = False,
            include_numbers=True,
            tick_size=0.125
        )

        #### just for generating ticks, and points on the number line, not for display
        f_numline = NumberLine(
            [left_end, right_end, 1/denominator],
            unit_size = unit,
            include_ticks = True, 
            include_tip = False,
            label_direction=UP,
            include_numbers=True,
            font_size=14,
            decimal_number_config={"num_decimal_places": 2},
            tick_size=0.075
        )

        w_ticks = [*w_numline.get_tick_marks()]
        f_ticks = [*f_numline.get_tick_marks()]
        w_lbls = [*w_numline.numbers]

        line_only = None
        r_arrow = None
        l_arrow = None
        if left_end < 0:
            r_arrow = Arrow(w_numline.get_tick(0).get_center(), 
                        w_ticks[-1].get_center() + RIGHT * tip_seg_factor,
                        tip_length = 0.3, 
                        stroke_width = 2, 
                        buff = 0)
            l_arrow = Arrow(w_numline.get_tick(0).get_center(),
                        w_ticks[0].get_center() + LEFT * tip_seg_factor,
                        tip_length = 0.3, 
                        stroke_width = 2,
                        buff = 0)
            line_only = VGroup(r_arrow, l_arrow)
        else:
            r_arrow = Arrow(w_numline.get_tick(0).get_center(),
                        w_ticks[-1].get_center() + RIGHT * tip_seg_factor,
                        tip_length = 0.3,
                        stroke_width = 2,
                        buff = 0)
            line_only = VGroup(r_arrow)

        line_only.move_to(ORIGIN)
        if(left_end == 0):
            line_only.shift(DOWN)

        frac_lbls = [] 
        for numer, s in enumerate(f_ticks, left_end*denominator):
            sign = "-" if numer < 0 else ""
            lbl = MathTex(f"{{{sign}}}", f"\\frac{{{abs(numer)}}} {{{denominator}}}",
                            font_size=frac_font_sz)
            # to align without sign with ticks
            no_sign = MathTex(f"\\frac{{{abs(numer)}}} {{{denominator}}}", 
                                    font_size=frac_font_sz)
            no_sign.next_to(s, direction=UP)
            lbl.next_to(s, direction=UP).align_to(no_sign, direction=RIGHT)
            
            frac_lbls.append(lbl)

        f_segs = []
        f_seg_length = (f_ticks[1].get_center() - f_ticks[0].get_center())[0]
        for t in f_ticks[:-1]:
            seg = Line(
                t.get_center(), 
                t.get_center() + [f_seg_length, 0, 0], 
                stroke_width=frac_seg_stroke_width
            )
            f_segs.append(seg)

        w_segs = []
        w_seg_length = (w_ticks[1].get_center() - w_ticks[0].get_center())[0]
        for t in w_ticks[:-1]:
            seg = Line(
                t.get_center(), 
                t.get_center() + [w_seg_length, 0, 0], 
                stroke_width=frac_seg_stroke_width
            )
            w_segs.append(seg)

        gp = {
            MANIM_NUM_LINE1: w_numline,
            MANIM_NUM_LINE2: f_numline,
            LINE_ONLY: line_only,
            W_TICKS: w_ticks,
            F_TICKS: f_ticks,
            W_LBLS: w_lbls,
            F_LBLS: frac_lbls,
            F_SEGS: f_segs,
            W_SEGS: w_segs,
            POSITIVE_SIDE: r_arrow,
            NEGATIVE_SIDE: l_arrow
        }

        return gp

    def get_segments(self, start_numerator, end_numerator, frac_segs):
        vg = VGroup()
        for i in range(start_numerator, end_numerator, 1):
            vg.add(frac_segs[i])
        return vg

    def get_single_segment(self, fticks, start_at=0, num_of_segs=1, the_color=RED, 
                            stroke_width=6, with_tips=False, tip_color=RED):
        seg = Line(fticks[start_at].get_center(), fticks[start_at + num_of_segs].get_center(), 
                stroke_width=stroke_width, color=the_color)
        if with_tips:
            t1 = ArrowSquareFilledTip(color=tip_color, length=1/8)
            t1.rotate(45*DEGREES)
            t2 = ArrowSquareFilledTip(color=tip_color, length=1/8)
            t2.rotate(45*DEGREES)
            t1.move_to(seg.get_left())
            t2.move_to(seg.get_right())
            return VGroup(seg, t1, t2)
        else:
            return VGroup(seg)
    """
    Parameters
    ----------
    start_at: Starting position of the brace. For the number line displaying multiples of 
    1/3, start_at=4 will start the
    brace at position 4/3.
    num_of_segs: the numerator of the fraction
    """
    def get_brace(self, fticks, start_at=0, num_of_segs=1):
        return BraceBetweenPoints(fticks[start_at].get_center(), 
            fticks[start_at + num_of_segs].get_center(), direction=UP)

    def alternate_color(self, ticks, color1, color2):
        for x, i in zip(ticks, range(0, len(ticks), 1)):
            x.set_color(color1 if i % 2 else color2 )

    def get_frac_tex_mul_step1(self, k, l, m, n, font_sz=34):
        return MathTex(f"{{{k}}}", r'\times', f"{{{m}}}", r'\over', f"{{{l}}}", r'\times',
            f"{{{n}}}")

    def get_frac_tex_l_pop(self, l, m, n, font_sz=34):
        return Tex(f"{{{l}}} equal parts of $\\frac{{{m}}}{{{n}}}$", font_size=font_sz)

    def get_frac_tex_simple(self, m, n, font_sz=34):
        return MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", font_size=font_sz)
       

        