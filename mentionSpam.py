# First keep your messenger open then, run this program and switch to messenger. enjoy !

import pyautogui
import time

print("Switch to Messenger! Starting in 5 seconds...")
time.sleep(5)

pyautogui.click(1107, 983) # Use your mouse coordinates here. This will move your mouse to that messenger chatbox according to the coordinates.
for i in range(10):
    pyautogui.write("@your friend's name", interval=0.2) # In the string section write the id name of your friend. But first mention yourself then paste that name.
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')

print("Done!")
