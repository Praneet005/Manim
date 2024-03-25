from manim import *


class CalculusApplications(Scene):
    def construct(self):
        text1 = Text("Real-world Application 1: Physics").shift(UP*2)
        text2 = Text("Real-world Application 2: Economics").shift(UP)
        text3 = Text("Real-world Application 3: Engineering").shift(DOWN)

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(2) 
