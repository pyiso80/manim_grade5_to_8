import numpy as np
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
class FracNumberLine(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.5,
            zoomed_display_height=2.5,
            zoomed_display_width=14,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        self.play_number_line_intro()
        self.wait(2)
        # self.play_the_unit_and_multiples()
        # self.wait(2)
        # self.play_one_third()
        # self.wait(5)

    def play_number_line_intro(self):
        number_line = self.create_rational_number_line(
            denominator = 3,
            unit = MY_UNIT_SIZE/2,
            left_end = -6,
            right_end = 6, 
            frac_font_sz=14, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012)
        #display plain line
        dummy = number_line.get("dummy_num_line")
        the_line = number_line.get("the_line")
        wticks = number_line.get("ticks_for_whole")
        fticks = number_line.get("ticks_for_frac")
        wlbl = number_line.get("label_for_whole")
        flbl = number_line.get("label_for_frac")
        fsegs = number_line.get("frac_segments")
        wsegs = number_line.get("whole_segments")
        sign = number_line.get("sign")
        self.play(GrowFromCenter(dummy.move_to(ORIGIN), run_time= 2))
        self.play(FadeIn(VGroup(*wticks).shift(UP * 2), shift = UP * 2), lag_ratio = 0.1, run_time = 2)
        self.play(ApplyWave(VGroup(*wticks), run_time = 2))
        self.play(AnimationGroup(
            VGroup(*wticks).animate(lag_ratio=0.1, run_time=2).shift(DOWN * 2)
        ))
        # the_unit = wsegs[0].copy().move_to(ORIGIN)
        # unit_segs = [None] * len(wsegs)
        # for i in range(0, len(wsegs), 1):
        #     unit_segs[i] = the_unit.copy()
        
        # vg_unit_segs = VGroup(*unit_segs)
        # vg_unit_segs.shift(UP * 3)
        # self.play(FadeIn(vg_unit_segs, shift = UP * 1.5))

        # self.play(vg_unit_segs.animate.arrange(DOWN, center = False, buff = 0.2))

        # sl = list(reversed(unit_segs))
        # run_times = [None] * len(unit_segs)
        # run_times[0:3] = [0.7] * 3
        # run_times[3:6] = [0.5] * 3
        # run_times[6:9] = [0.3] * 3
        # run_times[9:12] = [0.2] * 3
        # for i in range(0, len(sl), 1):
        #     self.play(sl[i].animate.move_to(wsegs[i]), run_time = run_times[i])
        
        # self.play(FadeIn(wlbl[6], shift = UP))
        # self.play(FadeIn(*wlbl[7:13], shift = UP))

        # zoomed_camera = self.zoomed_camera
        # zoomed_display = self.zoomed_display
        # frame = zoomed_camera.frame
        # zoomed_display_frame = zoomed_display.display_frame

        # frame.move_to(wticks[9]).shift(RIGHT * 0.25)
        # frame.set_color(PURPLE)
        # zoomed_display_frame.set_color(PURPLE)
        # zoomed_display.move_to(ORIGIN).shift(UP * 2.7)

        # zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        # self.add_foreground_mobject(zd_rect)

        # unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        # self.play(Create(frame))
        # self.activate_zooming()

        # self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, run_time = 5)

        # scale_factor = [0.9, 0.9, 0]
        # self.play(
        #     zoomed_display.animate.scale(scale_factor), run_time = 2
        # )
        # self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        # #self.play(Uncreate(vg_unit_segs), FadeOut(*wticks), FadeOut(dummy), FadeOut(frame), FadeOut(*wlbl[6:13]), FadeOut(zoomed_display_frame), run_time = 4)
        # self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        # self.play(Uncreate(vg_unit_segs))
        # self.play(FadeOut(*wlbl[6:13]))
        # self.play(FadeOut(*wticks))
        # self.play(FadeOut(dummy))


    def play_the_unit_and_multiples(self):
        frac_1by5 = number_line = self.create_rational_number_line(
            left_end = 0,
            right_end = 6,
            frac_font_sz = 24,  
            frac_only = True)
        #display plain line
        dummy = frac_1by5.get("dummy_num_line")
        wticks = frac_1by5.get("ticks_for_whole")
        fticks = frac_1by5.get("ticks_for_frac")
        wlbl = frac_1by5.get("label_for_whole")
        flbl = frac_1by5.get("label_for_frac")
        fsegs = frac_1by5.get("frac_segments")
        self.play(GrowFromPoint(dummy, dummy.get_left()), run_time= 2)
        self.play(FadeIn(*wticks, *wlbl))
        br1 = self.get_brace(wticks)
        br1.shift(UP * 0.1)
        lbl1 = Text("[0, 1]", font_size = 24)
        lbl2 = Text("The Unit Segment", font_size = 24)
        lbl1.next_to(br1, direction = UP)
        lbl2.next_to(lbl1)
        self.play(FadeIn(br1, lbl1))
        self.play(Write(lbl2))
        self.play(Unwrite(lbl2), Unwrite(lbl1), FadeOut(br1))

        br1 = self.get_brace(wticks, num_of_segs = 2)
        br1.shift(UP * 0.1)
        lbl1 = Text("[0, 2]", font_size = 24)
        lbl2 = Text("This segment's length is two unit.", font_size = 24)
        lbl1.next_to(br1, direction = UP)
        lbl2.next_to(lbl1)
        self.play(FadeIn(br1, lbl1))
        self.play(Write(lbl2))
        self.play(Unwrite(lbl2), Unwrite(lbl1), FadeOut(br1))

        br1 = self.get_brace(wticks, num_of_segs = 5)
        br1.shift(UP * 0.1)
        lbl1 = Text("[0, 5]", font_size = 24)
        lbl2 = Text("5 unit segment", font_size = 24)
        lbl1.next_to(br1, direction = UP)
        lbl2.next_to(lbl1)
        self.play(FadeIn(br1, lbl1))
        self.play(Write(lbl2))
        self.play(Unwrite(lbl2), Unwrite(lbl1), FadeOut(br1))

        self.play(FadeOut(dummy, *wticks, *wlbl))

    def play_one_third(self):

        nl0 = number_line = self.create_rational_number_line(
            denominator = 2,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)

        nl1 = number_line = self.create_rational_number_line(
            denominator = 3,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)

        nl2 = number_line = self.create_rational_number_line(
            denominator = 4,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)

        nl3 = number_line = self.create_rational_number_line(
            denominator = 5,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)

        nl4 = number_line = self.create_rational_number_line(
            denominator = 6,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)
        #display plain line
        dummy = nl1.get("dummy_num_line")
        wticks = nl1.get("ticks_for_whole")
        fticks = nl1.get("ticks_for_frac")
        wlbl = nl1.get("label_for_whole")
        flbl = nl1.get("label_for_frac")
        fsegs = nl1.get("frac_segments")
        self.play(GrowFromPoint(dummy, dummy.get_left()), run_time= 2)
        self.play(FadeIn(*wticks, *wlbl))
        # self.wait()
        # self.play(FadeIn(*fticks[0:3], shift = UP))

        # self.play(FadeIn(fsegs[0], shift = DOWN))
        # self.play(FadeIn(flbl[1]))

        fticks = nl0.get("ticks_for_frac")
        fsegs = nl0.get("frac_segments")
        self.play(FadeIn(*fticks[0:2], shift = UP))
        self.play(FadeIn(*fsegs[0:2], shift = DOWN))
        self.play(VGroup(*fsegs[0:2]).animate.arrange(direction = UP, center = False))
        self.play(FadeOut(*fticks[0:2], shift = DOWN))
        self.play(FadeOut(*fsegs[0:2], shift = UP))
        self.wait()
        fticks = nl1.get("ticks_for_frac")
        fsegs = nl1.get("frac_segments")
        self.play(FadeIn(*fticks[0:3], shift = UP))
        self.play(FadeIn(*fsegs[0:3], shift = DOWN))
        self.play(VGroup(*fsegs[0:3]).animate.arrange(direction = UP, center = False))
        self.play(VGroup(*fsegs[0:3]).animate.arrange(direction = RIGHT, center = False, buff = 0))
        self.play(FadeOut(*fticks[0:3], *fsegs[0:3]))
        self.wait()
        fticks = nl2.get("ticks_for_frac")
        fsegs = nl2.get("frac_segments")
        self.play(FadeIn(*fticks[0:4], shift = UP))
        for x in fsegs[0:4]:
            self.play(FadeIn(x, shift = DOWN), run_time = 0.75)
        self.play(VGroup(*fsegs[0:4]).animate.arrange(direction = UP, center = False), run_time = 1.5)
        self.play(VGroup(*fsegs[0:4]).animate.arrange(direction = RIGHT, center = False, buff = 0), run_time = 2)
        self.play(FadeOut(*fticks[0:4], *fsegs[0:4]))


        # br1 = self.get_brace(fticks)
        # br1.shift(UP * 0.1)
        # lbl1 = MathTex(r"[0, \frac{1}{3}]", font_size = 24)
        # lbl2 = Tex(r"Segment of length {\Large $\frac{1}{3}$}", font_size = 24)
        # lbl1.next_to(br1, direction = UP)
        # lbl2.next_to(lbl1)
        # self.play(FadeIn(br1, lbl1))
        # self.play(Write(lbl2))
        # self.play(Unwrite(lbl2), Unwrite(lbl1), FadeOut(br1))


    def play_one_third_v2(self):
        frac_1by5 = number_line = self.create_rational_number_line(
            denominator = 3,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=14, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)
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

    def create_rational_number_line(
        self,
        denominator = 3,
        unit = MY_UNIT_SIZE,
        right_end = 3,
        left_end = -3,
        color = GOLD,
        tip_seg_factor = 0.5,
        frac_font_sz = MY_FRAC_FONT_SIZE,
        frac_seg_stroke_width = 4,
        frac_seg_color = GOLD,
        sign_vertical_alignment_factor = 0.015, #for 22 0.015
        frac_only = False
    ):
        f1 = NumberLine(
            [left_end, right_end, 1],
            unit_size = unit,
            include_ticks = False, 
            include_tip = False,
            color = color
        )

        ticks_cnt = right_end - left_end + 1
        long_ticks = [None] * ticks_cnt
        wnum = range(left_end, right_end + 1, 1)
        for i in range(0, len(long_ticks), 1):
            long_ticks[i] = f1.get_tick(wnum[i], size = 0.12)
            
        ticks_cnt1 = (right_end - left_end) * denominator + 1
        short_ticks = [None] * ticks_cnt1 
        n = np.linspace(left_end, right_end, ticks_cnt1)     
        for i in range(0, len(short_ticks), 1):
            short_ticks[i] = f1.get_tick(n[i], size = 0.07)

        f2 = None
        if not frac_only:
            ar1 = Arrow([0,0,0], f1.get_right() + RIGHT * tip_seg_factor, tip_length = 0.3, color = GOLD, stroke_width = 2, buff = 0)
            ar2 = Arrow([0,0,0], f1.get_left() + LEFT * tip_seg_factor, tip_length = 0.3, color = GOLD, stroke_width = 2, buff = 0)
            f2 = VGroup(ar1, ar2)
        else:
            ar1 = Arrow(f1.get_left(), f1.get_right() + RIGHT * tip_seg_factor, tip_length = 0.3, color = GOLD, stroke_width = 2, buff = 0)
            f2 = VGroup(ar1)

        lbl_nums = [None] * ticks_cnt
        n = range(left_end, right_end + 1, 1)
        for i in range(0, len(lbl_nums), 1):
            lbl_nums[i] = f1.get_number_mobject(n[i])

        frac_lbls = [None] * ticks_cnt1
        frac_sign = [None] * ticks_cnt1
        n = range(left_end * denominator, right_end * denominator + 1, 1)

        for i in range(0, len(frac_lbls), 1):
            sign = "-" if n[i] < 0 else ""
            msign = MathTex(f"{sign}")
            lbl = MathTex(f"\\frac{{{abs(n[i])}}}{{{denominator}}}")
            lbl.next_to(short_ticks[i], UP, buff=-0.1)
            lbl.font_size=frac_font_sz
            msign.font_size=frac_font_sz
            msign.move_to(lbl.get_center())
            msign.next_to(lbl, LEFT, buff=0.04)
            msign.shift(DOWN * sign_vertical_alignment_factor)
            frac_lbls[i] = lbl
            frac_sign[i] = msign

        frac_segs = [None]*(ticks_cnt1-1)
        for i in range(0, len(frac_segs), 1):
            seg = Line(
                f1.number_to_point(i/denominator), 
                f1.number_to_point((i+1)/denominator), 
                stroke_width=frac_seg_stroke_width,
                color=frac_seg_color
            )
            frac_segs[i] = seg

        whole_segs = [None]*(ticks_cnt-1)
        for i in range(0, len(whole_segs), 1):
            seg = Line(
                f1.number_to_point(wnum[i]), 
                f1.number_to_point(wnum[i + 1]), 
                stroke_width=frac_seg_stroke_width,
                color=frac_seg_color
            )
            whole_segs[i] = seg

        gp = {
            "the_line": f1,
            "right_end": right_end,
            "dummy_num_line":f2,
            "ticks_for_whole":long_ticks,
            "ticks_for_frac": short_ticks,
            "label_for_whole": lbl_nums,
            "label_for_frac": frac_lbls,
            "frac_segments": frac_segs,
            "whole_segments": whole_segs,
            "sign": frac_sign
        }

        return gp

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
        