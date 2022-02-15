import numpy as np
from manim import *
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
        # self.play_number_line_intro()
        # self.wait(2)
        # self.play_the_unit_and_multiples()
        # self.wait(2)
        self.play_dividing_the_unit()
        self.play_frac_example(3,5)
        self.play_frac_example(5,8)
        #self.play_1half_to_1fifth()
        self.play(FadeIn(Text(f"သင်္ချာသင်ခန်းစာများ", font="Pyidaungsu").shift(UP * 2)))
        self.wait(2)

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
        ar1 = number_line.get("right_arrow")
        ar2 = number_line.get("left_arrow")
        self.play(GrowFromCenter(dummy.move_to(ORIGIN), run_time= 2))
        self.play(FadeIn(VGroup(*wticks).shift(UP * 2), shift = UP * 2), lag_ratio = 0.1, run_time = 2)
        self.play(ApplyWave(VGroup(*wticks), run_time = 2))
        self.play(AnimationGroup(
            VGroup(*wticks).animate(lag_ratio=0.1, run_time=2).shift(DOWN * 2)
        ))

        self.alternate_color(wsegs, MY_GRAY, MY_RED)
        ws1 = VGroup(*wsegs.copy())
        # self.play(FadeIn(ws1.shift(UP * 2), shift = UP * 2), lag_ratio = 0.3, run_time = 2)
        ws1.arrange(buff = 0.2, direction = UP, center = False)
        ws1.shift(UP * 1.5)
        self.play(FadeIn(ws1, shift = RIGHT, lag_ratio=0.1))
        self.play(ws1.animate(lag_ratio=0.1, run_time=2).arrange(buff = 0.0, direction = RIGHT, center = True))       
        self.play(ws1.animate(lag_ratio=0.1, run_time=2).arrange(buff = 0.2, direction = UP, center = False).shift(UP * 1.5))
        
        self.play(FadeIn(wlbl[6], shift = UP))
        self.play(Indicate(wlbl[6]))
        self.play(FadeIn(VGroup(*wlbl[7:13]), shift = UP), lag_ratio = 0.1, run_time = 2)

        fr = Rectangle(color = BLUE, height = 2, width = MY_UNIT_SIZE/2 * 7)
        fr.align_to(wlbl[6], direction = LEFT).shift(LEFT * 0.25)
        self.play(GrowFromCenter(fr))

        only_frac = number_line = self.create_rational_number_line(
            left_end = 0,
            right_end = 6,
            frac_font_sz = 24,  
            frac_only = True)
        #display plain line
        dummy1 = only_frac.get("dummy_num_line")
        wticks1 = only_frac.get("ticks_for_whole")
        fticks1 = only_frac.get("ticks_for_frac")
        wlbl1 = only_frac.get("label_for_whole")
        flbl1 = only_frac.get("label_for_frac")
        fsegs1 = only_frac.get("frac_segments")
        wsegs1 = number_line.get("whole_segments")

        fr1 = Rectangle(color = BLUE, height = 3, width = MY_UNIT_SIZE/2 * 13.5)
        self.play(
            FadeTransform(fr, fr1, stretch=True, dim_to_match=1), 
            FadeTransform(ar1, dummy1, dim_to_match=1),
            FadeTransformPieces(VGroup(*wlbl[6:13]), VGroup(*wlbl1), stretch=True, dim_to_match=1),
            FadeTransformPieces(VGroup(*wticks[6:13]), VGroup(*wticks1), stretch=True, dim_to_match=1),
            FadeOut(ws1, ar2, *wticks[0:6], shift = LEFT, run_time = 0.5),
            run_time = 2)

        self.play(FadeOut(fr1))
        

    def play_the_unit_and_multiples(self):
        prev_mobjs = self.mobjects
        number_line = self.create_rational_number_line(
            left_end = 0,
            right_end = 6,
            frac_font_sz = 24,  
            frac_only = True)
        #display plain line
        dummy = number_line.get("dummy_num_line")
        wticks = number_line.get("ticks_for_whole")
        wlbl = number_line.get("label_for_whole")
        wsegs = number_line.get("whole_segments")
        self.play(FadeIn(dummy, *wticks, *wlbl), run_time = 0.5)
        self.remove(*prev_mobjs)


        u1 = self.get_single_segment(wticks, start_at=0, num_of_segs=1, stroke_width=6, with_tips=False)
        lbl1 = Text("[0, 1]", font_size = 24)
        lbl2 = Text("The Unit Segment", font_size = 24)
        lbl1.next_to(u1, direction = UP, buff=0.5)
        lbl2.next_to(lbl1, direction = UP)
        self.play(GrowFromEdge(u1, edge = LEFT))
        self.play(Wiggle(u1, scale_value=1))
        self.play(FadeIn(lbl1, shift = DOWN))
        self.play(Wiggle(lbl1))
        self.play(AddTextLetterByLetter(lbl2))
        self.play(Wiggle(lbl1))
        self.play(FadeOut(lbl1, lbl2, u1))

        u2 = self.get_single_segment(wticks, start_at=0, num_of_segs=2, stroke_width=6, with_tips=False)
        lbl1 = Text("[0, 2]", font_size = 24)
        lbl2 = Text("The length of this line segment is 2 units.", font_size = 24)
        lbl1.next_to(u2, direction = UP, buff=0.5)
        lbl2.next_to(lbl1, direction = UP)
        self.play(GrowFromEdge(u2, edge = LEFT))
        self.play(Wiggle(u2, scale_value=1))
        self.play(FadeIn(lbl1, shift = DOWN))
        self.play(Wiggle(lbl1))
        self.play(AddTextLetterByLetter(lbl2))
        self.play(Wiggle(lbl1))
        self.play(FadeOut(lbl1, lbl2, u2))

        u5 = self.get_single_segment(wticks, start_at=0, num_of_segs=5, stroke_width=6, with_tips=False)
        lbl1 = Text("[0, 5]", font_size = 24)
        lbl2 = Text("The length of this line segment is 5 units.", font_size = 24)
        lbl1.next_to(u5, direction = UP, buff=0.5)
        lbl2.next_to(lbl1, direction = UP)
        self.play(GrowFromEdge(u5, edge = LEFT))
        self.play(Wiggle(u5, scale_value=1))
        self.play(FadeIn(lbl1, shift = DOWN))
        self.play(Wiggle(lbl1))
        self.play(AddTextLetterByLetter(lbl2))
        self.play(Wiggle(u5, scale_value=1))
        self.play(FadeOut(lbl1, lbl2, u5))


    def play_dividing_the_unit(self):
        denominators = [2, 3, 4, 5]
        num_lines = [None] * len(denominators)
        for deno, i in zip(denominators, range(0, len(num_lines))):
            num_lines[i] =  self.create_rational_number_line(
                        denominator = deno,
                        unit = MY_UNIT_SIZE,
                        left_end = 0,
                        right_end = 6, 
                        frac_font_sz=MY_FRAC_FONT_SIZE, 
                        frac_seg_stroke_width=6, 
                        frac_seg_color=MY_MERCURY,
                        sign_vertical_alignment_factor = 0.012,
                        frac_only = True)

        prev_mobjs = self.mobjects
        #display plain line
        dummy = num_lines[0].get("dummy_num_line")
        wticks = num_lines[0].get("ticks_for_whole")
        wlbl = num_lines[0].get("label_for_whole")
        wsegs = num_lines[0].get("whole_segments")
        self.play(FadeIn(dummy, *wticks, *wlbl), run_time = 0.5)
        self.remove(*prev_mobjs)

        b1 = self.get_brace(wticks)
        b1l = Tex("Segment of 1 unit length", font_size = 28)
        b1l.next_to(b1, direction=UP)
        self.play(GrowFromEdge(wsegs[0], edge=LEFT), FadeIn(b1), FadeIn(b1l))
        self.play(VGroup(wsegs[0], b1, b1l).animate().shift(UP*1.5))
        for nl, d in zip(num_lines, denominators):
            ts = Tex(f"{d} parts of equal length", font_size = 28)
            tcks = nl.get("ticks_for_frac")
            fsegs = nl.get("frac_segments")
            tcks1 = VGroup(*tcks[1:d])
            self.play(FadeIn(tcks1, shift=DOWN))
            fs1 = VGroup(*fsegs[0:d])
            self.play(AnimationGroup(*[
                GrowFromEdge(s, edge=LEFT)
                for s in fs1
            ]), run_time = 1)
            fs1.arrange(buff = 0.2, direction = DOWN, center = False).shift(UP * 1.2)
            ts.next_to(fs1).shift(RIGHT * 0.7)
            fs1.arrange(buff = 0.0, direction = RIGHT, center = False).shift(DOWN*1.2)
            self.play(fs1.animate(lag_ratio=0.1).arrange(buff = 0.2, direction = DOWN, center = False).shift(UP * 1.2), FadeIn(ts))
            self.play(fs1.animate(lag_ratio=0.1).arrange(buff = 0.0, direction = RIGHT, center = False), FadeOut(ts))       
            self.play(FadeOut(fs1), FadeOut(tcks1), lag_ratio = 0.1)

    def play_frac_example(self, deno, numer):
        prev_mobjs = self.mobjects
        num_line = self.create_rational_number_line(
            denominator = deno,
            unit = MY_UNIT_SIZE,
            left_end = 0,
            right_end = 6, 
            frac_font_sz=MY_FRAC_FONT_SIZE, 
            frac_seg_stroke_width=6, 
            frac_seg_color=MY_MERCURY,
            sign_vertical_alignment_factor = 0.012,
            frac_only = True)
        dummy = num_line.get("dummy_num_line")
        wticks = num_line.get("ticks_for_whole")
        fticks = num_line.get("ticks_for_frac")
        wlbl = num_line.get("label_for_whole")
        flbl = num_line.get("label_for_frac")
        wsegs = num_line.get("whole_segments")
        fsegs = num_line.get("frac_segments")
        self.play(FadeIn(dummy, *wticks, *wlbl), run_time = 0.5)
        self.remove(*prev_mobjs)

        fticks1 = VGroup(*[obj.copy() for obj in fticks[1:deno]]) 
        self.play(FadeIn(fticks1, shift=DOWN), lag_ratio = 0.5, run_time = 2)
        # fsegs1 = VGroup(*[obj.copy() for obj in fsegs[0:3]])
        # self.play(AnimationGroup(*[
        #     GrowFromEdge(s, edge=LEFT)
        #     for s in fsegs1
        # ]), run_time = 3)
        # self.wait()
        # self.play(fsegs1.animate(lag_ratio=0.1, run_time=2).arrange(buff = 0.2, direction = DOWN, center = False).shift(UP * 1.5))
        # self.play(FadeOut(fsegs1, shift=LEFT))

        self.play(FadeIn(*fticks[deno+1:], lag_ratio = 0.5, shift=DOWN))
        self.wait()

        for i in [0, 1]:
            self.play(Flash(fticks[i]))
            self.play(FadeIn(flbl[i], shift=DOWN))
            self.play(Wiggle(flbl[i]))

        ref = fsegs[0].copy()
        refb = self.get_brace(fticks, num_of_segs=1)
        refb.next_to(VGroup(*flbl[0:2]), direction=UP, buff=0.01)
        reflbl = Tex(f"$\\frac{{1}}{{{deno}}}$", font_size = 28)
        reflbl.next_to(refb, direction=UP, buff=0.01)
        self.play(GrowFromEdge(ref, edge=LEFT), FadeIn(refb))
        self.play(VGroup(reflbl, refb, ref).animate(lag_ratio=0.1).arrange(buff = 0.1, direction = DOWN, center = False).shift(UP * 2))

        for f, n in zip([*flbl[2:6]], [2, 3, 4, 5]):
            fsegs1 = VGroup(*[obj.copy() for obj in fsegs[0:n]])
            s = self.get_single_segment(fticks,start_at=0, num_of_segs=n)
            self.play(Flash(fticks[n]))
            self.play(GrowFromEdge(s, edge=LEFT))
            self.add(*fsegs1)
            self.remove(s)
            self.play(FadeIn(f, shift=DOWN))
            self.play(Wiggle(f))
            self.wait()
            txt = Tex(f"{n} copies of $\\frac{{1}}{{{deno}}}$", font_size=28)
            txt.shift(UP*2)
            txt.align_to(fticks[0], direction=LEFT)
            self.play(
                fsegs1.animate(lag_ratio=0.1).arrange(buff = 0.2, direction = RIGHT, center = False).shift(UP * 1.5), 
                FadeIn(txt))
            self.play(fsegs1.animate(lag_ratio=0.1).arrange(buff=0, direction = RIGHT, center = False))
            self.play(FadeOut(fsegs1, txt, shift=LEFT))

        self.play(FadeIn(*flbl[6:], lag_ratio = 0.1, shift=DOWN))
        self.wait()

        self.play(FadeOut(*flbl, ref, reflbl, refb))

        ref = fsegs[0].copy()
        refb = self.get_brace(fticks, num_of_segs=1)
        refb.next_to(VGroup(*fticks[0:2]), direction=UP, buff=0.1)
        reflbl = Tex(f"$\\frac{{1}}{{{deno}}}$", font_size = 28)
        reflbl.next_to(refb, direction=UP, buff=0.1)
        self.play(GrowFromEdge(ref, edge=LEFT), FadeIn(refb), FadeIn(reflbl))

        for i in [2, 3, 4]:
            self.play(VGroup(ref, refb, reflbl).animate.shift(RIGHT * (MY_UNIT_SIZE/deno) * i))
            self.wait()

        self.play(FadeOut(VGroup(ref, refb, reflbl)))

        ref = self.get_single_segment(fticks,num_of_segs=numer)
        refb = self.get_brace(fticks, num_of_segs=numer)
        refb.next_to(VGroup(*fticks[0:numer+1]), direction=UP, buff=0.1)
        reflbl = Tex(f'$\\frac{{{numer}}}{{{deno}}}$', font_size = 28)
        reflbl.next_to(refb, direction=UP, buff=0.1)
        self.play(GrowFromEdge(ref, edge=LEFT), FadeIn(refb), FadeIn(reflbl))

        for i in [2, 3, 4]:
            self.play(VGroup(ref, refb, reflbl).animate.shift(RIGHT * (MY_UNIT_SIZE/deno) * i))
            self.wait()
            



    def play_1half_to_1fifth(self):
        denominators = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        font_sz =[*[22]*3, *[20]*3, *[16]*2, 14, *[12]*2, 10]
        num_lines = [None] * len(denominators)
        for deno, i, fs in zip(denominators, range(0, len(num_lines)), font_sz):
            num_lines[i] =  self.create_rational_number_line(
                        denominator = deno,
                        unit = MY_UNIT_SIZE,
                        left_end = 0,
                        right_end = 6, 
                        frac_font_sz=fs, 
                        frac_seg_stroke_width=6, 
                        frac_seg_color=MY_MERCURY,
                        sign_vertical_alignment_factor = 0.012,
                        frac_only = True)

        group = VGroup()
        for nl in num_lines[0:6]:
            group.add(VGroup(
                nl.get("dummy_num_line"),
                *nl.get("ticks_for_whole"),
                *nl.get("ticks_for_frac"),
                *nl.get("label_for_frac")))
        
        group.arrange(direction=DOWN, buff=0.5)
        self.play(AnimationGroup(*[
            GrowFromEdge(nl.get("dummy_num_line"), edge=LEFT)
            for nl in num_lines[0:6]
        ]), run_time = 3, lag_ratio = 0.1)

        self.play(AnimationGroup(*[
            FadeIn(*nl.get("ticks_for_whole"), shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[0:6]
        ]), AnimationGroup(*[
            FadeIn(*nl.get("ticks_for_frac"), shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[0:6]
        ]), run_time = 3)

        self.play(AnimationGroup(*[
            FadeIn(*nl.get("label_for_frac")[1:], shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[0:6]
        ]), run_time = 3)

        prev_mobjs = self.mobjects
        self.play(FadeOut(*prev_mobjs, shift=LEFT))

        group = VGroup()
        for nl in num_lines[6:]:
            group.add(VGroup(
                nl.get("dummy_num_line"),
                *nl.get("ticks_for_whole"),
                *nl.get("ticks_for_frac"),
                *nl.get("label_for_frac")))
        
        group.arrange(direction=DOWN, buff=0.5)
        self.play(AnimationGroup(*[
            GrowFromEdge(nl.get("dummy_num_line"), edge=LEFT)
            for nl in num_lines[6:]
        ]), run_time = 3, lag_ratio = 0.1)

        self.play(AnimationGroup(*[
            FadeIn(*nl.get("ticks_for_whole"), shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[6:]
        ]), AnimationGroup(*[
            FadeIn(*nl.get("ticks_for_frac"), shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[6:]
        ]), run_time = 3)

        self.play(AnimationGroup(*[
            FadeIn(*nl.get("label_for_frac")[1:], shift=DOWN, lag_ratio=0.1)
            for nl in num_lines[6:]
        ]), run_time = 3)
        
        prev_mobjs = self.mobjects
        self.play(FadeOut(*prev_mobjs, shift=LEFT))



        # for nl, d, s in zip(num_lines[0:7], denominators, [3.5, 2 , 0.5, -1, 2.5, ]):
        #     dummy = nl.get("dummy_num_line")
        #     wticks = nl.get("ticks_for_whole")
        #     fticks = nl.get("ticks_for_frac")
        #     flbls = nl.get("label_for_frac")
        #     gp = VGroup(dummy, *wticks, *fticks, *flbls).shift(UP * s)
        #     self.play(GrowFromEdge(dummy, edge=LEFT))
        #     self.play(FadeIn(*wticks, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
        #     self.play(FadeIn(*fticks, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
        #     self.play(FadeIn(*flbls, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
        
        # prev_mobjs = self.mobjects
        # self.play(FadeOut(*prev_mobjs))

        # for nl, d, s in zip(num_lines[7:], denominators, [3,1.5,0,-1.5, -3]):
        #     dummy = nl.get("dummy_num_line")
        #     wticks = nl.get("ticks_for_whole")
        #     fticks = nl.get("ticks_for_frac")
        #     flbls = nl.get("label_for_frac")
        #     gp = VGroup(dummy, *wticks, *fticks, *flbls).shift(UP * s)
        #     self.play(GrowFromEdge(dummy, edge=LEFT))
        #     self.play(FadeIn(*wticks, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
        #     self.play(FadeIn(*fticks, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
        #     self.play(FadeIn(*flbls, shift=DOWN, lag_ratio = 0.1))
        #     self.wait()
            

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
        """
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
                "sign": frac_sign,
                "right_arrow": ar1,
                "left_arrow": ar2
            }
        """
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
        ar1 = None
        ar2 = None
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
            "sign": frac_sign,
            "right_arrow": ar1,
            "left_arrow": ar2
        }

        return gp

    def get_segments(self, start_numerator, end_numerator, frac_segs):
        vg = VGroup()
        for i in range(start_numerator, end_numerator, 1):
            vg.add(frac_segs[i])
        return vg

    def get_single_segment(self, fticks, start_at=0, num_of_segs=1, the_color=MY_MERCURY, stroke_width=6, with_tips=False, tip_color=RED):
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

    def alternate_color(self, ticks, color1, color2):
        for x, i in zip(ticks, range(0, len(ticks), 1)):
            x.set_color(color1 if i % 2 else color2 )

        