from manim import *

class MatrixVisualization(Scene):
    def construct(self):
        # Define the numerical values
        a, b, c, d = 1, 2, 2, 3

        # Define the matrix
        matrix = Matrix([
            [a, b],
            [c, d]
        ])
        matrix.scale(0.7)

        # Add text labels
        entries = matrix.get_entries()
        labels = VGroup(
            Tex(f"{a}").next_to(entries[0], UP),
            Tex(f"{b}").next_to(entries[1], UP),
            Tex(f"{c}").next_to(entries[2], UP),
            Tex(f"{d}").next_to(entries[3], UP)
        )

        # Create arrows to represent vectors
        arrow1 = Arrow(ORIGIN, RIGHT, color=BLUE).next_to(labels[0], DOWN)
        arrow2 = Arrow(ORIGIN, RIGHT, color=BLUE).next_to(labels[1], DOWN)
        arrow3 = Arrow(ORIGIN, RIGHT, color=BLUE).next_to(labels[2], DOWN)
        arrow4 = Arrow(ORIGIN, RIGHT, color=BLUE).next_to(labels[3], DOWN)

        # Group all objects together
        group = VGroup(matrix, labels, arrow1, arrow2, arrow3, arrow4)
        
        # Show matrix and arrows
        self.play(Create(group))
        self.wait()

        # You can add animations here to represent transformations if needed
        # For example:
        # self.play(matrix.animate.shift(LEFT))

        # Fade out the objects
        self.play(FadeOut(group))
        self.wait()

if __name__ == "__main__":
    module_name = "basic.py"
    command = f"manim -pql {module_name} MatrixVisualization"
    os.system(command)
