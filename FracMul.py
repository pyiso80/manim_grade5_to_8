from manim import *
from numpy import array
config.background_color="#191918"

LINE_WIDTH=2
class WholeNumAsArea(Scene):
    def construct(self):
        plane = NumberPlane()
        #self.add(plane)

        s1 = Square(side_length=1)
        s1.set_stroke(color=GOLD,width=LINE_WIDTH)
        s1.shift(UP*0.5)
        self.play(FadeIn(s1))
        s1.set_fill(color=DARK_BLUE)
        self.play(s1.animate.set_opacity(1))
        b1 = Brace(s1)
        b1txt = b1.get_tex("1\ unit")
        self.play(FadeIn(b1, b1txt))

        rect1 = Rectangle(height=2, width=3)
        rect1.set_stroke(color=GOLD,width=LINE_WIDTH)
        #horizontal divider line
        dv1 = Line(ORIGIN, RIGHT*3,color=GOLD,stroke_width=LINE_WIDTH)
        dv1.move_to(rect1.get_center())
        #vertical divider lines
        dv2 = Line(ORIGIN, UP*2,color=GOLD,stroke_width=LINE_WIDTH)
        dv3 = dv2.copy()
        dv2.move_to(LEFT/2.0)
        dv3.move_to(RIGHT/2.0)
        br1 = Brace(rect1)
        br2 = Brace(rect1, RIGHT)
        br1txt = br1.get_tex("3\ unit")
        br2txt = br2.get_tex("2\ unit")
        rect1Vg =VGroup(rect1, dv1, dv2, dv3, br1, br1txt, br2, br2txt)


        rect1Vg.shift(UP).shift(RIGHT*2.5)
        self.play(FadeIn(rect1))
        rect1.set_fill(color=DARK_BLUE)
        self.play(rect1.animate.set_opacity(1))
        self.play(FadeIn(dv1, dv2, dv3))
        self.play(FadeIn(br1, br1txt))
        self.play(FadeIn(br2, br2txt))


class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))

class FracMulAsArea(Scene):
    def construct(self):
        fracMul = MathTex("\\frac{m}{n}\\times\\frac{k}{l} = the\ area\ of\ a\ rectangle\ with\ sides\ \\frac{m}{n}\ and\ \\frac{k}{l}")
        fracMul.move_to(UP*3)
        self.add(fracMul)

        #Let's make a unit 4 times as big
        unitsq = Square(side_length=3,color="#005F7F", fill_opacity=1)
        unitsq.set_stroke(color=GOLD,width=2)
        hdivs = self.getHorizontalDividers(unitsq, 5, GOLD, 2)
        vdivs = FracMulAsArea.getVerticalDividers(unitsq, 7, GOLD, 2)
        x1 = self.getBottomSeg(unitsq, 7, 3)
        x2 = self.getLeftSeg(unitsq, 5, 3)
        b1btm = Brace(x1, buff=0.075)
        b1btmtxt = b1btm.get_tex("\\frac{3}{7}")
        b1left = Brace(x2, LEFT)
        b1lefttxt = b1left.get_tex("\\frac{3}{5}")
        b1lefttxt.font_size=24
        b1btmtxt.font_size=24

        print(">>>>>>")
        print(b1btm.get_bottom())
        print(b1btmtxt.get_top())

        b1btmtxt.next_to(b1btm, direction=DOWN)
        b1btmtxt.set_y(b1btmtxt.get_y()+0.2)

        b2btm = Brace(unitsq, DOWN)
        b2btm.stroke_width=2
        b2btm.next_to(b1btmtxt, direction=DOWN)
        b2btm.set_x(0)
        b2btm.set_y(b2btm.get_y()+0.2)


        
        #b2btm.move_to(DOWN*abs(b1btmtxt.get_boundary_point(DOWN)[1]))

        vgb1 = VGroup(b1btm, b2btm, b1btmtxt)
        vgb2 = VGroup(b1left, b1lefttxt)

        vg = VGroup(unitsq, *hdivs, *vdivs, vgb1, vgb2)
        #vg.move_to(RIGHT*2).move_to(DOWN*0.5)
        self.play(FadeIn(unitsq))
        self.play(FadeIn(*vdivs))
        self.play(FadeIn(*hdivs))
        pl = NumberPlane()
        self.add(b1btm, b1left, b2btm,b1btmtxt, b1lefttxt, pl)
        
    def getHorizontalDividers(self, rect, n, thecolor, the_stroke_width):
        delta = rect.height/(1.0*n)
        divs = [None]*(n-1)
        for i in range(1,n,1):
            l = Line(ORIGIN, RIGHT*rect.width, color=thecolor, stroke_width=the_stroke_width)
            l.move_to(rect.get_edge_center(DOWN)+[0,i*delta,0])
            divs[i-1]=l    
        return divs

    def getVerticalDividers(rect, n, thecolor, the_stroke_width):
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

class FracMulAsArea1(Scene):
    def construct(self):
        fracMul = MathTex("\\frac{m}{n}\\times\\frac{k}{l} = the\ area\ of\ a\ rectangle\ with\ sides\ \\frac{m}{n}\ and\ \\frac{k}{l}")
        fracMul.move_to(UP*3)
        self.add(fracMul)

        #Let's make a unit 3 times as big
        unitsq = Square(side_length=3,color="#005F7F", fill_opacity=1)
        unitsq.set_stroke(color=GOLD,width=2)
        hdivs = self.getHorizontalDividers(unitsq, 5, GOLD, 2)
        vdivs = FracMulAsArea.getVerticalDividers(unitsq, 7, GOLD, 2)
        x1 = self.getBottomSeg(unitsq, 7, 3)
        x2 = self.getLeftSeg(unitsq, 5, 3)
        b1btm = Brace(x1)
        b1btmtxt = b1btm.get_tex("\\frac{3}{7}")
        b1left = Brace(x2, LEFT)
        b1lefttxt = b1left.get_tex("\\frac{3}{5}")
        b1lefttxt.font_size=24
        b1btmtxt.font_size=24
        #b1lefttxt.rotate(90*DEGREES)

        b1btmtxt.next_to(b1btm, direction=DOWN)
        b1btmtxt.set_y(b1btmtxt.get_y())

        b2btm = Brace(unitsq, DOWN)
        b2btm.next_to(b1btmtxt, direction=DOWN)
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

    def getVerticalDividers(rect, n, thecolor, the_stroke_width):
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







