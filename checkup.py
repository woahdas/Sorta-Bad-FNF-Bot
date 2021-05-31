import os
import pyautogui
import time
from pynput.keyboard import Key, Controller
kb = Controller()



i = 1
imagecounter = 0


left = 1020
right = 700
top = 80
bottom = 140

time.sleep(6)

while(True):
    t0 = time.time()

    i += 1
    imagecounter += 11

    s = pyautogui.screenshot(region=(left, top, right, bottom))  # takes a screenshot
    s.save(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png')

    t1 = time.time()
    total = t1 - t0
    print(total)


    color = (18, 250, 5)   # color for the top arrow
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                kb.press(Key.up)
                kb.release(Key.up)
                os.remove(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png')
                continue
