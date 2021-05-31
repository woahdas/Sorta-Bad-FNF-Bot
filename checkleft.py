import os
import pyautogui
import time

i = 1
imagecounter = 0


left = 1020
right = 700
top = 80
bottom = 140

time.sleep(8)

while(True):
    t0 = time.time()

    i += 1
    imagecounter += 17

    s = pyautogui.screenshot(region=(left, top, right, bottom))  # takes a screenshot
    s.save(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png')

    t1 = time.time()
    total = t1 - t0
    print(total)


    color = (193, 76, 154)  # color for the left arrow
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pyautogui.keyDown("left")
                pyautogui.keyUp("left")
                os.remove(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png')
                continue
