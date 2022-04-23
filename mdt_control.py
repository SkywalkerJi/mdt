from glob import glob
import time
import win32gui
import pyautogui
import pyperclip
import numpy as np
from mdt import get_current_cid
import mdt_deck_reader

from mdt_cv import get_reset_button_postion, get_scale, get_search_button_postion

# pyautogui 强制关闭
pyautogui.FAILSAFE = True

# 1920x1080 分辨率下的偏移量，可以通过分辨率换算进行变换
blank_offset = (0, -150)
clear_offset = (335, 0)
card_offset = (0, 170)
card_width_offset = 89
card_height_offset = 144

# 用来处理同一个名字搜索出多个卡片的全局变量
last_cid = -1
last_target_position = None


def _add(a: tuple, b: tuple, scale=1.0):
    return a[0]+b[0]*scale, a[1]+b[1]*scale


def ydk_converter(ydk_deck: list[tuple], locale: str):
    """
    Convert YDK deck list to MDT deck.
    """
    # TODO: background click
    # TODO: 清空当前牌组
    # TODO: 等待搜索时间可调
    if ydk_deck is None or ydk_deck == []:
        return

    hWnd = win32gui.FindWindow(None, "masterduel")
    win32gui.SetForegroundWindow(hWnd)
    box = win32gui.ClientToScreen(hWnd, (0, 0))

    scale = get_scale()
    # 先横后竖
    search = get_search_button_postion()
    search = _add(search, box)
    reset = get_reset_button_postion()
    reset = _add(reset, box)
    blank = _add(search, blank_offset, scale)
    clear = _add(search, clear_offset, scale)
    card = _add(search, card_offset, scale)
    target_card_position = None

    pyautogui.click(reset, interval=.5)
    for index, tup in enumerate(ydk_deck):
        element, cid = tup
        if index == 0 or element != ydk_deck[index-1][0]:
            pyautogui.click(clear, interval=.1)
            pyautogui.click(blank, interval=.1)
            pyautogui.click(search)
            # 粘贴卡片名
            pyperclip.copy(element)
            pyperclip.paste()
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            # 等待搜索完成
            time.sleep(1.2)
            # 处理搜索得到多卡片的情况
            target_card_position = travel_through_deck(card,
                                                       card_width_offset*scale,
                                                       card_height_offset*scale,
                                                       int(cid))
        print(f"{element}\n")
        pyautogui.rightClick(target_card_position)
    
    # 对卡组进行校验
    mdt_deck_reader.check_deck([int(i[1]) for i in ydk_deck], locale)


def travel_through_deck(start, width_step, height_step, target_cid=-1):
    global last_cid, last_target_position

    # 竖
    for i in range(5):
        # 横
        for j in range(6):
            click_position = start[0]+width_step*j, start[1]+height_step*i
            pyautogui.click(click_position)
            cid = get_current_cid()
            if cid == target_cid:
                return click_position
            elif cid == last_cid:
                return last_target_position

            # TODO: 如果搜索不到就不添加
            last_cid = cid
            last_target_position = click_position
