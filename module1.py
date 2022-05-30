import pyautogui as gui
from time import sleep


while True:
    posXY=gui.position()
    sleep(1)
    print(posXY, gui.pixel(posXY[0],posXY[1]))
    if posXY[0]==0: break
