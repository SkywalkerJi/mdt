import os
from threading import Thread
import pymem
import keyboard
import time
import json

pause_hotkey = "ctrl+p"
exit_hotkey = "ctrl+q"
switch_hotkey = "ctrl+s"

cards_dir = "./cards.json"

cid_temp = 0

# 清理终端
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def read_longlongs(pm, base, offsets):
    value = pm.read_longlong(base)
    for offset in offsets:
        value = pm.read_longlong(value + offset)
    return value


def get_cid(type: int):
    global pm
    global deck_addr
    global duel_addr
    while type == 1:
        try:
            deck_pointer_value = (
                read_longlongs(pm, deck_addr, [0xB8, 0x0, 0xF8, 0x1D8]) + 0x20
            )

            deck_cid = pm.read_int(deck_pointer_value)
            # print({"deck_cid": deck_cid})
            return deck_cid
        except:
            print({"deck_cid not_found"})
            return 0

    while type == 2:
        try:
            duel_pointer_value = read_longlongs(pm, duel_addr, [0xB8, 0x0]) + 0x44

            duel_cid = pm.read_int(duel_pointer_value)
            # print({"duel_cid": duel_cid})
            return duel_cid
        except:
            print({"duel_cid not_found"})
            return 0


def translate(type: int):
    global cid_temp
    global baseAddress
    if baseAddress is None:
        print("地址没找到，不执行检测")
        return
    if type == 1:
        # print("翻译卡组卡片")
        cid = get_cid(type)
    elif type == 2:
        # print("翻译决斗卡片")
        cid = get_cid(type)
    else:
        print("not support")
        return
    if cid and cid_temp != cid:
        cls()
        get_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"检测时间:{get_at}")
        cid_temp = cid
        card_t = cards_db[str(cid)]
        print(
            f"{card_t['cn_name']}(密码:{card_t['id']})\n英文名:{card_t['en_name']}\n日文名:{card_t['jp_name']})\n{card_t['text']['types']}\n{card_t['text']['desc']}\n"
        )
        print("-----------------------------------")
        print(f"{switch_hotkey}切换检测卡组/决斗详细卡片信息,{pause_hotkey}暂停检测,{exit_hotkey}退出程序\n")


# 循环
translate_type = 0
pause = True
process_exit = False
enable_debug = False


def translate_check_thread():
    global translate_type
    global pause
    global process_exit
    global enable_debug

    while not process_exit:
        if pause:
            cls()
            print("暂停")
            print(f"{switch_hotkey}切换检测卡组/决斗,{pause_hotkey}暂停检测,{exit_hotkey}退出程序\n")
        elif translate_type == 0:
            translate(translate_type + 1)
        elif translate_type == 1:
            translate(translate_type + 1)
        else:
            print("Unknown Operator")
        time.sleep(1)
    print("程序结束")


def status_change(switch: bool, need_pause: bool, exit: bool):
    global translate_type
    global pause
    global process_exit
    global enable_debug
    process_exit = exit
    pause = need_pause
    if switch:
        translate_type = int(not bool(translate_type))
        if translate_type == 1:
            print("翻译卡组卡片")
        elif translate_type == 0:
            print("翻译决斗卡片")


if __name__ == "__main__":
    with open("cards.json", "rb") as f:
        cards_db = json.load(f)
    pm = pymem.Pymem("masterduel.exe")
    print("Process id: %s" % pm.process_id)
    try:
        baseAddress = pymem.process.module_from_name(
            pm.process_handle, "GameAssembly.dll"
        ).lpBaseOfDll
        print("success")
        # deck 组卡界面1 duel 决斗界面2
        deck_addr = baseAddress + int("0x01CCD278", base=16)
        duel_addr = baseAddress + int("0x01cb2b90", base=16)
    except:
        print("baseAddress not_found")

    keyboard.add_hotkey(switch_hotkey, status_change, args=(True, False, False))
    keyboard.add_hotkey(exit_hotkey, status_change, args=(False, False, True))
    keyboard.add_hotkey(pause_hotkey, status_change, args=(False, True, False))

    p = Thread(target=translate_check_thread)
    p.start()
    p.join()
