from manim import *

config.frame_height = 9
config.frame_width = 16

config.pixel_width = 1920*2
config.pixel_height = 1080*2

class NumberLineAndPlane(Scene):

    def construct(self):
        # self.add(NumberPlane(color=RED))
        eg_num_line = NumberLine([-5,5])
        ax = Axes(x_range=[-8,8], y_range=[-4.5,4.5], y_length=4.5, x_length=8, x_axis_config={"color": RED})
        self.add(NumberPlane(x_range=[-8,8], y_range=[-4.5, 4.5], x_length=8, y_length=4.5), ax, )
        return super().construct()