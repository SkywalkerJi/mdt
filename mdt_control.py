import time
import win32gui
import pyautogui
import pyperclip
import numpy as np

from mdt_cv import get_reset_button_postion, get_scale, get_search_button_postion

pyautogui.FAILSAFE= True
blank_offset = (0, -150)
clear_offset = (335, 0)
card_offset = (0, 170)

def _add(a: tuple, b: tuple, scale=1.0):
    return a[0]+b[0]*scale, a[1]+b[1]*scale

def ydk_converter(ydk_deck: list[str]):
    """
    Convert YDK deck list to MDT deck.
    """
    # TODO: background click
    # TODO: 卡组校验
    # TODO: 出现多张候选时进行遍历
    # TODO: 清空当前牌组
    if ydk_deck is None or ydk_deck == []:
        return

    hWnd = win32gui.FindWindow(None, "masterduel")
    win32gui.SetForegroundWindow(hWnd)
    box = win32gui.ClientToScreen(hWnd, (0, 0))
    # 先横后竖
    search = get_search_button_postion()
    search = _add(search, box)
    reset = get_reset_button_postion()
    reset = _add(reset, box)
    blank = _add(search, blank_offset, get_scale())
    clear = _add(search, clear_offset, get_scale())
    card = _add(search, card_offset, get_scale())
    pyautogui.click(reset, interval=.5)

    for index, element in enumerate(ydk_deck):
        if index == 0 or element != ydk_deck[index-1]:
            pyautogui.click(clear, interval=.2)
            pyautogui.click(search)
            pyautogui.click(blank, interval=.2)
            pyautogui.click(search)
            # 粘贴卡片名
            pyperclip.copy(element)
            pyperclip.paste()
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            # 等待搜索完成
            time.sleep(1)
        print(f"{element}\n")
        pyautogui.rightClick(card)


def main():
    ydk_converter([1])


if __name__ == "__main__":
    main()
