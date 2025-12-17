#!venv/bin/python3

import pygame, time, select, math
from gpiozero import Button

buttonA = Button(5)
buttonB = Button(6)

buttonL = Button(27)
buttonR = Button(23)
buttonU = Button(17)
buttonD = Button(22)
buttonC = Button(4)


surfaceSize = (240, 240)
# fontFile = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

pygame.init()
# pygame.font.init()

# defaultFont = pygame.font.Font(fontFile, 30)
lcd = pygame.Surface(surfaceSize)

def refresh():
    f = open("/dev/fb1","wb")
    f.write(lcd.get_buffer())
    f.close()
    time.sleep(0.016)
    
# This loop allows us to write red dots on the screen where we touch it
r = 0
defaultColor = (25,25,25)
pressedColor = (255,255,255)

buttonSize = 24

cx = 24
cy = 24
buttons = [
    (buttonA, (200, 200)),
    (buttonB, (224, 224))

    (buttonL, (cx - buttonSize, cy))
    (buttonR, (cx + buttonSize, cy))
    (buttonU, (cx, cy - buttonSize))
    (buttonD, (cx, cy + buttonSize))
    (buttonC, (cx, cy))
]

while True:
    r = (r + 1) % 255
    lcd.fill((r,r,r))

    for button, position in buttons:
        pygame.draw.circle(lcd, (pressedColor if button.is_pressed else pressedColor), position, buttonSize, 0)
    # lcd.blit(defaultFont.render("Hello World!", False, (0, 0, 0)),(0, 0))
    refresh()

exit()
