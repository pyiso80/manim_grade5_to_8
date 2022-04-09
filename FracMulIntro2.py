from manim import *
import numpy as np
import copy as cp

config.background_color="#FDF6E3" # OLD PAPER: "#E0C9A6", PAPER WHITE: #F9FBFF, moleskin: FFF8DC
BACKGROUND = "#FFFBEF"
G_FIG_FILL_COLOR1 = "#EE204D" # LIGHT CORAL: "#F08080" #TEAL LEAD: #05EDFF #PINE: #6EB183
G_FIG_STROKE_COLOR1= "#0B0B0B" #Main, # TORONTO: #526B9B, 
G_FIG_STROKE_COLOR2= "#A9A9A9" #Dimmed
G_FIG_STROKE_W1=1.5
IND_COLOR1 = "#FF2600"
IND_STROKE_W1 = 1.25
TEX_COLOR1 = "#212121"
BR_COLOR1 = "#424242"

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

class FracMulIntro2(Scene):

    def construct(self):
        Rectangle.set_default(fill_color=G_FIG_FILL_COLOR1, fill_opacity=0
            , stroke_color=G_FIG_STROKE_COLOR1, stroke_width=G_FIG_STROKE_W1)
        Line.set_default(color=G_FIG_STROKE_COLOR1, stroke_width=G_FIG_STROKE_W1)
        MathTex.set_default(color=TEX_COLOR1, font_size=34)
        AnnularSector.set_default(color=G_FIG_FILL_COLOR1,
            stroke_color=G_FIG_STROKE_COLOR1,
            stroke_width= G_FIG_STROKE_W1)
        Brace.set_default(color=BR_COLOR1)
        
        self.play_frac_mul_illu(6, 7, 4, 5)


    def play_frac_mul_illu(self, k, l, m, n):
        f1dt = self.create_frac_mul_illu(m, n, gp_sz1=7)
        self.play(FadeIn(f1dt.get(UNIT_SQ), direction=DOWN))
        self.play(FadeIn(VGroup(*f1dt.get(V_SLICES)[:-1]), lag_ratio=0.6, shift=DOWN),
                    run_time=2)

        f1_br = Brace(VGroup(*f1dt.get(V_SLICES)[:m]), direction=DOWN)
        f1_tex = self.get_frac_tex(m, n).next_to(f1_br, direction=DOWN)
        self.play(FadeIn(f1_br), FadeIn(f1_tex, shift=UP))

        self.play(FadeIn(VGroup(*f1dt.get(H_DIVS)[1:-1]), shift=RIGHT*2, lag_ratio=0.5),
                    run_time=2)

        to_remove = self.mobjects

        f2dt = self.create_frac_mul_illu1(m, n, k, l)
        unit_frac_pcs = f2dt.get(UNIT_FRAC_PCS)
        for r in unit_frac_pcs:
            self.add(VGroup(*r))
        
        self.remove(*to_remove)

        original = VGroup(*f2dt.get(EQ_P_O_P))
        target = original \
                    .generate_target() \
                    .arrange(center=False, direction=UP, buff=0.1)\
                    .move_to(ORIGIN)\
                    .align_to(f2dt.get(UNIT_SQ), direction=LEFT)\
                    .shift(LEFT*0.2)

        original.save_state()

        h_divs_br = Brace(VGroup(*f2dt.get(UNIT_SQ)), direction=LEFT, buff=0.4)
        h_divs_lbl = Tex(f"{{{l}}} equals parts of ${{{m}}} \\over {{{n}}}$"
                            , arg_separator=" ") 
        h_divs_lbl.rotate(90*DEGREES).next_to(h_divs_br, direction=LEFT)
        self.play(AnimationGroup(*[o.animate.move_to(t) for o, t in zip(original, target)]))
        self.play(FadeIn(h_divs_br, run_time=0.75), Write(h_divs_lbl), run_time=1)
        self.wait(3)
        self.play(Restore(original))

        self.wait()

        k_parts_br = Brace(VGroup(*[row[0]for row in unit_frac_pcs[:-1]]), direction=LEFT)
        k_parts_tex = Tex(f"${{{k}}}$ of them is ${{{k}}} \\over {{{l}}}$", 
                            r'$\times$', 
                            f"${{{m}}} \\over {{{n}}}$",
                            arg_separator=" ")
        k_parts_tex.rotate(90*DEGREES)
        k_parts_tex.next_to(k_parts_br, direction=LEFT)
        to_fade = VGroup(*[VGroup(*r) for r in unit_frac_pcs[k:]])
        to_fade.generate_target().set_fill(opacity=0)
        self.play(Transform(h_divs_br, k_parts_br),
                    FadeOut(h_divs_lbl),
                    Write(k_parts_tex),
                    Transform(to_fade, to_fade.target))
       
        self.wait(3)


    def create_frac_mul_illu(self, m, n, gp_sz1=1, gp_sz2=1):
        unit_sq = Square(side_length=THE_UNIT, fill_opacity=0)
        v_slices =  [Rectangle(height=THE_UNIT, width= THE_UNIT/n) for i in range(n)]
        for s in v_slices[:m]:
            s.set_fill(opacity=1)
        gp = VGroup(*v_slices[:]).arrange(buff=0)

        h_divs = [Line(start=UP*y, end=[THE_UNIT, y, 0]) 
                    for y in np.linspace(0, THE_UNIT, gp_sz1+1)]
        VGroup(*h_divs).move_to(ORIGIN)
        return {
            V_SLICES: v_slices,
            H_DIVS: h_divs,
            UNIT_SQ: unit_sq,
            GP_OF_ALL: VGroup(*v_slices, *h_divs, unit_sq)
        }


    def create_frac_mul_illu1(self, m, n, k, l):
        unit_sq = Square(side_length=THE_UNIT, fill_opacity=0)
        unit_frac_w = THE_UNIT/n
        unit_frac_h = THE_UNIT/l
        a_row = [Rectangle(height=unit_frac_h, width=unit_frac_w) for _ in range(n)]
        rows = [cp.deepcopy(a_row) for _ in range(l)]
        gp = VGroup()
        for i in range(l):
            gp.add(VGroup(*rows[i]).arrange(buff=0)) 
        gp.arrange(direction=UP, buff=0)

        for i in range(l):
            for j in range(m):
                rows[i][j].set_fill(color=G_FIG_FILL_COLOR1, opacity=1)

        eq_parts_of_frac = [VGroup(*r[:m]) for r in rows]
            
        return {
            UNIT_FRAC_PCS: rows,
            UNIT_SQ: unit_sq,
            EQ_P_O_P: eq_parts_of_frac
        }


    def get_frac_tex(self, m, n, font_sz=34):
        return MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", font_size=font_sz)


    def get_frac_tex_1(self, k, l, m, n, font_sz=34):
        return MathTex(f"{{{k}}}", r'\times', f"{{{m}}}", r'\over', f"{{{l}}}", r'\times',
            f"{{{n}}}")