from manim import *

class Test(Scene):
    def construct(self):
        Square.set_default(stroke_width=10)
        Circle.set_default(stroke_width=5)
        
        s1 = Square()
        s2 = Square().set_fill(color=RED, opacity=1)
        self.play(Transform(s1, s2))
        self.play(FadeOut(s1))
        print(Line().get_unit_vector())