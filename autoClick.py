import keyboard, pyautogui

def autoClick():
    a,b = pyautogui.position()
    while True:
        try:
            pyautogui.click()
            x,y = pyautogui.position()
        except:
            pass

        # automatic Click Cancell
        if not a == x and not b == y: break

# automatic Click Start
keyboard.add_hotkey("s", autoClick)

keyboard.wait()