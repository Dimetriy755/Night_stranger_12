import pyautogui
import sys
import os
import time

# disable protection pyautogui
pyautogui.FAILSAFE = False

# removing extra traceback
sys.tracebacklimit = 0

pyautogui.move(-1275, 0, duration=0.25) # left
time.sleep(1)

pyautogui.move(0, -1275, duration=0.25) # up
time.sleep(1)

pyautogui.move(300, 0, duration=0.25)  # right
time.sleep(2)

pyautogui.move(0, 254, duration=0.25)  # down
time.sleep(2)