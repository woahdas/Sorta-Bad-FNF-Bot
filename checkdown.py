import os
import pyautogui
import time


i = 1
imagecounter = 0


left = 1020
right = 700
top = 80
bottom = 140

time.sleep(5)

while(True):


    i += 1
    imagecounter += 7

    s = pyautogui.screenshot(region=(left, top, right, bottom))  # takes a screenshot
    s.save(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png')


    color = (3, 255, 255) # color for the left arrow
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:   #scans the entire screenshot for the color
                pyautogui.keyDown("left") #presses left key
                pyautogui.keyUp("left") #releases left key
                os.remove(r'C:\Users\eyesi\OneDrive\Pictures\Screenshots\test' + str(imagecounter) + '.png') #removes image
                continue #goes back to the top of the while loop
