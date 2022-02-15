from turtle import fillcolor
from manim import *
config.background_color="#212121"
#config.frame_height=9 * 1.01
#config.frame_width=16 * 1.01
MY_GOLD = GOLD
MY_BLUE = "#003366"
MY_RED = "#EE3300"
MY_GRAY = "#AAAAAA"
MY_MERCURY = "#EBEBEB"
MY_SILVER = "#D6D6D6"
MY_UNIT_SIZE = 2
MY_FRAC_FONT_SIZE = 24
MY_BACKGROUND_COLOR = "#212121"
class Counting(Scene):
    def construct(self): 
        #self.play_ones()
        #self.play_ones()      
        self.play_tens()
        #self.play_hundreds()
    
    def play_tens(self):
        tens = self.gen_tens().get("tens")
        ones = self.gen_tens().get("ones")
        """
        =========================================================================

        Counting is the beginning of mathematics. Let's try to understand a little bit 
        more deeply about how counting is done in the so-called Hindu-Arabic numeral
        system, which is the numeral system we used today all over the world.

        In Hindu-Arabic numeral system, we only use 10 symbols, 0 through 9. 
        The numbers are constructed by placing these 10 symbols at
        different position. Each number may just take one place (or one position)
        For instance, the number 7 take only place, the number 21 has two
        place, whereas 2501 has four place, etc etc. Notice that although we only use
        10 symbols, the number of place we are allowed to use for each number is unlimited.

        We'll see that although we are limited to using just 10 symbols, by not limiting 
        the number of place a number can take, we can count as many as we like

        Let's first study the simplest numbers among all. 0 through 9. They have only
        one place.

        Using `ten` symbols 0 to 9, we can count up to 9. 
        
        The first symbol 0, which is a `single` 0 I have to emphasize for reasons we
        will see shortly, is usually used when we have nothing to count. For example, 
        I have no sibling is the same as I have zero sibling. Human beings have no 
        tail is the same as saying human being have zero tail.
        
        Starting with 1, we can count up to nine items. I have one elder sister and 
        2 younger brothers. I have 9 cats. But you can't talk about the number of
        fingers you have using only these 10 symbols 0 to 9. Because you have more
        than 9 fingers.

        Why limited to just 9 symbols? you might wonder. Just invent more symbols,

        Ancient civilization in India (or China) realized that, without introducing
        new symbols, they still can count more. If they use one than one symbols for
        each number.

        Let's imagine the way they probably realized this better way of counting things.
        
        We will use the same ten symbols. Write them down in the next row.

        """

        for i in range(0, 10):
            self.play(FadeIn(tens[0][i]))
        """
        But to indicate that these are in the second row, we put the symbol 1 before 
        all the symbols 0 to 9 this time. Therefore, it will look like this. Each number 
        in this row has two symbols. The first one, or the first digit from the left, is 
        1 for all of them, and the second one running from 0 all the way to 9. And these 
        are called two digit numbers. And, by the way, the numbers in the first row are
        called one digit numbers simply because only one symbol is used for each number.

        Now let's consider the first two digit number, which is 10, in this row. What does
        it mean? Well, if we count. 10 comes next after 9. So we have just one more thing 
        than 9. And now you can count how many fingers you have. This is a special number. 
        We'll see the special role it plays very soon.

        What about 11? The second digit from the left is 1. It it just means that we've
        count just one more from 10.

        What do you think 17 means? Well, it's quite obvious that 7 more than 10. So,
        all the numbers in this row are related to 10, and the second digit tells us that
        how many more objects you 

        We say this is the second row and, the fact that it's starting with 1 is a little
        confusing. You can think of it as the first row of two digit numbers if you'd like.
        That may make you less confused.
        """
        self.play(FadeIn(tens[1][0]))
        #from 1 to 10, you can count exactly ten objects
        self.wait(4)

        #counting 9 more up to 19
        for i in range(1, 10):
            self.play(FadeIn(tens[1][i]))

        #By convention, if the first digit, from the left, is zero, we just write the numbers without it. i.e 00 as 0 and 01 as 1, 02 as 2, etc
        self.add(*ones)
        self.play(FadeOut(*tens[0]))

        #Let's pause and ponder. The second row. 
        #what is 1 in the tens place of the number 10, 11, 17?
        #1 in the tens place (the first digit) indicates we've counted and passed the first row i.e 1 to 9
        #and we are in the second row. 10 means the first number of the second row. And it is exactly 10. 11 means you are on the
        #second row and have counted one more, 17 means you have counted seven more.

        #So the first number 1 of from 10 to 19 means 10 and the second number indicates how many more you have counted from ten.
        #Similarly, 2 in the tens ...
        #So the first digit 2 in 20 to 29 means two times ten and 
        #1 to 10 is 10, 11 to 20 is another 10, so 1 to 20 is 2 times 10
        pv10 = VGroup()
        for i in range(0,10):
            d = MathTex("1", color=MY_RED)
            d.move_to(tens[1][i], aligned_edge=LEFT)
            pv10.add(d)

        self.play(FadeIn(pv10))
        self.wait(5)
        self.play(FadeOut(pv10))
        #======================================================================
        #At this point, we've used up all ten symbols in the second row. So, we
        #go down to the next row, and to remind us we've reached to the third row
        #we put 2 in the first place.
        """
        =======================================================================
        At this point we have used up all the two digit numbers starting with 1
        in the second row. So we can move down to the next row to be able to
        count more than 19.

        We repeat the same ten symbols 0 to 9 in this new row, but we put 2 before
        all of them to distinguish them from the previous row.

        20 is the first in this row. Don't you think it's related to 10 in a specific
        way? We know that 10 . 19 is 9 things more than 10. Or

        So, we reach 20 after counting ten more things from 10. If we count from 1
        to 10, it means we have 10 things. If we keep counting from 11

        So what is 23?
        """
        self.play(FadeIn(tens[2][0]))
        self.wait(5)
        #20 is the start of the third row. 1 to 10 is exactly 10, which obviously
        #we already know. 
        for i in range(1, 10):
            self.play(FadeIn(tens[2][i]))

        #Let's think about 21. It starts with 2, meaning that you are in the third row. 
        #From 1 to 20 is exactly 20, or ten times two. And you count one more, which is
        #indicated by 1, which is the second digit from the left.
        
        #How about 27? It still starts with 2, that is, it too is in the third row.
        #From 1 to 20 is exactly 20, or ten times two. 7 tells us that we count 7
        #more, up to here. Similarly, for 29, you count 9 more objects from 20. 

        pv20 = VGroup()
        for i in range(0,10):
            d = MathTex("2", color=MY_RED)
            d.move_to(tens[2][i], aligned_edge=LEFT)
            pv20.add(d)

        self.play(FadeIn(pv20))
        self.wait(5)
        self.play(FadeOut(pv20))



        self.play(FadeIn(*tens[3]))
        self.play(FadeIn(*tens[4]))
        self.play(FadeIn(*tens[5]))
        self.play(FadeIn(*tens[6]))
        self.play(FadeIn(*tens[7]))
        self.play(FadeIn(*tens[8]))
        self.play(FadeIn(*tens[9]))
        self.wait(20)

    def play_three_digits(self):
        #self.play_hundreds()
        data = self.gen_hundreds_full_display_data()
        #self.play(self.camera.frame.animate.move_to(RIGHT * data[0][86].get_x()), run_time=5)
        

        vg = VGroup()
        for i in range(0, 10):
            vg.add(*data[i])

        self.add(vg)

        lf = Rectangle(height=config.frame_height, width=2, stroke_color = MY_BACKGROUND_COLOR, fill_color=MY_BACKGROUND_COLOR, fill_opacity=1)
        rh = Rectangle(height=config.frame_height, width=2, stroke_color = MY_BACKGROUND_COLOR, fill_color=MY_BACKGROUND_COLOR, fill_opacity=1)
        lf.next_to(data[5][0], direction=LEFT, buff=0.1)
        rh.next_to(data[5][27], direction=RIGHT, buff=0.1)
        self.add(lf, rh)
        shift_amt = (data[5][1].get_center() - data[5][0].get_center())
        self.play(vg.animate.shift(LEFT * shift_amt * 50), run_time=10)

        self.wait(10)

        self.clear()
        self.add(vg.scale())

        #self.wait(1)
        #self.play(Restore(self.camera.frame))
        #self.wait(5)

    def play_hundreds(self):
        gp = self.gen_hundreds_display_data()
        data = gp.get("hundreds")
        frow = gp.get("first_row")
        self.add(*data[0])
        self.add(*data[1])
        self.add(*data[3])
        self.add(*frow)
        self.play(FadeOut(*data[0]))
                                                                                                                                                                                     
    def play_one_digit(self):
        digits = [None]*(10)
        for i in range(0, 10):
            digits[i] = MathTex(f"{i}")
        self.play(FadeIn(digits[1]))
        return

    def gen_rows_of_one_digit(self):
        tens = [None]*(10)
        ax = Axes(x_range=[0,10,1], y_range=[-10,0,1])
        ax.add_coordinates()
        for i in range(0, 10):
            tens[i] = [None]*(10)
            for j in range(0, 10):
                tens[i][j] = MathTex(f"{j}").move_to(ax.c2p(j, i * -1))
        return tens

    def gen_tens(self):
        tens = [None] * 10
        ax = Axes(x_range = [0,10,1], y_range = [-10,0,1])
        ax.add_coordinates()
        for i in range(0, 10):
            tens[i] = [None] * 10
            for j in range(0, 10):
                tens[i][j] = MathTex(f"{i}{j}").move_to(ax.c2p(j, -i))
        ones = [None] * 10
        for i in range(0, 10):
            n = MathTex(f"{i}")
            n.move_to(tens[0][i], aligned_edge=RIGHT)
            ones[i] = n
        dict = {
            "tens":tens,
            "ones":ones
        }
        return dict

    """
    000 001 002 003 ... 009   010 011 012 013 ... 019   020 021 022 023 ... 029   030 ... ... ... 090 091 092 093 ... 099
    100 101 102 103 ... 109   110 `11`1 112 113 ... 119   120 121 122 123 ... 129   130 ... ... ... 190 191 192 193 ... 199
    ...
    ...
    ...
    900 901 902 903 ... 909   910 911 912 913 ... 919   920 921 922 923 ... 929   930 ... ... ... 990 991 992 993 ... 999
    """
    def gen_hundreds_display_data(self):
        row_data = [0, 1, 2, 3, "...",  9, 10, 11, 12, 13, "...", 19, 20, 21, 22,  23, "...", 29, 30, "...", "...", "...", 90, 91, 92, 93, "...", 99]
        row_data_str = [None]*(len(row_data))
        for i in range(0, len(row_data)):
            row_data_str[i] = str(row_data[i])
        ax = Axes(x_range=[0,len(row_data),1], y_range=[-10,0,1])
        ax.add_coordinates()
        hundreds = [None]*(10)
        first_row = [None] * len(row_data)
        for i in range(0, 10):
            hundreds[i] = [None] * (len(row_data_str))
            for j in range(0, len(row_data_str)):
                if(i == 0):
                    pre = ""
                    pre = "00" if len(row_data_str[j]) == 1 else "0"                       
                    num = row_data_str[j]
                    hundreds[i][j] = MathTex(f"{pre}{num}", font_size = 20).move_to(ax.c2p(j, i * -1))
                    first_row[j] = MathTex(f"{num}", font_size = 20).move_to(hundreds[i][j], aligned_edge=RIGHT)
                else:
                    num = (int(row_data_str[j]) + (i * 100)) if row_data_str[j] != "..." else row_data_str[j]
                    hundreds[i][j] = MathTex(f"{num}", font_size = 20).move_to(ax.c2p(j, i * -1))      
        gp = {
            "hundreds": hundreds,
            "first_row": first_row,
        }
        return gp

    def gen_hundreds_full_display_data(self):
        ax = Axes(x_range=[0,28,1], y_range=[-10,0,1])
        ax.add_coordinates()
        hundreds = [None] * 10
        first_row = [None] * 100
        for i in range(0, 10):
            hundreds[i] = [None] * 100
            for j in range(0, 100):
                num = i * 100 + j
                hundreds[i][j] = MathTex(f"{num}", font_size = 20).move_to(ax.c2p(j, i * -1))

        for j in range(0, 100):
            pre = ""
            pre = "00" if j < 10 else "0"                       
            first_row[j] = MathTex(f"{pre}{j}", font_size = 20).move_to(ax.c2p(j, 0))
            hundreds[0][j].move_to(first_row[j], aligned_edge=RIGHT)

        return hundreds
