import pyautogui
import time
time.sleep(5)
f = open("spam", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(600)
    pyautogui.press("enter")
