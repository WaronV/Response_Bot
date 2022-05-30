import pyautogui as gui
from time import sleep
import pyperclip
import random

gui.FAILSAFE = True
def jaz(picture, text):
    sleep(5)
    pos_xy=gui.locateOnScreen(picture,confidence=0.7)
    if pos_xy is None: return jaz(picture, text)
    gui.click(pos_xy[0],pos_xy[1])
    sleep(1)
    gui.typewrite(text+"\n", interval=0.2)
    return pos_xy
count=0
while True:
    jaz("pictures/blue_dot.JPG","lubisz jaz?")
    