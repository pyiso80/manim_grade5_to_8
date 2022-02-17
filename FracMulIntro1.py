from manim import *

config.background_color="#FFFBEF"
BACKGROUND = "#FFFBEF"
G_FIG_FILL_1 = TEAL
G_FIG_STROKE_1= "#5E5E5E" #Main
G_FIG_STROKE_2= "#A9A9A9" #Dimmed
IND_COLOR = "#FF2600"
IND_LINE_W = 1.5
TEX_COLOR1 = "#212121"



class FracMulIntro1(Scene):
    left_alignment_point = Point().shift(LEFT*6)
    def construct(self):
        self.wait()
        self.play_mul_illu(2,3,5,7)
        self.clear()
        self.play_mul_illu(3,5,4,3)
        #self.play(Create(Sector().set_fill(color=BLACK)))
        self.wait()

    def play_mul_illu(self, m, n, k, l):
        f1dt= self.get_frac_illustration(m, n, range(0,m),sec_per_group=1)
        f1_rep = f1dt.get("parts")
        f1_tex = f1dt.get("symbols")[0]
        f1_vgp = f1dt.get("group")

        f2dt= self.get_frac_illustration(m*l, n*l, range(0,m*l), sec_per_group=m)
        f2_rep = f2dt.get("parts")

        f2dt.get("group").move_to(f1_vgp)
        f1dt.get("vg_symbols").next_to(f1_vgp, buff=0.5, direction=DOWN)
        
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
                            
        self.play(FadeIn(*f1_rep, f1_tex.next_to(f1_vgp, direction=LEFT, buff=2)))
       
        ##### divide n/n into n*l/n*l
        self.play(FadeOut(f1_tex))
        for i in range(0,n):
            self.play(FadeIn(*f2_rep[i*l: (i+1)*l ]), run_time=0.1)
            self.wait()

        self.remove(*f1_rep)

        ###
        # emphasize each parts of n/n,  each having l parts

        # group l parts in each of n parts (eg for 5/7 x 2/3, each parts of 3/3 divided into 7 parts)
        n_gp = [VGroup(*f2_rep[i*l:i*l+l]) for i in range(0, n)]
        self.play(AnimationGroup(
            *[g.animate().shift(v.get_unit_vector()*0.05) for g, v in zip(n_gp, f1dt.get("vectors"))]
        ))
        self.wait()
        self.play(AnimationGroup(
            *[g.animate().shift(-v.get_unit_vector()*0.05) for g, v in zip(n_gp, f1dt.get("vectors"))]
        ))

        ###
        # For m/n, there are m*l equal parts  
        self.play(FadeIn(*f2dt.get("sec_lbls")[0:m*l]))
        self.wait(3)

        ###
        # emphasize l equal parts of m/n by moving outward from the center
        # (m*l parts are l equal group, each group having m parts)  
        shift_val = [0.1] * n*l
        v_gp = f2dt.get("vectors_gp")
        l_gp = [VGroup(*f2_rep[i*m:i*m+m]) for i in range(0,l)]
        self.play(AnimationGroup(
            *[g.animate().shift(v.get_unit_vector()*sv) for g, v, sv in zip(l_gp, v_gp, shift_val)]
        ))
        
        self.play(FadeIn(*f2dt.get("gp_lbls")[0:l], shift=RIGHT, run_time=1.5),
                    FadeOut(*f2dt.get("sec_lbls")[0:m*l], shift=LEFT, run_time=1))
        self.wait(2)

        ###
        # emphasize only k parts if k < l
        # emphasize up to l parts first if k > l
        up_to = l if k > l else k
        self.play(
            FadeIn(*l_gp[0:k], lag_ratio=1), 
            AnimationGroup(
                *[Flash(l, scale_value=1.7, color=IND_COLOR, line_stroke_width=IND_LINE_W) 
                    for l in f2dt.get("gp_lbls")[0:up_to]])
        )

        ###
        # emphasize remaining parts whe k > l
        if k > l:
            l_gp1 = [VGroup(*f2_rep[i*m:i*m+m]) for i in range(l,k)]
            self.play(AnimationGroup(
                *[g.animate().shift(v.get_unit_vector()*sv) for g, v, sv in zip(l_gp1, v_gp[l:k], shift_val)]
            ), run_time=0.5)
            self.play(AnimationGroup(
                        *[Transform(s, s.copy().set_fill(G_FIG_FILL_1, opacity=1)) for s in f2_rep[m*l:k*l]]
                ), 
                FadeIn(*f2dt.get("gp_lbls")[l:k], lag_ratio=1), 
                AnimationGroup(
                    *[Flash(l, scale_value=1.7, color=IND_COLOR, line_stroke_width=IND_LINE_W) 
                        for l in f2dt.get("gp_lbls")[l:k]]))

        ###
        # De-emphasize remaining if k < l
        if k < l:
            l_gp2 = [VGroup(*f2_rep[i*m:i*m+m]) for i in range(k,l)]
            self.play(AnimationGroup(
                *[g.animate().shift(-v.get_unit_vector()*sv) for g, v, sv in zip(l_gp2, v_gp[k:l], shift_val)]
            ), run_time=0.5)
            self.play(AnimationGroup(
                        *[Transform(s, s.copy().set_fill(color=G_FIG_FILL_1,opacity=0.2)) for s in f2_rep[k*m:m*l]]
                ), 
                FadeOut(*f2dt.get("gp_lbls")[k:l], lag_ratio=1))

        self.play(FadeOut(*f2dt.get("gp_lbls")[0:k], shift=LEFT))
        exp = MathTex(f"{{{k}}}", r'\times', f"{{{m}}}", r'\over', f"{{{l}}}", r'\times', f"{{{n}}}", color=TEX_COLOR1)
        equal = MathTex('=', color=TEX_COLOR1)
        exp2 = MathTex(f"{{{int(k*m)}}}", r'\over', f"{{{int(l*n)}}}", color=TEX_COLOR1)
        VGroup(exp, equal, exp2).arrange().next_to(f2dt.get("group"), direction=LEFT, buff=1)

        self.play(Write(VGroup(*exp.submobjects[0:3])))#5x2
        self.play(Write(VGroup(equal, exp2[0])), FadeIn(*f2dt.get("sec_lbls")[0:k*m], lag_ratio=0.5, run_time=2))# = 10, 1,2,3, ... 10
        self.play(FadeOut(*f2dt.get("sec_lbls")[0:k*m]))

        self.play(FadeIn(exp.submobjects[3], shift=RIGHT), Write(exp[4:]), FadeIn(*f2dt.get("sec_lbls"), lag_ratio=0.5, run_time=2))
        self.play(FadeIn(exp2[1], shift=RIGHT),Write(exp2[2]))
        

        self.wait(3)
        


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

