import pyautogui
import pynput
import time
import webbrowser
from pynput.mouse import Button, Controller

mouse = Controller()

webbrowser.register('firefox',
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open("cfchome.org/livestream")

# enter fullscreen
time.sleep(5)
mouse.position = (1345, 853)
mouse.click(Button.left, 1)

# switch to Discord
time.sleep(1)
pyautogui.press('winleft')
mouse.position = (916, 1067)
mouse.click(Button.left, 1)
time.sleep(1)

# go to ISR Happenings channel
mouse.position = (48,164)
mouse.click(Button.left, 1)

# enter Sunday Service channel
mouse.position = (209, 434)
time.sleep(1)
mouse.scroll(0, 8)
time.sleep(1) # wait to scroll
mouse.click(Button.left, 1)

# share screen
mouse.position = (294, 936)
time.sleep(1) # wait to connect
mouse.click(Button.left, 1) # click 'Share Screen'
time.sleep(3) # wait for screens to load
mouse.position = (1102, 504)
time.sleep(2)
mouse.click(Button.left, 1) # click on proper screen
mouse.position = (1144, 783)
time.sleep(1) # wait for cursor to move
mouse.click(Button.left, 1) # press 'Go Live'
mouse.position = (0, 0)

# stream for duration of service
time.sleep(5300)

# end stream
mouse.position = (368, 882)
mouse.click(Button.left, 1) # click 'Disconnect'

print("Done")