from manim import *
import math
config.background_color="#202020"
MY_GOLD = GOLD
MY_BLUE = "#003366"
MY_RED = "#993333"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24
class FracMultiplicationScene(Scene):
    def construct(self):
        gp = self.create_rect(m=7, n=5, k=16, l=7, one_unit_eqv=2)
        self.add(gp.get("rect"))
        b1 = self.get_brace(gp.get("rect"), 3, 7, 2, DOWN)
        b2 = self.get_brace(gp.get("rect"), 6, 5, 2, LEFT)
        self.get_unit_sq_divs(gp.get("v_lines"), gp.get("h_lines"), 4, MY_GOLD, 5, 7)
        #self.add(*gp.get("cell"))
        self.add(*gp.get("result")[2])
        self.add(b1, b2)
        self.add(*gp.get("h_lines"))
        self.add(*gp.get("v_lines"))

    """
    m/n * k/l
    m/n left side, k/l bottom
    """
    def create_rect(self, m=1, n=2, k=1, l=2, one_unit_eqv= 5, stroke_width=2, fill_color=MY_BLUE, stroke_color=MY_GOLD):
        height=math.ceil(m/n) * one_unit_eqv
        width=math.ceil(k/l) * one_unit_eqv
        grid_xstep=one_unit_eqv/l
        grid_ystep=one_unit_eqv/n
        r = Rectangle(height=height, width=width, fill_color=fill_color, fill_opacity=1)
        r.set_stroke(color=stroke_color, width=stroke_width)

        v = r.get_vertices()
        grid_xstep = abs(grid_xstep)
        count = int(width / grid_xstep)
        vlines = [
            *(
                Line(
                    v[1] + i * grid_xstep * RIGHT,
                    v[1] + i * grid_xstep * RIGHT + height * DOWN,
                    color=stroke_color,
                    stroke_width=stroke_width
                )
                for i in range(1, count)
            )
        ]

        grid_ystep = abs(grid_ystep)
        count = int(height / grid_ystep)
        hlines = [
            *(
                Line(
                    v[1] + i * grid_ystep * DOWN,
                    v[1] + i * grid_ystep * DOWN + width * RIGHT,
                    color=stroke_color,
                    stroke_width=stroke_width
                )
                for i in range(1, count)
            )
        ]

        cell = Rectangle(height=grid_ystep, width=grid_xstep, stroke_width=stroke_width, stroke_color=MY_GOLD, fill_color=MY_RED, fill_opacity=1)
        cell.align_to(r, direction=LEFT).align_to(r, DOWN)

        results = [
            *(
                [
                    *(
                        cell.copy().shift(RIGHT * grid_xstep * i, UP * grid_ystep * j)
                        for i in range(0,k)
                    )
                ]
                for j in range(0,m)
            )
        ]
        gp = {
            "rect": r,
            "v_lines": vlines,
            "h_lines": hlines,
            "result": results,
        }

        return gp

    def get_brace(self, rect, numer, deno, one_unit_eq, dir):
        v = rect.get_vertices()
        if((dir==DOWN).all()):
            return BraceBetweenPoints(v[2], v[2] + RIGHT * one_unit_eq/deno * numer, direction=DOWN, color=MY_GOLD)
        if((dir==LEFT).all()):
            return BraceBetweenPoints(v[2], v[2] + UP * one_unit_eq/deno * numer, direction=LEFT)

    def get_unit_sq_divs(self, vlines, hlines, stroke_width, color, n, l):
        for i in range(n-1, len(hlines), n):
            hlines[i].stroke_width=stroke_width
            hlines[i].set_color(color)
        for i in range(l-1, len(vlines), l):
            vlines[i].stroke_width=stroke_width
            vlines[i].set_color(color)