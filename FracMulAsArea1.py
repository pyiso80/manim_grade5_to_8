from manim import *
from numpy import array
config.background_color="#202020"
class FracMulAsArea(Scene):
    def construct(self):
        fracMul = MathTex("\\frac{m}{n}\\times\\frac{k}{l} = the\ area\ of\ a\ rectangle\ with\ sides\ \\frac{m}{n}\ and\ \\frac{k}{l}")
        fracMul.move_to(UP*3)
        self.add(fracMul)

        #Let's make a unit 3 times as big
        unitsq = Square(side_length=3,color="#005F7F", fill_opacity=1)
        unitsq.set_stroke(color=GOLD,width=2)
        hdivs = self.getHorizontalDividers(unitsq, 5, GOLD, 2)
        vdivs = self.getVerticalDividers(unitsq, 7, GOLD, 2)
        x1 = self.getBottomSeg(unitsq, 7, 3)
        x2 = self.getLeftSeg(unitsq, 5, 3)
        b1btm = Brace(x1)
        b1btmtxt = b1btm.get_tex("\\frac{3}{7}")
        b1left = Brace(x2, LEFT)
        b1lefttxt = b1left.get_tex("\\frac{3}{5}", buff=0.05)
        b1lefttxt.font_size=24
        b1btmtxt.font_size=24
        #b1lefttxt.rotate(90*DEGREES)

        b1btmtxt.next_to(b1btm, direction=DOWN, buff=0.05)
        b1btmtxt.set_y(b1btmtxt.get_y())

        b2btm = Brace(unitsq, DOWN)
        b2btm.next_to(b1btmtxt, direction=DOWN, buff=0.05)
        b2btm.set_x(0)
        b2btm.set_y(b2btm.get_y())

        vgb1 = VGroup(b1btm, b2btm, b1btmtxt)
        vgb2 = VGroup(b1left, b1lefttxt)

        vg = VGroup(unitsq, *hdivs, *vdivs, vgb1, vgb2)
        #vg.move_to(RIGHT*2).move_to(DOWN*0.5)
        self.play(FadeIn(unitsq))
        self.play(FadeIn(*vdivs))
        self.play(FadeIn(*hdivs))
        self.add(b1btm, b1left, b2btm,b1btmtxt, b1lefttxt)
        
    def getHorizontalDividers(self, rect, n, thecolor, the_stroke_width):
        delta = rect.height/(1.0*n)
        divs = [None]*(n-1)
        for i in range(1,n,1):
            l = Line(ORIGIN, RIGHT*rect.width, color=thecolor, stroke_width=the_stroke_width)
            l.move_to(rect.get_edge_center(DOWN)+[0,i*delta,0])
            divs[i-1]=l    
        return divs

    def getVerticalDividers(self, rect, n, thecolor, the_stroke_width):
        delta = rect.width/(1.0*n)
        divs = [None]*(n-1)
        for i in range(1,n,1):
            l = Line(ORIGIN, UP*rect.height, color=thecolor, stroke_width=the_stroke_width)
            l.move_to(rect.get_edge_center(LEFT)+[i*delta,0,0])
            divs[i-1]=l        
        return divs

    def getBottomSeg(self, rect, n, p):
        d = rect.width/(1.0*n)
        l = d * p
        s = Line(ORIGIN, RIGHT*l)
        s.shift(DOWN*(rect.height/2.0)).shift(LEFT*(rect.width/2.0))
        return s

    def getLeftSeg(self, rect, n, p):
        d = rect.height/(1.0*n)
        l = d * p
        s = Line(ORIGIN, UP*l)
        s.shift(DOWN*(rect.height/2.0)).shift(LEFT*(rect.width/2.0))
        return s

    def getCells(self, rect, l, n, thecolor, buff):
        w = rect.width/l
        h = rect.height/n
        r = Rectangle()
        rows = [None]*l
        for i in range(0, l, 1):
            rows[i] = Rectangle()

#333
class RectTest(Scene):
    def construct(self):
        r = Rectangle(
            height=5, width=5, fill_color="#003366",#fill_color="#005F75", #fill_color="#0055A4#06c", 
            fill_opacity=1, grid_xstep=5/7, grid_ystep=5/5, 
        )
        r.set_stroke(color=GOLD, width=2)
        r2 = Rectangle(
            height=5/5*3, width=5/7*3, fill_color="#993333",
            fill_opacity=1, grid_xstep=5/7, grid_ystep=5/5,
        )
        r2.set_stroke(color=GOLD, width=2.5)
        r2.shift(LEFT*(5/7)*2)
        print(r2.get_center())
        r2.shift(DOWN*(5/5*1))
        print(r2.get_center())
        self.play(FadeIn(r), run_time=2.0)
        self.play(GrowFromPoint(r2,point=r2.get_left()), run_time=1.5)
            