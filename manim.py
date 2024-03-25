from manim import Scene, Text, Sphere, Torus, BLUE, PI, Rotate, FadeIn, FadeTransform, ShowCreation, TexturedSurface

class SurfaceExample(Scene):

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(inner_radius=1, outer_radius=1)
        torus2 = Torus(inner_radius=3, outer_radius=1)
        sphere = Sphere(radius=3)
        
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.set_stroke(BLUE, 1, opacity=0.5)

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface, lag_ratio=0.01, run_time=3),
        )
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            run_time=3
        )

        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)

        drag_text = Text("Try moving the mouse while pressing d or s")
        drag_text.move_to(light_text)
        self.play(FadeTransform(light_text, drag_text))
        self.wait()
