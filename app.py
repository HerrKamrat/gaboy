#!venv/bin/python3

import pygame, time, select, math

# Very important: the exact pixel size of the TFT screen must be known so we can build graphics at this exact format
surfaceSize = (240, 240)

# Note that we don't instantiate any display!
pygame.init()

# The pygame surface we are going to draw onto.
# /!\ It must be the exact same size of the target display /!\
lcd = pygame.Surface(surfaceSize)

# This is the important bit
def refresh():
    # We open the TFT screen's framebuffer as a binary file. Note that we will write bytes into it, hence the "wb" operator
    f = open("/dev/fb1","wb")
    # According to the TFT screen specs, it supports only 16bits pixels depth
    # Pygame surfaces use 24bits pixels depth by default, but the surface itself provides a very handy method to convert it.
    # once converted, we write the full byte buffer of the pygame surface into the TFT screen framebuffer like we would in >
    f.write(lcd.get_buffer())
    # We can then close our access to the framebuffer
    f.close()
    time.sleep(0.016)

# Now we've got a function that can get the bytes from a pygame surface to the TFT framebuffer,
# we can use the usual pygame primitives to draw on our surface before calling the refresh function.

# Here we just blink the screen background in a few colors with the "Hello World!" text
pygame.font.init()
defaultFont = pygame.font.SysFont(None,30)

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