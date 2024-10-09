import time
import pyautogui
import sys

def type_physical(text, delay=0.2):

    for i in text:
        pyautogui.typewrite(i)
        time.sleep(delay)

def erase_physical(text, delay=0.2):
    for i in range(len(text)):
        pyautogui.press('backspace')
        time.sleep(delay)

def type_remove_physical(text, tbt, delay=0.2, delay_del = 0.2, delay_start = 5):
    time.sleep(delay_start)
    type_physical(text, delay)
    time.sleep(tbt)
    erase_physical(text, delay_del)

def write(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def erase(text, delay=0.2):
    for i in range(len(text)):
        sys.stdout.write('\b')
        sys.stdout.flush()
        time.sleep(delay)

def write_and_erase(text, tbt, delay = 0.2, delay_del = 0.2):
    write(text, delay)
    time.sleep(tbt)
    erase(text, delay_del)