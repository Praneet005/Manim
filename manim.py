# trigonometric_graphs.py

from manim import *

class TrigonometricGraphs(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * PI, 2 * PI],
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
            y_length=6,
            x_length=10
        )

        # Create graphs
        sine_graph = axes.plot(lambda x: np.sin(x), color=GREEN)
        cosine_graph = axes.plot(lambda x: np.cos(x), color=RED)
        tangent_graph = axes.plot(lambda x: np.tan(x), color=YELLOW)

        # Add labels
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Display graphs and labels
        self.add(axes, axes_labels, sine_graph, cosine_graph, tangent_graph)
        self.wait(20)  # Extend the duration to 20 seconds
