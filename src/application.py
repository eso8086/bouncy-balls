import pygame as pg
from ball import Ball
from pygame import Vector2 as vec2


class Application:
    def __init__(self):
        pg.init()

        self.running = True
        self.dt = 0

        self._screen_resolution = 500, 500
        self._screen = pg.display.set_mode(self._screen_resolution)
        self._clock = pg.time.Clock()
        self._screen_refresh_rate = pg.display.get_current_refresh_rate()
        self._entities = {Ball(center=vec2(self._screen.get_rect().center) - vec2(120, 0)), Ball(center=vec2(self._screen.get_rect().center) + vec2(120, 0))}

    def update(self):
        events = pg.event.get()
        keys = pg.key.get_pressed()

        for event in events:
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

        for entity in self._entities:
            entity.update(self.dt, events, keys)

    def render(self):
        self._screen.fill("yellow")

        for entity in self._entities:
            entity.draw(self._screen)

        pg.display.flip()
        self.dt = self._clock.tick(self._screen_refresh_rate) * .001

    def exit(self):
        pg.quit()
