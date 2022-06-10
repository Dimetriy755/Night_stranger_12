import pyautogui
import time

time.sleep(12)

# ATTENTION there is a special loop
# for python that repeats the code
# endlessly after a given time:

starttime = time.time()
while 1==1:

    # Move mouse in a square
    for i in range(2): 
        pyautogui.move(50, 0, duration=0.25)  # right 
        pyautogui.click(button='left')
        pyautogui.move(0, 50, duration=0.25)  # down
        pyautogui.click(button='left')
        pyautogui.move(-50, 0, duration=0.25) # left
        pyautogui.click(button='left')
        pyautogui.move(0, -50, duration=0.25) # up
        pyautogui.click(button='left')

    time.sleep(90.0 - ((time.time() - starttime) % 90.0))
    continue