from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import pyautogui

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    print(key)
    currentMouseX, currentMouseY = pyautogui.position()
    if key == "Hat 0 [Right]":
        print("right")
        pyautogui.moveTo(currentMouseX+20, currentMouseY)
    elif key == "Hat 0 [Left]":
        print("left")
        pyautogui.moveTo(currentMouseX-20, currentMouseY)
    elif key == "Hat 0 [Down]":
        print("Down")
        pyautogui.moveTo(currentMouseX, currentMouseY+20)
    elif key == "Hat 0 [Up]":
        print("up")
        pyautogui.moveTo(currentMouseX, currentMouseY-20)
    elif key == "Axis 2":
        print("click")
        pyautogui.click()
    elif key == "Axis 5":
        print("click")
        pyautogui.rightClick()
    elif key == "-Axis 4":
        print("click")
        pyautogui.scroll(20)
    elif key == "Axis 4":
        print("click")
        pyautogui.scroll(-20)
    elif key == "Button 2":
        print("click")
        pyautogui.hotkey('ctrl', 'x')
    elif key == "Button 3":
        print("click")
        pyautogui.hotkey('ctrl', 'c')
    elif key == "Button 1":
        print("click")
        pyautogui.hotkey('ctrl', 'v')
    elif key == "Button 0":
        print("click")
        pyautogui.hotkey('ctrl', 'z')

run_event_loop(print_add, print_remove, key_received)