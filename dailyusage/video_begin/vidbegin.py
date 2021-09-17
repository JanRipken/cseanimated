from manim import *

class vidbegin(Scene):
    def construct(self):
        image_vidbegin = ImageMobject("main/e-i-vidstart.png")
        self.play(FadeInFromDown(image_vidbegin))
        self.wait(5)
        self.play(FadeOutAndShift(image_vidbegin))
        self.wait(1)