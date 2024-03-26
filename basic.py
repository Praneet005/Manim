from manim import *


class TransformCurve(Scene):
    def construct(self):
        # Define the parametric curve
        curve1 = ParametricFunction(lambda t: np.array([2 * np.cos(3 * t), 2 * np.sin(5 * t), 0]), t_range=[-TAU, TAU])
        curve2 = ParametricFunction(lambda t: np.array([2 * np.cos(3 * t), 2 * np.sin(5 * t), t]), t_range=[-TAU, TAU])

        # Create curves
        curve1.set_color(RED)
        curve2.set_color(BLUE)

        # Display curves
        self.add(curve1)

        # Transform the curve
        self.play(Transform(curve1, curve2, run_time=3))
        self.wait()

