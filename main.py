import pygame as pg
from random import randrange

vec2 = pg.Vector2

if __name__ == "__main__":
    t = 0
    class Circle:
        def __init__(self, color: pg.color.Color = "red", radius: int = 40, center: pg.Vector2 = 0):
            self.color = color
            self.radius = radius
            self.center = center

            self.velocity = vec2(0, 0)
            self.acceleration = vec2(0, 0)
            self.can_move = False

        def update(self, dt: int):
            self._handle_controls()

        
            self.velocity += self.acceleration

            if abs(self.velocity.x) > 400:
                self.velocity.x = self.velocity.x // abs(self.velocity.x) * 400

            if abs(self.velocity.y) > 400:
                self.velocity.y = self.velocity.y // abs(self.velocity.y) * 400

            self.center += self.velocity * dt

            self.velocity *= 0.3 ** dt

            if self.velocity.length() < 0.1:
                self.velocity = vec2(0, 0)

            self.acceleration = vec2(0, 0)


            collided = False

            # collision:
            if self._check_collision_with_right():
                collided = True
                self.center.x = 500 - self.radius
                self.velocity.x = self.velocity.x * -1

            if self._check_collistion_with_left():
                collided = True
                self.center.x = self.radius
                self.velocity.x = self.velocity.x * -1         

            if self._check_collision_with_top():
                collided = True
                self.center.y = self.radius
                self.velocity.y = self.velocity.y * -1

            if self._check_collision_with_bottom():
                collided = True
                self.center.y = 500 - self.radius
                self.velocity.y = self.velocity.y * -1

            self.can_move = collided

        def draw(self, surface: pg.surface.Surface):
            pg.draw.circle(surface, "red", self.center, self.radius)


        def _handle_controls(self):
             if not self.can_move:
                keys = pg.key.get_pressed()
    
                if keys[pg.K_w]:
                    self.acceleration = vec2(0, 200)

                if keys[pg.K_a]:
                    self.acceleration = vec2(200, 0)

                if keys[pg.K_d]:
                    self.acceleration = vec2(200, 0)

                if keys[pg.K_s]:
                    self.acceleration = vec2(0, 200)
                
                if keys[pg.K_SPACE]:
                    self.acceleration = vec2(randrange(-400, 400), randrange(-400, 400))

        def _check_collision_with_right(self):
            return self.center.x >= 500 - self.radius

        def _check_collistion_with_left(self):
            return self.center.x <= 0 + self.radius
        
        def _check_collision_with_top(self):
            return self.center.y <= 0 + self.radius
        
        def _check_collision_with_bottom(self):
            return self.center.y >= 500 - self.radius

    running = False
    dt = 0

    def init():
        global screen, clock, running
        pg.init()
        screen  = pg.display.set_mode((500, 500))
        clock = pg.time.Clock()
        running = True


    def handle_keyboard_inputs():
        global running
        keys = pg.key.get_pressed()

        if keys[pg.K_ESCAPE]:
            running = False


    init()

    circles = [Circle(center=vec2(screen.get_rect().center))]

    while running:
        for event in pg.event.get(eventtype=pg.QUIT):
            if event.type == pg.QUIT:
                running = False


        handle_keyboard_inputs()

        screen.fill("yellow")


        for circle in circles:
            circle.update(dt)
            circle.draw(screen)

        pg.display.flip()
        dt = clock.tick(20) * .001
        
    pg.quit()

