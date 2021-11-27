from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip
config.background_color="#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24
class FracNumberLine(Scene):
    def construct(self):
        frac_1by5 = self.create_frac_num_line(denominator=3, frac_font_sz=22, frac_seg_stroke_width=6, frac_seg_color=MY_MERCURY)
        #display plain line
        dummy = frac_1by5.get("dummy_num_line")
        wticks = frac_1by5.get("ticks_for_whole")
        fticks = frac_1by5.get("ticks_for_frac")
        wlbl = frac_1by5.get("label_for_whole")
        flbl = frac_1by5.get("label_for_frac")
        fsegs = frac_1by5.get("frac_segments")
        self.play(GrowFromPoint(dummy, dummy.get_left()), run_time= 2)

        #define one unit
        self.play(FadeIn(wticks[0]))
        self.play(FadeIn(wlbl[0]))
        self.play(FadeIn(wticks[1]))
        self.play(FadeIn(wlbl[1]))

        #display other whole numbers
        for i in range(2, len(wticks), 1):
            self.play(FadeIn(wticks[i]), run_time=1/2**i)
            self.play(FadeIn(wlbl[i]), run_time=1/2**i) 
        
        self.wait(2)

        self.play(FadeIn(fticks[1]))
        self.play(FadeIn(fticks[2]))

        for i in range(3, len(fticks), 1):
            self.play(FadeIn(fticks[i]), run_time=2**3/2**i)

        self.wait(2)

        #explain 1/3
        #1/3 is the length of one part when 1 unit is divided into 3 equal parts
        #
        self.play(GrowFromPoint(fsegs[0], fsegs[0].get_left()))
        self.wait(2)
        self.play(GrowFromPoint(fsegs[4], fsegs[4].get_left()))
        self.wait(2)
        self.play(GrowFromPoint(fsegs[6], fsegs[6].get_left()))
        self.wait(2)
        self.play(GrowFromPoint(fsegs[8], fsegs[8].get_left()))
        self.wait(2)

        self.play(FadeOut(fsegs[0], fsegs[4], fsegs[6], fsegs[8]))

        #2/3 is the length of 2 such segments concatinated together
        #As long as the length is 2 parts of 1/3, it can be anywhere on the line
        s1 = self.get_single_segment(fticks=fticks, start_at=0, num_of_segs=2, stroke_width=6, with_tips=False)
        self.play(GrowFromPoint(s1, s1.get_left()), run_time=2)
        s2 = self.get_single_segment(fticks=fticks, start_at=5, num_of_segs=2, stroke_width=6, with_tips=False)
        self.play(GrowFromPoint(s2, s2.get_left()), run_time=2)
        s3 = self.get_single_segment(fticks=fticks, start_at=13, num_of_segs=2, stroke_width=6, with_tips=False)
        self.play(GrowFromPoint(s3, s3.get_left()), run_time=2)
        self.wait(5)
        self.play(FadeOut(s1,s2,s3))

        s1a = self.get_single_segment(fticks=fticks, start_at=0, num_of_segs=3, stroke_width=6, with_tips=False)
        s2a = self.get_single_segment(fticks=fticks, start_at=5, num_of_segs=3, stroke_width=6, with_tips=False)
        s3a = self.get_single_segment(fticks=fticks, start_at=15, num_of_segs=3, stroke_width=6, with_tips=False)
        self.play(GrowFromPoint(s1a, s1a.get_left()), run_time=2)
        self.play(GrowFromPoint(s2a, s2a.get_left()), run_time=2)
        self.play(GrowFromPoint(s3a, s3a.get_left()), run_time=2)
        self.wait(5)
        self.play(FadeOut(s1a, s2a, s3a))

        s1b = self.get_single_segment(fticks=fticks, start_at=0, num_of_segs=5, stroke_width=6, with_tips=False)
        s2b = self.get_single_segment(fticks=fticks, start_at=5, num_of_segs=5, stroke_width=6, with_tips=False, the_color=MY_RED)
        s3b = self.get_single_segment(fticks=fticks, start_at=13, num_of_segs=5, stroke_width=6, with_tips=False)
        self.play(GrowFromPoint(s1b, s1b.get_left()), run_time=2)
        self.play(GrowFromPoint(s2b, s2b.get_left()), run_time=2)
        self.play(GrowFromPoint(s3b, s3b.get_left()), run_time=2)
        self.wait(5)

        path1 = ArcBetweenPoints(start=s2b.get_center(), end=s1b.get_center()+UP*0.3)
        path2 = ArcBetweenPoints(start=s3b.get_center(), end=s1b.get_center()+UP*0.6, radius=10)
        self.play(MoveAlongPath(s2b, path1), run_time=3)
        self.play(MoveAlongPath(s3b, path2), run_time=5)


    def create_frac_num_line(self,
        denominator=3,
        unit=MY_UNIT_SIZE,
        last_whole_num=6,
        color=GOLD,
        tip_set_len=0.5,
        frac_font_sz=MY_FRAC_FONT_SIZE,
        frac_seg_stroke_width=4,
        frac_seg_color=GOLD,
    ):
        f1 = NumberLine(
            [0, last_whole_num, 1],
            unit_size=unit,
            include_ticks=False, 
            include_tip=False,
            color=color
        )

        ticks_cnt = last_whole_num + 1
        long_ticks = [None]*ticks_cnt
        for i in range(0, len(long_ticks), 1):
            long_ticks[i] = f1.get_tick(i, size=0.2)


        ticks_cnt1 = last_whole_num * denominator + 1
        short_ticks = [None]*ticks_cnt1
        for i in range(0, len(short_ticks), 1):
            short_ticks[i] = f1.get_tick(i/denominator)
        
        tip_seg = Line(f1.get_right(), f1.get_right() + [tip_set_len, 0, 0], color=color, stroke_width=f1.get_stroke_width())
        tip_arrow= ArrowTriangleFilledTip(start_angle=0, color=color)
        tip_arrow.next_to(tip_seg,RIGHT,buff=0)
        right_end = VGroup(tip_seg, tip_arrow)

        f2 = NumberLine(
            [0, last_whole_num, 1],
            length=f1.get_length() + tip_seg.get_length() + tip_arrow.length,
            unit_size=unit,
            include_ticks=False, 
            include_tip=True,
            color=color
        )

        f2.align_to(f1, LEFT)

        lbl_nums = [None] * ticks_cnt
        for i in range(0, len(lbl_nums), 1):
            lbl_nums[i] = f1.get_number_mobject(i)

        frac_lbls = [None] * ticks_cnt1
        for i in range(0, len(frac_lbls), 1):
            lbl = MathTex(f"\\frac{{{i}}}{{{denominator}}}")
            lbl.next_to(short_ticks[i], UP, buff=-0.1)
            lbl.font_size=frac_font_sz
            frac_lbls[i] = lbl

        frac_segs = [None]*(ticks_cnt1-1)
        for i in range(0, len(frac_segs), 1):
            seg = Line(
                f1.number_to_point(i/denominator), 
                f1.number_to_point((i+1)/denominator), 
                stroke_width=frac_seg_stroke_width,
                color=frac_seg_color
            )
            frac_segs[i] = seg

        gp = {
            "the_line": f1,
            "right_end": right_end,
            "dummy_num_line":f2,
            "ticks_for_whole":long_ticks,
            "ticks_for_frac": short_ticks,
            "label_for_whole": lbl_nums,
            "label_for_frac": frac_lbls,
            "frac_segments": frac_segs,

        }

        return gp
        
        #longseg = self.highlight_single_seg(6, 20, frac_segs, tip_color=TEAL)
        #longseg.shift(UP*0.5)
        #self.add(f1, *short_ticks, tip_seg, tip_arrow, *lbl_nums, *long_ticks, vg, b, longseg)
        #self.add(f1, *short_ticks, tip_seg, tip_arrow, *lbl_nums, *long_ticks, vg)
        #self.play(GrowFromPoint(longseg, point=longseg.get_left()), run_time=4)

    def get_segments(self, start_numerator, end_numerator, frac_segs):
        vg = VGroup()
        for i in range(start_numerator, end_numerator, 1):
            vg.add(frac_segs[i])
        return vg

    def get_single_segment(self, fticks, start_at=0, num_of_segs=1, the_color=MY_MERCURY, stroke_width=3, with_tips=True, tip_color=RED):
        seg = Line(fticks[start_at].get_center(), fticks[start_at + num_of_segs].get_center(), stroke_width=stroke_width, color=the_color)
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
    start_at: Starting position of the brace. For the number line displaying multiples of 1/3, start_at=4 will start the
    brace at position 4/3.
    num_of_segs: the numerator of the fraction
    """
    def get_brace(self, fticks, start_at=0, num_of_segs=1):
        return BraceBetweenPoints(fticks[start_at].get_center(), fticks[start_at + num_of_segs].get_center(), direction=UP)




