from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip
config.background_color="#202020"
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24
class FracNumberLine(Scene):
    def construct(self):
        self.create_frac_num_line(denominator=7)
    def create_frac_num_line(self, denominator=3, unit=MY_UNIT_SIZE, last_whole_num=6, frac_font_sz=MY_FRAC_FONT_SIZE, color=GOLD):
        f1 = NumberLine(
            [0, last_whole_num, 1],
            unit_size=unit,
            include_ticks=False, 
            include_tip=True,
            color=color
        )
        self.add(f1)
        self.play(FadeIn(f1.get_tick(0, size=0.2)))
        self.play(FadeIn(f1.get_number_mobject(0)))

        self.play(FadeIn(f1.get_tick(1, size=0.2)))
        self.play(FadeIn(f1.get_number_mobject(1)))

        for i in range(2, last_whole_num, 1):
            self.play(FadeIn(f1.get_tick(i, size=0.2), f1.get_number_mobject(i)))

        #1 unit divided into 3 equal parts
        self.play(FadeIn(f1.get_tick(1/denominator)))
        self.play(FadeIn(f1.get_tick(2/denominator)))

        #each and every unit divided into 3 equals parts
        f1a = NumberLine(
            [0, last_whole_num, 1/denominator],
            unit_size=MY_UNIT_SIZE,
            numbers_with_elongated_ticks=range(0,last_whole_num + 5,1),
            include_ticks=True, 
            include_tip=False,
            color=GOLD
        )
        line = Line(start=ORIGIN, end=RIGHT*0.25, buff=0, color=GOLD,stroke_width=2)
        
        f1tip = NumberLine(
            x_range=[0, 0.75, 1],
            include_ticks=False,
            include_tip=True,
            color=GOLD,
        )

        f1tip.next_to(f1a.get_right(), RIGHT, buff=0)
        
        self.play(FadeIn(f1a, f1tip))
        self.remove(f1)

        #display one third as segment length at different positions
        #every segment repres#999ents 1/3
        onethird = Line(
            f1a.get_left(),
            f1a.get_left() + [MY_UNIT_SIZE/denominator,0,0],
            color=GOLD_C, 
            stroke_width=6,
            buff=0.01
        )
        self.add(onethird)

        #self.play(FadeIn(onethird.copy().shift(RIGHT*MY_UNIT_SIZE/3*5), run_time=1.5))
        #self.play(FadeIn(onethird.copy().shift(RIGHT*MY_UNIT_SIZE/3*7), run_time=1.5))

        #multiples of 1/3
        l = MathTex(f"\\frac{{{1}}}{{{denominator}}}")
        l.next_to(f1a.number_to_point(1/denominator), direction=UP, buff=0)
        l.font_size = 16
        self.play(FadeIn(l))
        for i in range(0, last_whole_num * denominator, 1):
            s = onethird.copy().shift(RIGHT*MY_UNIT_SIZE/denominator*i)
            self.play(GrowFromPoint(s, s.get_left()), run_time=1)
            l = MathTex(f"\\frac{{{i + 1}}}{{{denominator}}}")
            l.next_to(f1a.number_to_point(1/denominator*(i+1)), direction=UP, buff=0)
            l.font_size = 16
            self.play(FadeIn(l)) 

        f2 = NumberLine(
            [0, 6, 1],
            unit_size=2,
            include_ticks=True,
            numbers_with_elongated_ticks=[0,1,2],
            include_tip=True,

        )

        f2.shift(DOWN*2)
        self.add(f2)

        for i in range(1, 5):
            self.play(FadeIn(f2.get_tick((i/5))))
