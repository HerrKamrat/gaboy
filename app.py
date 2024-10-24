#!venv/bin/python3

import pygame, time, select, math

surfaceSize = (240, 240)
fontFile = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

pygame.init()
pygame.font.init()

defaultFont = pygame.font.Font(fontFile, 30)
lcd = pygame.Surface(surfaceSize)

def refresh():
    f = open("/dev/fb1","wb")
    f.write(lcd.get_buffer())
    f.close()
    time.sleep(0.016)

lcd.fill((255,0,0))
lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
refresh()

lcd.fill((0, 255, 0))
lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
refresh()

lcd.fill((0,0,255))
lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
refresh()

lcd.fill((0,0,255))
lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
refresh()

lcd.fill((128, 128, 128))
lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
refresh()

# This loop allows us to write red dots on the screen where we touch it
r = 0
while True:
    r = (r + 1) % 255
    lcd.fill((r,r,r))
    pygame.draw.circle(lcd, (r % 255, 0, 0), (120, 120) , 120, 60)
    refresh()

exit()