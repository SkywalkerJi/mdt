from threading import Thread
from unicodedata import name

import mdt as mdt
import mdt_deck_reader as reader

import win32api
import win32con
import win32gui
import time
import pyautogui
import pyperclip

def start():
    mdt_service = Thread(target=mdt.main)
    mdt_service.start()


def run():
    mdt.status_change(True, False, False)


def exit():
    mdt.status_change(False, False, True)


def pause():
    mdt.status_change(False, True, False)


def get_cid():
    if mdt.cid_show_gui:
        return mdt.cid_show_gui
    else:
        return None


def set_cv_mode():
    if mdt.cv_mode == 0:
        mdt.cv_mode = 1
    else:
        mdt.cv_mode = 0


def get_cards_db(locale: str):
    if locale == "zh-CN":
        if mdt.cards_db_CN:
            return mdt.cards_db_CN
        else:
            return None
    elif locale == "zh-TW":
        if mdt.cards_db_TW:
            return mdt.cards_db_TW
        else:
            return None


def get_card_tier(cid: str):
    if mdt.ur_tier_list and mdt.sr_tier_list:
        if cid in mdt.ur_tier_list:
            return mdt.ur_tier_list[cid]["tier"]
        elif cid in mdt.sr_tier_list:
            return mdt.sr_tier_list[cid]["tier"]
        else:
            return None
    else:
        return None


def get_break_point(cid: str):
    if mdt.break_point:
        if cid in mdt.break_point:
            return mdt.break_point[cid]["tier"]
    else:
        return None


def get_bgm(cid: str):
    if mdt.bgm_list:
        if cid in mdt.bgm_list:
            return mdt.bgm_list[cid]["file"]
    else:
        return None


def get_deck_dict():
    return reader.get_deck_dict()


def get_deck_string(locale: str):
    return reader.get_deck_string(locale)

def ydk_converter(ydk_deck: str, game_client_locale: str='en'):
    tmp=reader.ydk_converter(ydk_deck, game_client_locale)
    hWnd = win32gui.FindWindow(None, "masterduel")
    win32gui.SetForegroundWindow(hWnd)
    
    tmp.sort()
    blank=(1083, 171)
    search=(1400, 295)
    clear=(1670, 295)
    card=(1400, 440)
    if tmp is not None:
        for index, element in enumerate(tmp):
            if index == 0 or element != tmp[index-1]:
                print(index)
                pyautogui.click(blank, interval=.2)
                pyautogui.click(clear)
                pyautogui.click(blank, interval=.2)
                pyautogui.click(search)
                pyperclip.copy(element)
                pyperclip.paste()
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(1.5)
            print(f"{element}\n")
            pyautogui.rightClick(card)

if __name__ == "__main__":
    ydk_converter("", "")