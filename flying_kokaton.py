import os
import sys
import pygame as pg

import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    f_bg_img = pg.transform.flip(bg_img, True, False)
    tmr = 0

    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    koukaton_rct = koukaton.get_rect()
    koukaton_rct.center = 300, 200


    while True:
        x = -(tmr % 3200)

        move = [0, 0]

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()

        screen.blit(bg_img, [x, 0])
        screen.blit(f_bg_img, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])

        if key_lst[pg.K_UP]:
            move[1] -= 1

        if key_lst[pg.K_DOWN]:
            move[1] += 1

        if key_lst[pg.K_LEFT]:
            move[0] -= 1

        if key_lst[pg.K_RIGHT]:
            move[0] += 1
        else:
            move[0] -= 1

        koukaton_rct.move_ip(move)
        screen.blit(koukaton, koukaton_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()