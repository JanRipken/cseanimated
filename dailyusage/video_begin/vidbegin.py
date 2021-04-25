from manimlib.imports import *

class vidbegin(Scene):
    def construct(self):

        image_vidbegin = ImageMobject("main/e-i-vidstart.png")

        self.play(FadeIn(image_vidbegin))
        self.wait(5)
        self.play(FadeOut(image_vidbegin))
        self.wait()