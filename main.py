import pyautogui, time
import keyboard
time.sleep(5) # Time to wait before it starts.
file = open("spam_text.txt", 'r')
for word in file:
    pyautogui.typewrite(word) # Content to be written
    pyautogui.write(['enter']) # Enter to send or newline
    time.sleep(1)
    if keyboard.is_pressed('esc'): # ESC to stop (Must be pressed in CLI)
        break
