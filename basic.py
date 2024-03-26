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

        # Move camera to show x-z plane
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES)
        self.wait()

        # Add axes for x-z plane
        axes_xz = ThreeDAxes(x_range=(-3, 3), y_range=(-3, 3), z_range=(-3, 3))
        self.add(axes_xz)

        # Move camera to show y-z plane
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait()

        # Add axes for y-z plane
        axes_yz = ThreeDAxes(x_range=(-3, 3), y_range=(-3, 3), z_range=(-3, 3))
        axes_yz.rotate(PI / 2, RIGHT)
        self.add(axes_yz)

        self.wait()



