import math
from manim import *
config.background_color="#202020"
BACKGROUND = "#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24

class FracIntro(Scene):
    def construct(self):
        self.play_add_frac(1,2,1,4,2,4,1,4)
        self.clear()
        self.play_add_frac(1,3,2,5,5,15,6,15)
        # self.play(FadeOut(*self.mobjects))
        # self.play_add_frac(1,3,2,6,2,6,2,6)
        # self.play(FadeOut(*self.mobjects))
        # self.play_add_frac(1,2,1,3,3,6,2,6)
        # self.play(FadeOut(*self.mobjects))
  

    def play_add_frac(self, m, n, k, l, a, b, c, d):

        f1dt= self.get_frac_illustration(m, n, range(0,m),c=int(b/n))

        f3dt= self.get_frac_illustration(a, b, range(0, a))

        f2dt = self.get_frac_illustration(k, l, range(l-1, l-k-1, -1), c=int(d/l))

        f4dt= self.get_frac_illustration(c, d, range(d-1, d-c-1, -1))

        result = self.get_frac_illustration(a+c, d, [*range(0, a), *range(d-1, d-c-1, -1)])

        eq = Tex(r'$=$')
        plus = Tex(r'$+$')

        VGroup(f1dt.get("group"), plus, f2dt.get("group"), eq, result.get("group")).arrange(buff=0.5)
        
        f3dt.get("group").move_to(f1dt.get("group"))
        f4dt.get("group").move_to(f2dt.get("group"))

        f1dt.get("vg_symbols").next_to(f1dt.get("group"), buff=0.5, direction=DOWN)
        f3dt.get("vg_symbols").next_to(f3dt.get("group"), buff=0.5, direction=DOWN)
        f2dt.get("vg_symbols").next_to(f2dt.get("group"), buff=0.5, direction=DOWN)
        f4dt.get("vg_symbols").next_to(f4dt.get("group"), buff=0.5, direction=DOWN)
        result.get("vg_symbols").next_to(result.get("group"), buff=0.5, direction=DOWN)

        self.play(FadeIn(f1dt.get("circle"), f2dt.get("circle")))
        self.play(FadeIn(*f1dt.get("all_parts")),
           FadeIn(*f2dt.get("all_parts"))
        )

        self.play(
            FadeOut(f1dt.get("circle", f2dt.get("circle")), *f1dt.get("all_parts"), *f2dt.get("all_parts")), 
            FadeIn(
                *f1dt.get("parts"),
                *f2dt.get("parts"),
                f1dt.get("symbols")[0],
                f2dt.get("symbols")[0],    
            ))

        self.play(
            FadeIn(*f3dt.get("parts")),
            FadeIn(*f4dt.get("parts")),
            ReplacementTransform(f1dt.get("symbols")[0], f1dt.get("symbols")[1]),
            ReplacementTransform(f2dt.get("symbols")[0], f2dt.get("symbols")[1]),
        )
        print(f3dt.get("vectors"))
        #self.play(f3dt.get("parts")[0].animate().shift(f3dt.get("vectors")[0]))
        self.play(AnimationGroup(
                    *[s.animate().shift(v.get_unit_vector()*0.5 if m != a else [0,0,0]) for s,v in zip(f3dt.get("parts"), f3dt.get("vectors"))],
                    *[s.animate().shift(v.get_unit_vector()*0.5 if k != c else [0,0,0]) for s,v in zip(f4dt.get("parts"), f4dt.get("vectors"))]
                )
            )
        self.play(AnimationGroup(
                    *[s.animate().shift(-v.get_unit_vector()*0.5 if m != a else [0,0,0]) for s,v in zip(f3dt.get("parts"), f3dt.get("vectors"))],
                    *[s.animate().shift(-v.get_unit_vector()*0.5 if k != c else [0,0,0]) for s,v in zip(f4dt.get("parts"), f4dt.get("vectors"))]
                )
            )
        self.wait()
        self.play(
            ReplacementTransform(f1dt.get("symbols")[1], f1dt.get("symbols")[2]),
            ReplacementTransform(f2dt.get("symbols")[1], f2dt.get("symbols")[2]),
        )

        self.remove(*f1dt.get("parts"), *f2dt.get("parts"))
        self.wait(1.5)

        self.play(FadeIn(plus))
        self.play(FadeIn(eq, *result.get("parts"), result.get("symbols")[0]))
        self.wait()
        
    def get_frac_illustration(self, m, n, which_parts, radius=1.5, c=1, sec_per_group=1):
        circle = Circle(radius=radius, color=MY_RED, stroke_width=1.5, stroke_color=GOLD, fill_opacity=1)
        arc_len = 2*PI/n
        pts_n = [circle.point_at_angle((arc_len) * i) for i in range(0, n)]
        dps = [Dot().move_to(p) for p in pts_n]
        VGroup(circle, *dps).rotate(angle=PI/2, about_point=circle.get_center())

        pts_mid_n = [circle.point_at_angle((arc_len) * i + PI/2 + arc_len/2) for i in range(0, n)]
        vec_n = [Line(circle.get_center(), p) for p in pts_mid_n]

        pts_mid_group = [circle.point_at_angle(arc_len*sec_per_group/2 * i + PI/2) for i in range(1, math.ceil(n/sec_per_group)+1)]
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


        


