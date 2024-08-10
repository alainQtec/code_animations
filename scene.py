from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.9)  # set the color and transparency
        circle.set_opacity(0.5)
        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount
        rect = Rectangle()
        rect.set_fill(YELLOW, opacity=0.5)

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))
        self.play(Transform(circle, rect))
        self.play(FadeOut(circle))