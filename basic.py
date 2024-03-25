from manim import *

class MatrixVisualization(Scene):
    def construct(self):
        matrix = Matrix([
            ["a", "b"],
            ["c", "d"]
        ])

        self.play(Create(matrix))
        self.wait()

        self.play(Transform(matrix, matrix.copy().scale(2)))
        self.wait()

        self.play(Transform(matrix, matrix.copy().rotate(PI/4)))
        self.wait()

        self.play(Uncreate(matrix))
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(sys.argv[0])
    command = f"manim -pql {module_name} MatrixVisualization"
    os.system(command)


