import pyautogui
import time


class Macro:

    def __init__(self):
        self.__macroAtivo = False

    def press_key(self, hold_time: float, key: str, delay=0):
        start = time.time()
        while time.time() - start < hold_time:
            pyautogui.press(key)
            time.sleep(delay)

    def click_mouse(self, hold_time: int, button='left', delay=0):
        start = time.time()
        while time.time() - start < hold_time:
            pyautogui.click(button=button)
            time.sleep(delay)
