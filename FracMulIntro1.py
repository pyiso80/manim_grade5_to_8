from manim import *
import numpy as np

config.background_color="#FDF6E3" # OLD PAPER: "#E0C9A6", PAPER WHITE: #F9FBFF, moleskin: FFF8DC
BACKGROUND = "#FDF6E3"
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


class FracMulIntro1(Scene):


    def construct(self):
        Circle.set_default(color=G_FIG_FILL_COLOR1, stroke_color=G_FIG_STROKE_COLOR1)
        Circle.set_default(stroke_width=G_FIG_STROKE_W1)
        MathTex.set_default(color=TEX_COLOR1, font_size=34)
        AnnularSector.set_default(color=G_FIG_FILL_COLOR1,
            stroke_color=G_FIG_STROKE_COLOR1,
            stroke_width= G_FIG_STROKE_W1)

        self.wait()
        self.play_mul_illu(2,3,10,7)
        self.clear()
        self.play_mul_illu(3,5,4,3)
        self.wait()


    def play_mul_illu(self, m, n, k, l):
        f1dt= self.get_frac_illustration(m, n, range(0,m),gp_sz1=1)
        f2dt= self.get_frac_illustration(m*l, n*l, range(0,m*l), gp_sz1=l, gp_sz2=m)  
        f1_rep = f1dt.get(SECTORS)
        f1_vgp = f1dt.get(GP_OF_ALL)
        f2_rep = f2dt.get(SECTORS)
        f2dt.get(GP_OF_ALL).move_to(f1_vgp)
        
        tex1_f1 = self.get_frac_tex(k, l)
        tex2_x = MathTex(r'\times') 
        tex3_f2 = self.get_frac_tex(m, n)
        tex4 = Tex("is defined as", 
                    f"{{{k}}}", 
                    "parts when", arg_separator=" ", font_size=34)
        tex5 = tex3_f2.copy()
        
        tex6 = Tex(f" is divided into", 
                    f"{{{l}}} equal parts.", arg_separator=" ", font_size=34)

        self.play(Write(VGroup(tex1_f1, tex2_x, tex3_f2, tex4, tex5, tex6)
            .arrange().shift(UP*3)))

        f1_tex = self.get_frac_tex(m,n)                   
        self.play(FadeIn(*f1_rep, f1_tex.next_to(f1_vgp, direction=LEFT, buff=2)))
        self.play(FadeOut(f1_tex))
       
        ##### divide n/n into n*l/n*l       
        gp_of_l = np.array(f2_rep).reshape(-1, l)
        for i in range(0,n):
            self.play(FadeIn(*gp_of_l[i]), run_time=0.1)
            self.wait()

        self.remove(*f1_rep)

        ##### emphasize each parts of n/n,  each having l parts
        n_gp = [VGroup(*gp_of_l[i]) for i in range(0, n)]
        v_gp1 = [l.get_unit_vector() for l in f2dt.get(SEC_GP1_BISECTORS)]
        self.play(AnimationGroup(
            *[g.animate().shift(v*0.05) for g, v in zip(n_gp, v_gp1)]
        ))
        self.wait()
        self.play(AnimationGroup(
            *[g.animate().shift(-v*0.05) for g, v in zip(n_gp, v_gp1)]
        ))

        ##### display labels m*l parts  
        self.play(FadeIn(*f2dt.get(SEC_LBLS)[0:m*l]))
        self.wait(3)

        ##### emphasize l equal parts of m/n by moving outward from the center
        shift_val = [0.1] * n*l
        v_gp = [l.get_unit_vector() for l in f2dt.get(SEC_GP2_BISECTORS)]
        sz = int(len(f2_rep)/m)*m # for reshaping, only take multiple of m
        l_eq_vgp = [VGroup(*g) for g in  np.array(f2_rep)[0:sz].reshape(-1, m)]
        self.play(AnimationGroup(
            *[g.animate().shift(v*sv) for g, v, sv in zip(l_eq_vgp[0:l], v_gp, shift_val)]
        ))
        
        #### display labels of each of l equal parts
        sec_gp2_lbl = f2dt.get(SEC_GP_LBLS)
        sec_lbl = f2dt.get(SEC_LBLS)
        self.play(FadeIn(*sec_gp2_lbl[0:l], shift=RIGHT, run_time=1.5),
                    FadeOut(*sec_lbl[0:m*l], shift=LEFT, run_time=1))
        self.wait(2)

        ##### emphasize only k parts if k < l
        ##### emphasize up to l parts first if k > l
        up_to = l if k > l else k
        self.play(
            FadeIn(*l_eq_vgp[0:up_to], lag_ratio=1), 
            AnimationGroup(
                *[Flash(l, scale_value=1.7, color=IND_COLOR1, line_stroke_width=IND_STROKE_W1) 
                    for l in sec_gp2_lbl[0:up_to]])
        )

        ##### emphasize remaining parts whe k > l
        if k > l:
            gp_left = l_eq_vgp[l:k]
            for g, v, sv in zip(gp_left, v_gp[l:k], shift_val) :
                g.generate_target()
                g.target.set_fill(G_FIG_FILL_COLOR1, opacity=1)
                g.target.shift(v*sv)
            self.play(
                AnimationGroup(*[Transform(g, g.target) for g in gp_left]),
                FadeIn(*sec_gp2_lbl[l:k], lag_ratio=1), 
                AnimationGroup(*[Flash(l, scale_value=1.7, color=IND_COLOR1, 
                    line_stroke_width=IND_STROKE_W1) for l in sec_gp2_lbl[l:k]])
            )

        ##### De-emphasize remaining if k < l
        if k < l:
            gp_left_deemp =  l_eq_vgp[k:l]
            for g, v, sv in zip(gp_left_deemp, v_gp[k:l], shift_val) :
                g.generate_target()
                g.target.set_fill(G_FIG_FILL_COLOR1, opacity=0.25)
                g.target.shift(-v*sv)
            self.play(AnimationGroup(*[Transform(g, g.target) for g in gp_left_deemp]),
                FadeOut(*sec_gp2_lbl[k:l], lag_ratio=1))           

        self.play(FadeOut(*sec_gp2_lbl[0:k], shift=LEFT))
        exp = self.get_frac_tex_1(k, l, m, n)
        equal = MathTex('=', color=TEX_COLOR1)
        exp2 = self.get_frac_tex(k*m, l*n)
        VGroup(exp, equal, exp2).arrange().next_to(f2dt.get(GP_OF_ALL), direction=LEFT, buff=1)

        self.play(Write(VGroup(*exp.submobjects[0:3])))#5x2
        self.play(Write(VGroup(equal, exp2[0])), 
            FadeIn(*sec_lbl[0:k*m], lag_ratio=0.5, run_time=2))
        self.play(FadeOut(*sec_lbl[0:k*m]))

        self.play(FadeIn(exp.submobjects[3], shift=RIGHT), 
            Write(exp[4:]), 
            FadeIn(*sec_lbl, lag_ratio=0.5, run_time=2))
        self.play(FadeIn(exp2[1], shift=RIGHT),Write(exp2[2]))
        self.wait(3)
        

    def get_frac_illustration(self, m, n, which_parts, radius=1.5, gp_sz1=1, gp_sz2=1, 
        diff_radius = 0.5):
        """
        m: numerator of fraction
        n: denominator
        which_parts: parts to be highlighted
        gp_sz1: number of sectors to be grouped together (for illustrating m÷c/n÷c)
        gp_sz2: number of sectors to be grouped together (for illustrating m/n x 1/l)
        """
        circle = Circle(radius=radius, fill_opacity=1)
        outer_circle = Circle(radius=radius+diff_radius, fill_opacity=1)
        arc_len = 2*PI/n

        #dots and points on the start and end points of the arc of the sectors
        div_dots = [Dot().move_to(p) for p in 
            [circle.point_at_angle(arc_len * i) for i in range(0, n)]]
        VGroup(*div_dots).rotate(angle=PI/2, about_point=circle.get_center())
        div_pts = [d.get_center() for d in div_dots]

        #dots and points on the mid points of the arc of the sectors
        mid_pt_dots = [Dot().move_to(circle.point_at_angle(arc_len * i)) 
                        for i in range(0, n)]
        VGroup(*mid_pt_dots).rotate(angle=PI/2+ (arc_len/2.0))
        mid_pts = [d.get_center() for d in mid_pt_dots ]
        sec_bisectors = [Line(circle.get_center(), p) for p in mid_pts]

        gp1_mid_dots = [Dot().move_to(circle.point_at_angle(i * arc_len*gp_sz1)) 
            for i in range(0, int(n/gp_sz1))]
        VGroup(*gp1_mid_dots).rotate(angle=PI/2+ arc_len*gp_sz1/2.0)
        gp1_mid_pts = [d.get_center() for d in gp1_mid_dots]
        gp1_bisectors = [Line(circle.get_center(), p) for p in gp1_mid_pts]

        gp2_mid_dots = [Dot().move_to(circle.point_at_angle(i * arc_len*gp_sz2)) 
            for i in range(0, int(n/gp_sz2))]
        VGroup(*gp2_mid_dots).rotate(angle=PI/2+ arc_len*gp_sz2/2.0)
        gp2_mid_pts = [d.get_center() for d in gp2_mid_dots]
        gp2_bisectors = [Line(circle.get_center(), p) for p in gp2_mid_pts]


        sec_num_pos = [Dot().move_to(outer_circle.point_at_angle(i*arc_len)) 
            for i in range(0, n)]
        VGroup(*sec_num_pos).rotate(angle=PI/2 + (arc_len/2.0))
        sec_num_pts = [d.get_center() for d in sec_num_pos]
        sec_lbls = [MathTex(i+1, font_size=18).move_to(p)
                        for p,i in zip(sec_num_pts, range(0, n))] 

        gp2_lbl_dots = [Dot().move_to(outer_circle.point_at_angle(i * arc_len*gp_sz2)) 
            for i in range(0, int(n/gp_sz2))]
        VGroup(*gp2_lbl_dots).rotate(angle=PI/2+ arc_len*gp_sz2/2.0)
        gp2_lbl_pts = [d.get_center() for d in gp2_lbl_dots]
        gp2_lbls = [MathTex(i+1, font_size=18).move_to(p)
                    for p,i in zip(gp2_lbl_pts, range(0, int(n/gp_sz2)))]       

        all_parts = [
            AnnularSector(
                inner_radius=0, 
                outer_radius=radius, 
                angle=arc_len, 
                start_angle=(PI/2 + i * arc_len))
            for i in range(0, n)]    
        parts = [p.copy().set_fill(BACKGROUND).set_stroke(color=G_FIG_STROKE_COLOR1, width=1.5, 
            opacity=1).set_z_index(1) for p in all_parts]
        for i in which_parts:
            parts[i].set_fill(G_FIG_FILL_COLOR1).set_stroke(G_FIG_STROKE_COLOR1).set_z_index(2) 

        VGroup(*all_parts).move_to(ORIGIN)
        VGroup(*parts).move_to(ORIGIN)
        circle.move_to(ORIGIN)
        VGroup(*div_dots).move_to(ORIGIN)
        VGroup(*sec_bisectors).move_to(ORIGIN)
        VGroup(*sec_lbls).move_to(ORIGIN)
        VGroup(*gp2_bisectors).move_to(ORIGIN)
        VGroup(*gp1_bisectors).move_to(ORIGIN)
        VGroup(*gp2_lbls).move_to(ORIGIN)
        return {
            SECTORS : parts,
            SEC_LBLS : sec_lbls,
            SEC_GP_LBLS : gp2_lbls,
            SEC_GP1_BISECTORS: gp1_bisectors,
            SEC_GP2_BISECTORS: gp2_bisectors,
            GP_OF_ALL : VGroup(*all_parts, *parts, circle, VGroup(*div_dots), 
                VGroup(*sec_bisectors), VGroup(*gp1_bisectors), VGroup(*gp2_bisectors))
        }


    def get_frac_tex(self, m, n, font_sz=34):
        return MathTex(f"{{{m}}}", r'\over', f"{{{n}}}", font_size=font_sz)


    def get_frac_tex_1(self, k, l, m, n, font_sz=34):
        return MathTex(f"{{{k}}}", r'\times', f"{{{m}}}", r'\over', f"{{{l}}}", r'\times',
            f"{{{n}}}")


