from manim import *

from CONSTANTS import *

class FracIntroIntro(Scene):
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

        self.play_can_you_add(1,2, 1,4, 3)



    def play_can_you_add(self, m, n, k, l, v_shift):
        f1dt = self.get_frac_illustration(1,2,[0], radius=1)
        f2dt = self.get_frac_illustration(1,4,[3], radius=1)
        f2dt.get(GP_OF_ALL).next_to(f2dt.get(GP_OF_ALL))
        f1p = f1dt.get(SECTORS)
        f2p = f2dt.get(SECTORS)
        self.add(*f1p, *f2p)

        return

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
        parts = [p.copy().set_fill(BACKGROUND, opacity=0)
                    .set_stroke(color=G_FIG_STROKE_COLOR1, width=1.5)
                    .set_z_index(1) 
                for p in all_parts]
        for i in which_parts:
            parts[i].set_fill(G_FIG_FILL_COLOR1, opacity=1) \
                .set_stroke(G_FIG_STROKE_COLOR1) \
                .set_z_index(2) 

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



