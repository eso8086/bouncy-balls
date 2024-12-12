import pygame as pg
from random import randrange
from pygame import Vector2 as vec2

GRAVITY = vec2(0, -20)
class Ball:
        def __init__(self, color: pg.color.Color = "red", radius: int = 40, center: pg.Vector2 = 0):
            self.color = color
            self.radius = radius
            self.center = center

            self.velocity = vec2(0, 0)
            self.speed = self.velocity.length()
            self.acceleration = vec2(0, 0)
            self.can_move = False

        def update(self, dt: int):
            self._handle_controls()

            self.acceleration -= GRAVITY

            self.velocity += self.acceleration
            self.speed = self.velocity.length()

            if self.speed != 0:
                self.center += self.velocity.normalize() * self.speed * dt


            if self.speed < 5:
                self.velocity = vec2(0, 0)

            self.velocity *= 0.3 ** dt
            self.acceleration = vec2(0, 0)


            collided = True

            # collision:
            if self._check_collision_with_right():
                self.center.x = 500 - self.radius
                self.velocity.x = self.velocity.x * -1

            elif self._check_collistion_with_left():
                self.center.x = self.radius
                self.velocity.x = self.velocity.x * -1         

            elif self._check_collision_with_top():
                self.center.y = self.radius
                self.velocity.y = self.velocity.y * -1

            elif self._check_collision_with_bottom():
                self.center.y = 500 - self.radius
                self.velocity.y = self.velocity.y * -1

            else: collided = False

            self.can_move = not collided

        def draw(self, surface: pg.surface.Surface):
            pg.draw.circle(surface, "red", self.center, self.radius)


        def _handle_controls(self):
             if self.can_move:
                keys = pg.key.get_pressed()
                if keys[pg.K_w]:
                    self.acceleration.y = -80

                if keys[pg.K_a]:
                    self.acceleration.x = -80

                if keys[pg.K_d]:
                    self.acceleration.x = 80

                if keys[pg.K_s]:
                    self.acceleration.y = 80
                
                if keys[pg.K_SPACE]:
                    self.acceleration = vec2(randrange(-1, 1)* 300, randrange(-1, 1) * 300)

        def _check_collision_with_right(self):
            return self.center.x >= 500 - self.radius

        def _check_collistion_with_left(self):
            return self.center.x <= 0 + self.radius
        
        def _check_collision_with_top(self):
            return self.center.y <= 0 + self.radius
        
        def _check_collision_with_bottom(self):
            return self.center.y >= 500 - self.radius