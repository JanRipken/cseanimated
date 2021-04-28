from manimlib.imports import *


class Bally(Circle):
    CONFIG = {
        "radius": 0.1,
        "fill_color": BLUE,
        "fill_opacity": 1,
        "color": GREEN
    }

    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.velocity = np.array((2, 0, 0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius

class Box(Rectangle):
    CONFIG = {
        "height": 6,
        "width": FRAME_WIDTH - 2,
        "color": GREEN_C
    }

    def __init__(self, ** kwargs):
        Rectangle.__init__(self, ** kwargs)  
        self.top = 0.5 * self.height
        self.bottom = -0.5 * self.height
        self.right_edge = 0.5 * self.width
        self.left_edge = -0.5 * self.width

class bouncyball(Scene):
    CONFIG = {
        "bouncing_time": 10,
    }
    def construct(self):
        box = Box()
        bally = Bally()
        self.play(FadeIn(box))
        self.play(FadeIn(bally))

        def update_ball(bally,dt):
            bally.acceleration = np.array((0, -10, 0))
            bally.velocity = bally.velocity + bally.acceleration * dt
            bally.shift(bally.velocity * dt)  
            if bally.get_bottom() <= box.bottom*0.96 or \
                    bally.get_top() >= box.top*0.7:
                bally.velocity[1] = -bally.velocity[1]
            
            if bally.get_left_edge() <= box.left_edge or \
                    bally.get_right_edge() >= box.right_edge:
                bally.velocity[0] = -bally.velocity[0]

        bally.add_updater(update_ball)
        self.add(bally)
        self.wait(self.bouncing_time)
        bally.clear_updaters()
        self.wait(3)