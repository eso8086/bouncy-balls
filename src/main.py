import pygame as pg
from Ball import Ball
from shared import vec2

if __name__ == "__main__":
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

    circles = [Ball(center=vec2(screen.get_rect().center))]

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
        dt = clock.tick(pg.display.get_current_refresh_rate()) * .001
        
    pg.quit()

