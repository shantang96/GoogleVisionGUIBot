import pyautogui
from time import sleep

#urlx = https://cloud.google.com/vision/
x=0

#OPEN FIREFOX
pyautogui.hotkey('command', 'space')
pyautogui.hotkey('f')
pyautogui.hotkey('i')
pyautogui.hotkey('r')
pyautogui.hotkey('e')
pyautogui.hotkey('enter')
sleep(1)

#PASTE URL
pyautogui.moveTo(287, 76)
pyautogui.hotkey('command', 'l')
pyautogui.hotkey('command', 'v')
pyautogui.hotkey('enter')
sleep(2)
#(learn how to loop through a string to simulate typing using a for loop- for urls)

#SCROLL DOWN TO IMAGE BOX
x=15;
while x > 0:
    pyautogui.hotkey('down')
    sleep(0.25)
    x=x-1

'''
#GO TO DESKTOP (FOX DRAG & DROP) NEVERMIND.
pyautogui.moveTo(0, 800)
'''

#CLICK IMAGE BOX
pyautogui.moveTo(618, 325)
pyautogui.click()
pyautogui.moveTo(576, 167)
sleep(2)
pyautogui.doubleClick()
pyautogui.hotkey('enter')


'''
pyautogui.moveTo(259, 46)
while x < 100000:
 pyautogui.hotkey('command', 't')
 #sleep(0.01)
 pyautogui.hotkey('command', 'l')
 #sleep(0.01)
 pyautogui.hotkey('command', 'v')
 #sleep(0.01)
 pyautogui.hotkey('enter')
 x=x+1
 #sleep(0.01)
 
 if x%17 == 0:
    #sleep(3)
    for x in range(0, 5):
     pyautogui.hotkey('command', 'w')
     sleep(0.1)
 #sleep()
'''
