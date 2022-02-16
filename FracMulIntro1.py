from manim import *

config.background_color="#FFFBEF"
BACKGROUND = "#FFFBEF"
G_FIG_FILL_1 = "#33CCCC"
G_FIG_STROKE_1= "#5E5E5E" #Main
G_FIG_STROKE_2= "#A9A9A9" #Dimmed
IND_COLOR = "#FF2600"
IND_LINE_W = 1.5
TEX_COLOR1 = "#212121"

class FracMulIntro1(Scene):
    left_alignment_point = Point().shift(LEFT*6)
    def construct(self):
        self.wait()

        
        
        # self.play_mul(2,5,3,7)
        # self.clear()
        # self.play_mul("m", "n", "k", "l")
        self.play_mul_illu(2,3,5,7)
        self.play_mul_illu(3,5,4,3)
        # f2dt= self.get_frac_illustration(14, 21, range(0,14), sec_per_group=3)
        # self.add(*f2dt.get("parts"), *f2dt.get("markers"))
        #Circle().point_at_angle(2*PI + 0.1)
        self.wait()

    def play_mul_illu(self, m, n, k, l):
        f1dt= self.get_frac_illustration(m, n, range(0,m),sec_per_group=1)
        f2dt= self.get_frac_illustration(m*l, n*l, range(0,m*l), sec_per_group=m)
        f2dt.get("group").move_to(f1dt.get("group"))
        f1dt.get("vg_symbols").next_to(f1dt.get("group"), buff=0.5, direction=DOWN)
        
        tex1_f1 = MathTex(f"{{{k}}}", r'\over', f"{{{l}}}", font_size=34, color=TEX_COLOR1)
        tex2_x = MathTex(r'\times', font_size=34, color=TEX_COLOR1) 
        tex3_f2 = MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", font_size=34, color=TEX_COLOR1)
        tex4 = Tex("is defined as", 
                    f"{{{k}}}", 
                    "parts when", arg_separator=" ", font_size=34, color=TEX_COLOR1)
        tex5 = tex3_f2.copy()
        
        tex6 = Tex(f" is divided into", 
                    f"{{{l}}} equal parts.", arg_separator=" ", font_size=34, color=TEX_COLOR1)

        self.play(Write(VGroup(tex1_f1, tex2_x, tex3_f2, tex4, tex5, tex6).arrange().shift(UP*3)))
                    

        
        self.play( 
            FadeIn(
                *f1dt.get("parts"),
                f1dt.get("symbols")[0].next_to(f1dt.get("group"), direction=LEFT, buff=2)
            ))

        self.play(FadeOut(f1dt.get("symbols")[0]))
        for i in range(0,n):
            self.play(FadeIn(*f2dt.get("parts")[i*l: (i+1)*l ]), run_time=0.1)
            self.wait()

        self.remove(*f1dt.get("parts"))

        ###
        # Each part of 3/3 is divided into 7 equal parts

        self.play(VGroup(*f2dt.get("parts")[0:l]).animate().shift(f1dt.get("vectors")[0].get_unit_vector()*0.05)
                    ,VGroup(*f2dt.get("parts")[l:2*l]).animate().shift(f1dt.get("vectors")[1].get_unit_vector()*0.05)
                    ,VGroup(*f2dt.get("parts")[2*l:3*l]).animate().shift(f1dt.get("vectors")[2].get_unit_vector()*0.1))

        self.play(VGroup(*f2dt.get("parts")[0:l]).animate().shift(-f1dt.get("vectors")[0].get_unit_vector()*0.05)
                    ,VGroup(*f2dt.get("parts")[l:2*l]).animate().shift(-f1dt.get("vectors")[1].get_unit_vector()*0.05)
                    ,VGroup(*f2dt.get("parts")[2*l:3*l]).animate().shift(-f1dt.get("vectors")[2].get_unit_vector()*0.1))

        ###
        # For 2/3, there are 14 equal parts  
        self.play(FadeIn(*f2dt.get("sec_lbls")[0:2*l]))
        self.wait(3)

        sec_even = f2dt.get("parts")[0::2][0:l]
        sec_odd = f2dt.get("parts")[1::2][0:l]
        shift_val = [0.1, 0.15]*n*l
        v = f2dt.get("vectors_gp")

        self.play(AnimationGroup(
                    *[s.animate().shift(v.get_unit_vector()*d) for s,v,d in zip(sec_even, v, shift_val)]
                ),
                AnimationGroup(
                    *[s.animate().shift(v.get_unit_vector()*d) for s,v,d in zip(sec_odd, v, shift_val)]
                ),
            )

        ###
        # 14 equals parts of 2/3 into 7 equals parts and emphasize 7 equal parts of 2/3
        self.play(FadeIn(*f2dt.get("gp_lbls")[0:l], shift=RIGHT, run_time=1.5),
                    FadeOut(*f2dt.get("sec_lbls")[0:2*l], shift=LEFT, run_time=0.75))
        self.wait(2)

        ###
        # emphasize 5 of 7 parts of 2/3 more
        self.play(AnimationGroup(
                    *[s.animate().shift(v.get_unit_vector()*d) for s,v,d in zip(sec_even[0:5], v, shift_val)]
                ),
                AnimationGroup(
                    *[s.animate().shift(v.get_unit_vector()*d) for s,v,d in zip(sec_odd[0:5], v, shift_val)]
                ),
                AnimationGroup(*[Flash(l, scale_value=1.7, color=IND_COLOR, line_stroke_width=IND_LINE_W) for l in f2dt.get("gp_lbls")[0:5]])
            )
        self.play(AnimationGroup(*[Wiggle(l, scale_value=1.7) for l in f2dt.get("gp_lbls")[0:5]]), run_time=2)

        ###
        # De-emphasize 6th and 7th parts of 2/3
        de_ems = [s.set_fill(color=G_FIG_FILL_1, opacity=0.4) for s in f2dt.get("parts")[10:14]]

        self.play(AnimationGroup(
                    *[s.animate().shift(-v.get_unit_vector()*d) for s,v,d in zip(sec_even[5:7], v[5:7], shift_val[5:7])]
                ),
                AnimationGroup(
                    *[s.animate().shift(-v.get_unit_vector()*d) for s,v,d in zip(sec_odd[5:7], v[5:7], shift_val[5:7])]
                ),
                FadeOut(*f2dt.get("gp_lbls")[k:7])
            )

        self.play(FadeOut(*f2dt.get("gp_lbls")[0:k]))

        exp = MathTex(f"{{{k}}}", r'\times', f"{{{m}}}", r'\over', f"{{{l}}}", r'\times', f"{{{n}}}", color=TEX_COLOR1)
        equal = MathTex('=', color=TEX_COLOR1)
        exp2 = MathTex(f"{{{int(k*m)}}}", r'\over', f"{{{int(l*n)}}}", color=TEX_COLOR1)
        VGroup(exp, equal, exp2).arrange().next_to(f2dt.get("group"), direction=LEFT, buff=1)

        self.play(Write(VGroup(*exp.submobjects[0:3])))#5x2
        self.play(Write(VGroup(equal, exp2[0])), FadeIn(*f2dt.get("sec_lbls")[0:k*m], lag_ratio=0.5, run_time=2))# = 10, 1,2,3, ... 10
        self.play(FadeOut(*f2dt.get("sec_lbls")[0:k*m]))

        self.play(FadeIn(exp.submobjects[3], shift=RIGHT), Write(exp[4:]), FadeIn(*f2dt.get("sec_lbls"), lag_ratio=0.5, run_time=2))
        self.play(FadeIn(exp2[1], shift=RIGHT),Write(exp2[2]))
        

        self.wait(10)
        


    def get_frac_illustration(self, m, n, which_parts, radius=1.5, c=1, sec_per_group=1, diff_radius = 0.5):
        circle = Circle(radius=radius, color=G_FIG_FILL_1, stroke_width=G_FIG_STROKE_1, stroke_color=G_FIG_STROKE_1, fill_opacity=1)
        outer_circle = Circle(radius=radius+diff_radius, color=G_FIG_FILL_1, stroke_width=1.5, stroke_color=G_FIG_STROKE_1, fill_opacity=1)
        arc_len = 2*PI/n

        #dots and points on the start and end points of the arc of the sectors
        div_dots = [Dot().move_to(p) for p in 
            [circle.point_at_angle(arc_len * i) for i in range(0, n)]]
        VGroup(*div_dots).rotate(angle=PI/2, about_point=circle.get_center())
        div_pts = [d.get_center() for d in div_dots]

        #dots and points on the mid points of the arc of the sectors
        mid_pt_dots = [Dot().move_to(circle.point_at_angle(arc_len * i)) for i in range(0, n)]
        VGroup(*mid_pt_dots).rotate(angle=PI/2+ (arc_len/2.0))
        mid_pts = [d.get_center() for d in mid_pt_dots ]
        outward_vecs = [Line(circle.get_center(), p) for p in mid_pts]

        gp_mid_pt_dots = [Dot().move_to(circle.point_at_angle(i * arc_len*sec_per_group)) for i in range(0, int(n/sec_per_group))]
        VGroup(*gp_mid_pt_dots).rotate(angle=PI/2+ arc_len*sec_per_group/2.0)
        gp_mid_pts = [d.get_center() for d in gp_mid_pt_dots]
        gp_outward_vecs = [Line(circle.get_center(), p) for p in gp_mid_pts]


        sec_lbl_dots = [Dot().move_to(outer_circle.point_at_angle(i*arc_len)) for i in range(0, n)]
        VGroup(*sec_lbl_dots).rotate(angle=PI/2 + (arc_len/2.0))
        sec_lbl_pts = [d.get_center() for d in sec_lbl_dots]
        sec_lbls = [MathTex(i+1, font_size=18, color=TEX_COLOR1).move_to(p)#.rotate(i*arc_len + arc_len/2) 
                        for p,i in zip(sec_lbl_pts, range(0, n))] 

        gp_lbl_dots = [Dot().move_to(outer_circle.point_at_angle(i * arc_len*sec_per_group)) for i in range(0, int(n/sec_per_group))]
        VGroup(*gp_lbl_dots).rotate(angle=PI/2+ arc_len*sec_per_group/2.0)
        gp_lbl_pts = [d.get_center() for d in gp_lbl_dots]
        gp_lbls = [MathTex(i+1, font_size=18, color=TEX_COLOR1).move_to(p)#.rotate(i*arc_len + arc_len/2) 
                    for p,i in zip(gp_lbl_pts, range(0, int(n/sec_per_group)))]       

        all_parts = [
            AnnularSector(
                inner_radius=0, 
                outer_radius=radius, 
                angle=arc_len, 
                start_angle=(PI/2 + i * arc_len),
                color=G_FIG_FILL_1,
                stroke_width=G_FIG_STROKE_1,
                stroke_color=G_FIG_STROKE_1)
            for i in range(0, n)]    
        parts = [p.copy().set_fill(BACKGROUND).set_stroke(color=G_FIG_STROKE_1, width=1.5, opacity=1).set_z_index(0) for p in all_parts]
        for i in which_parts:
            parts[i].set_fill(G_FIG_FILL_1).set_stroke(G_FIG_STROKE_1).set_z_index(1) 
        symbols = [
                    MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", color=TEX_COLOR1),
                    MathTex(f"{{{c}}}", r'\times', f"{{{m}}}", r'\over', f"{{{c}}}", r'\times', f"{{{n}}}", color=TEX_COLOR1),
                    MathTex(f"{{{int(c*m)}}}", r'\over', f"{{{int(c*n)}}}", color=TEX_COLOR1)
                ] if c != 1 else [MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", color=TEX_COLOR1)]*3
        for s in symbols:
            s.next_to(circle, direction=LEFT, buff=1)   

        VGroup(*all_parts).move_to(ORIGIN)
        VGroup(*parts).move_to(ORIGIN)
        circle.move_to(ORIGIN)
        VGroup(*div_dots).move_to(ORIGIN)
        VGroup(*outward_vecs).move_to(ORIGIN)
        VGroup(*gp_outward_vecs).move_to(ORIGIN)
        VGroup(*sec_lbls).move_to(ORIGIN)
        VGroup(*gp_lbls).move_to(ORIGIN)

        return {
            "all_parts" : all_parts,
            "parts" : parts,
            "symbols" : symbols,
            "vg_symbols" : VGroup(*symbols),
            "sec_lbls" : sec_lbls,
            "gp_lbls" : gp_lbls,
            "circle" : circle,
            "markers" : div_dots,
            "vectors" :outward_vecs,
            "vectors_gp": gp_outward_vecs,
            "group" : VGroup(*all_parts, *parts, circle, VGroup(*div_dots), VGroup(*outward_vecs), VGroup(*gp_outward_vecs))
        }

