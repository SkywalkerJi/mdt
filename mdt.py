import configparser
import contextlib
import ctypes
import json
import sys
import time
from threading import Thread

import keyboard
import pymem

import mdt_cv

config_file = "config.ini"
cid_temp = 0
cid_temp_duel = 0
cid_temp_deck = 0
cid_temp_oppo = 0
cid_show_gui = 0
pause = False
process_exit = False
baseAddress = None
pm = {}
deck_addr = None
duel_addr = None
oppo_addr = None
sleep_time = 0.1
cv_mode = 0
cards_db_CN = {}
cards_db_TW = {}
ur_tier_list = {}
sr_tier_list = {}
break_point = {}
bgm_list = {}
pause_hotkey = "ctrl+p"
switch_hotkey = "ctrl+s"


def read_longlongs(pm, base, offsets):
    value = pm.read_longlong(base)
    for offset in offsets:
        value = pm.read_longlong(value + offset)
    return value


def get_cid(type: int):  # sourcery skip: inline-immediately-returned-variable
    global pm
    global deck_addr
    global duel_addr
    global oppo_addr
    while type == 1:
        try:
            deck_pointer_value = (
                read_longlongs(pm, deck_addr, [0xB8, 0x0, 0xF8, 0x200]) + 0x2C
            )
            deck_cid = pm.read_int(deck_pointer_value)
            return deck_cid
        except Exception:
            return 0
    while type == 2:
        try:
            duel_pointer_value = read_longlongs(pm, duel_addr, [0xB8, 0x10]) + 0x4C
            duel_cid = pm.read_int(duel_pointer_value)
            return duel_cid
        except Exception:
            return 0
    while type == 3:
        try:
            oppo_pointer_value = (
                read_longlongs(pm, oppo_addr, [0xB8, 0x0, 0xF8, 0x138]) + 0x2C
            )
            oppo_cid = pm.read_int(oppo_pointer_value)
            return oppo_cid
        except Exception:
            return 0


def valid_cid(cid: int):
    return cid > 4000 and cid < 20000


def translate():
    global cid_temp_duel
    global cid_temp_deck
    global cid_temp_oppo
    global cid_show_gui
    global baseAddress
    if cv_mode == 0:
        if baseAddress is None:
            try:
                get_baseAddress()
            except Exception:
                return
        cid_deck = get_cid(1)
        cid_duel = get_cid(2)
        cid_oppo = get_cid(3)

        if valid_cid(cid_oppo) and cid_oppo != cid_temp_oppo:
            cid_temp_oppo = cid_oppo
            cid_show_gui = cid_oppo
        if valid_cid(cid_deck) and cid_deck != cid_temp_deck:
            cid_temp_deck = cid_deck
            cid_show_gui = cid_deck
        if valid_cid(cid_duel) and cid_duel != cid_temp_duel:
            cid_temp_duel = cid_duel
            cid_show_gui = cid_duel
    elif cv_mode == 1:
        cid_show_gui = mdt_cv.get_scan()


def translate_check_thread():
    global pause
    global process_exit
    global sleep_time
    while not process_exit:
        if not pause:
            translate()
        time.sleep(sleep_time)


def status_change(switch: bool, need_pause: bool, exit: bool):
    global pause
    global process_exit
    process_exit = exit
    pause = need_pause


def get_baseAddress():
    global pm
    global baseAddress
    global deck_addr
    global duel_addr
    global oppo_addr
    pm = pymem.Pymem("masterduel.exe")
    baseAddress = pymem.process.module_from_name(
        pm.process_handle, "GameAssembly.dll"
    ).lpBaseOfDll
    # deck 组卡界面 duel 决斗界面 oppo 回放
    deck_addr = baseAddress + int("0x01F501A8", base=16)
    duel_addr = baseAddress + int("0x01F31E48", base=16)
    oppo_addr = baseAddress + int("0x01F501A8", base=16)


# UAC判断
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


# UAC重开
def uac_reload():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


# 加载配置文件
def config_load():
    global pause_hotkey
    global switch_hotkey
    global cards_db_CN
    global cards_db_TW
    global ur_tier_list
    global sr_tier_list
    global break_point
    global bgm_list
    con = configparser.ConfigParser()
    with contextlib.suppress(Exception):
        con.read(config_file, encoding="utf-8")
        config = con.items("cli")
        config = dict(config)
        pause_hotkey = config["pause_hotkey"]
        switch_hotkey = config["switch_hotkey"]
    # 加载卡片文本
    with contextlib.suppress(Exception):
        with open("./locales/zh-CN/cards.json", "rb") as f:
            cards_db_CN = json.load(f)
    with contextlib.suppress(Exception):
        with open("./locales/zh-TW/cards.json", "rb") as f:
            cards_db_TW = json.load(f)
    with contextlib.suppress(Exception):
        with open("./data/ur.json", "rb") as f:
            ur_tier_list = json.load(f)
    with contextlib.suppress(Exception):
        with open("./data/sr.json", "rb") as f:
            sr_tier_list = json.load(f)
    with contextlib.suppress(Exception):
        with open("./data/breakpoint.json", "rb") as f:
            break_point = json.load(f)
    with contextlib.suppress(Exception):
        with open("./data/bgm.json", "rb") as f:
            bgm_list = json.load(f)


def get_current_cid():
    translate()
    return int(cid_show_gui)


def main():
    uac_reload()
    # 加载游戏
    with contextlib.suppress(Exception):
        get_baseAddress()
    config_load()
    keyboard.add_hotkey(switch_hotkey, status_change, args=(True, False, False))
    keyboard.add_hotkey(pause_hotkey, status_change, args=(False, True, False))
    p = Thread(target=translate_check_thread)
    p.start()
    p.join()


if __name__ == "__main__":
    main()
