from manim import *
import math
config.background_color="#202020"
BACKGROUND = "#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24

class FracMulIntro1(Scene):
    left_alignment_point = Point().shift(LEFT*6)
    def construct(self):
        
        # self.play_mul(2,5,3,7)
        # self.clear()
        # self.play_mul("m", "n", "k", "l")
        #self.play_mul_illu(2,3,5,7)
        fd = self.get_frac_illustration(14, 21, range(0,14), sec_per_group=2)
        self.add(*fd.get("parts"),*fd.get("markers"))
        self.wait()

    def play_mul_illu(self, m, n, k, l):
        f1dt= self.get_frac_illustration(m, n, range(0,m))
        f2dt= self.get_frac_illustration(m*l, n*l, range(0,m*l), sec_per_group=m)
        f2dt.get("group").move_to(f1dt.get("group"))
        f1dt.get("vg_symbols").next_to(f1dt.get("group"), buff=0.5, direction=DOWN)
        f1dt.get("vg_symbols").next_to(f1dt.get("group"), buff=0.5, direction=DOWN)
        
        self.play( 
            FadeIn(
                *f1dt.get("parts"),
                # f1dt.get("symbols")[0]   
            ))

        for i in range(0,n):
            self.play(FadeIn(*f2dt.get("parts")[i*l: (i+1)*l ]))

        sec_even = f2dt.get("parts")[0::2]
        sec_odd = f2dt.get("parts")[1::2]
        v = f2dt.get("vectors_gp")

        self.play(FadeIn(*f2dt.get("markers")))

        # self.play(AnimationGroup(
        #             *[s.animate().shift(v.get_unit_vector()) for s,v in zip(sec_even, v)]
        #         ),
        #         AnimationGroup(
        #             *[s.animate().shift(v.get_unit_vector()) for s,v in zip(sec_odd, v)]
        #         )
        #     )

        # for s1, v1, s2, v2 in zip(sec_even[0:l], v_even[0:l], sec_odd, v_odd):
        #     self.play(s1.animate().shift(-v1.get_unit_vector()), s2.animate().shift(-v2.get_unit_vector()), run_time=0.3)
        #     self.wait(0.4)


    def get_frac_illustration(self, m, n, which_parts, radius=1.5, c=1, sec_per_group=1):
        circle = Circle(radius=radius, color=MY_RED, stroke_width=1.5, stroke_color=GOLD, fill_opacity=1)
        arc_len = 2*PI/n
        pts_n = [circle.point_at_angle(arc_len * i) for i in range(0, n)]
        dps = [Dot().move_to(p) for p in pts_n]
        VGroup(circle, *dps).rotate(angle=PI/2, about_point=circle.get_center())

        pts_mid_n = [circle.point_at_angle(arc_len * i + PI/2 + arc_len/2) for i in range(0, n)]
        vec_n = [Line(circle.get_center(), p) for p in pts_mid_n]

        pts_mid_group = [circle.point_at_angle(PI/2*i) for i in range(1, 4)]
        dps = [Dot().move_to(p) for p in pts_mid_group]
        vec_mid_group = [Line(circle.get_center(), p) for p in pts_mid_group]

        all_parts = [
            AnnularSector(
                inner_radius=0, 
                outer_radius=radius, 
                angle=arc_len, 
                start_angle=(PI/2 + i * arc_len),
                color=MY_RED,
                stroke_width=1.5,
                stroke_color=GOLD)
            for i in range(0, n)]    
        parts = [p.copy().set_fill(BACKGROUND).set_stroke(color=GRAY, width=1.5, opacity=1).set_z_index(0) for p in all_parts]
        for i in which_parts:
            parts[i].set_fill(MY_RED).set_stroke(GOLD).set_z_index(1) 
        symbols = [
                    MathTex(f"{{{m}}}", r'\over', f"{{{n}}}"),
                    MathTex(f"{{{c}}}", r'\times', f"{{{m}}}", r'\over', f"{{{c}}}", r'\times', f"{{{n}}}"),
                    MathTex(f"{{{int(c*m)}}}", r'\over', f"{{{int(c*n)}}}")
                ] if c != 1 else [MathTex(f"{{{m}}}", r'\over', f"{{{n}}}")]*3
        for s in symbols:
            s.next_to(circle, direction=DOWN, buff=0.5)   

        VGroup(*all_parts).move_to(ORIGIN)
        VGroup(*parts).move_to(ORIGIN)
        circle.move_to(ORIGIN)
        VGroup(*dps).move_to(ORIGIN)
        VGroup(*vec_n).move_to(ORIGIN)
        VGroup(*vec_mid_group).move_to(ORIGIN)

        return {
            "all_parts" : all_parts,
            "parts" : parts,
            "symbols" : symbols,
            "vg_symbols" : VGroup(*symbols),
            "circle" : circle,
            "markers" : dps,
            "vectors" :vec_n,
            "vectors_gp": vec_mid_group,
            "group" : VGroup(*all_parts, *parts, circle, *dps, VGroup(*vec_n))
        }

