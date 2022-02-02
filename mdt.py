from threading import Thread
import pymem
import keyboard
import time
import json
import configparser
import ctypes, sys

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
cards_db_CN = {}
cards_db_TW = {}
pause_hotkey = "ctrl+p"
switch_hotkey = "ctrl+s"


def read_longlongs(pm, base, offsets):
    value = pm.read_longlong(base)
    for offset in offsets:
        value = pm.read_longlong(value + offset)
    return value


def get_cid(type: int):
    global pm
    global deck_addr
    global duel_addr
    global oppo_addr
    while type == 1:
        try:
            deck_pointer_value = (
                read_longlongs(pm, deck_addr, [0xB8, 0x0, 0xF8, 0x1D8]) + 0x20
            )
            deck_cid = pm.read_int(deck_pointer_value)
            return deck_cid
        except Exception:
            return 0
    while type == 2:
        try:
            duel_pointer_value = read_longlongs(pm, duel_addr, [0xB8, 0x0]) + 0x44
            duel_cid = pm.read_int(duel_pointer_value)
            return duel_cid
        except Exception:
            return 0
    while type == 3:
        try:
            oppo_pointer_value = (
                read_longlongs(pm, oppo_addr, [0xB8, 0x0, 0xF8, 0x140]) + 0x20
            )
            oppo_cid = pm.read_int(oppo_pointer_value)
            return oppo_cid
        except Exception:
            return 0


def valid_cid(cid: int):
    if cid > 4000 and cid < 20000:
        return True
    else:
        return False


def translate():
    global cid_temp_duel
    global cid_temp_deck
    global cid_temp_oppo
    global cid_show_gui
    global baseAddress
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
    deck_addr = baseAddress + int("0x01CCD278", base=16)
    duel_addr = baseAddress + int("0x01cb2b90", base=16)
    oppo_addr = baseAddress + int("0x01CCD278", base=16)


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
    con = configparser.ConfigParser()
    try:
        con.read(config_file, encoding="utf-8")
        config = con.items("cli")
        config = dict(config)
        pause_hotkey = config["pause_hotkey"]
        switch_hotkey = config["switch_hotkey"]
    except Exception:
        pass
    # 加载卡片文本
    try:
        with open("./locales/zh-CN/cards.json", "rb") as f:
            cards_db_CN = json.load(f)
    except Exception:
        pass
    try:
        with open("./locales/zh-TW/cards.json", "rb") as f:
            cards_db_TW = json.load(f)
    except Exception:
        pass


def main():
    uac_reload()
    # 加载游戏
    try:
        get_baseAddress()
    except Exception:
        pass
    config_load()
    keyboard.add_hotkey(switch_hotkey, status_change, args=(True, False, False))
    keyboard.add_hotkey(pause_hotkey, status_change, args=(False, True, False))
    p = Thread(target=translate_check_thread)
    p.start()
    p.join()


if __name__ == "__main__":
    main()
