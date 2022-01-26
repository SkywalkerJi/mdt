import os
from random import expovariate
from threading import Thread
import pymem
import keyboard
import time
import json
import win32gui
import win32con
import configparser
import ctypes, sys

config_file = "config.ini"
cid_temp = 0
cid_temp_duel = 0
cid_temp_deck = 0
cid_temp_oppo = 0
translate_type = 0
pause = False
process_exit = False
enable_debug = False
baseAddress = None
pm = {}
deck_addr = None
duel_addr = None
oppo_addr = None
core_path = 'core'
sleep_time = 1


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
            deck_pointer_value = read_longlongs(pm, deck_addr, [0xB8, 0x0, 0xF8, 0x1D8]) + 0x20
            deck_cid = pm.read_int(deck_pointer_value)
            return deck_cid
        except:
            return 0
    while type == 2:
        try:
            duel_pointer_value = read_longlongs(pm, duel_addr, [0xB8, 0x0]) + 0x44
            duel_cid = pm.read_int(duel_pointer_value)
            return duel_cid
        except:
            return 0
    while type == 3:
        try:
            oppo_pointer_value = read_longlongs(pm, oppo_addr, [0xB8, 0x0, 0xF8, 0x140]) + 0x20
            oppo_cid = pm.read_int(oppo_pointer_value)
            return oppo_cid
        except:
            return 0


def valid_cid(cid: int):
    if cid > 0 and cid < 30000:
        return True
    else:
        return False


def translate(type: int):
    global cid_temp_duel
    global cid_temp_deck
    global cid_temp_oppo
    global baseAddress
    if baseAddress is None:
        try:
            get_baseAddress()
        except:
            print("地址没找到，不执行检测")
            return

    cid_duel = get_cid(1)
    cid_deck = get_cid(2)
    cid_oppo = get_cid(3)
    cid_update = False
    if valid_cid(cid_duel) and cid_duel != cid_temp_duel:
        cid_temp_duel = cid_duel
        cid = cid_duel
        cid_update = True
    elif valid_cid(cid_deck) and cid_deck != cid_temp_deck:
        cid_temp_deck = cid_deck
        cid = cid_deck
        cid_update = True
    elif valid_cid(cid_oppo) and cid_oppo != cid_temp_oppo:
        cid_temp_oppo = cid_oppo
        cid = cid_oppo
        cid_update = True

    if valid_cid(cid_duel) or valid_cid(cid_deck) or valid_cid(cid_oppo):
        if cid_update:
            cls()
            get_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"检测时间:{get_at}")
            print("-----------------------------------")
            try:
                card_t = cards_db[str(cid)]
                print(
                    f"{card_t['cn_name']}(密码:{card_t['id']})\n英文名:{card_t['en_name']}\n日文名:{card_t['jp_name']}\n{card_t['text']['types']}\n"
                )
                if card_t["text"]["pdesc"]:
                    print(f"灵摆效果:{card_t['text']['pdesc']}\n")
                print(f"{card_t['text']['desc']}\n")
            except:
                print(f"数据库中未查到该卡,cid:{cid}，如果是新卡请提交issue。如果是token衍生物请忽略。")
            print("-----------------------------------")
    else:
        cls()
        print("-----------------------------------")
        print("当前无选中卡片")
        print("-----------------------------------")


def translate_check_thread():
    global translate_type
    global pause
    global process_exit
    global enable_debug
    global sleep_time

    while not process_exit:
        if pause:
            cls()
            print("暂停")
            print(f"{switch_hotkey}切换检测卡组/决斗,{pause_hotkey}暂停检测,{exit_hotkey}退出程序\n")
        elif translate_type == 0:
            translate(translate_type + 1)
        # elif translate_type == 1:
        #     translate(translate_type + 1)
        else:
            print("Unknown Operator")
        time.sleep(sleep_time)
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
            print("已切换至决斗卡片检测模式")
        elif translate_type == 0:
            print("已切换至卡组卡片检测模式")


def get_baseAddress():
    global pm
    global baseAddress
    global deck_addr
    global duel_addr
    global oppo_addr
    pm = pymem.Pymem("masterduel.exe")
    print("Process id: %s" % pm.process_id)
    baseAddress = pymem.process.module_from_name(
        pm.process_handle, "GameAssembly.dll"
    ).lpBaseOfDll
    print("成功找到模块")
    # deck 组卡界面1 duel 决斗界面2
    deck_addr = baseAddress + int("0x01CCD278", base=16)
    duel_addr = baseAddress + int("0x01CB2B90", base=16)
    oppo_addr = baseAddress + int("0x01CCD278", base=16)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    # 判断UAC
    if not is_admin():
        stdout = os.popen('cd ' + core_path + ' && start mdt.exe ')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    # 加载配置文件
    con = configparser.ConfigParser()
    try:
        con.read(config_file, encoding="utf-8")
        config = con.items("config")
        config = dict(config)
        pause_hotkey = config["pause_hotkey"]
        exit_hotkey = config["exit_hotkey"]
        switch_hotkey = config["switch_hotkey"]
        # sleep_time = int(config["sleep_time"])
    except:
        print(f"未找到{config_file}配置文件或配置文件格式有误。")
    # 置顶功能
    '''
    if (config["window_on_top"] == "1") and config["lp_window_name"]:
        try:
            hwnd = win32gui.FindWindow(None, config["lp_window_name"])
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOPMOST,
                int(config["window_pos_x"]),
                int(config["window_pos_y"]),
                int(config["window_pos_cx"]),
                int(config["window_pos_cy"]),
                0,
            )
            print(f"窗口置顶成功,如需调整默认位置大小，可配置{config_file}")
        except:
            print(
                f"置顶失败,目前配置中窗口名为：{config['lp_window_name']}。请在配置文件中更改lp_window_name与上方窗口名一致，一般等于mdt.exe路径。"
            )
    elif config["window_on_top"] == "0":
        print("置顶功能已关闭")
    else:
        print(f"置顶功能配置异常，请检查{config_file}")
    '''
    # 加载卡片文本
    try:
        with open(config["cards_db"], "rb") as f:
            cards_db = json.load(f)
    except:
        print(f"未找到{config['cards_db']},请下载后放在同一目录")
    # 加载游戏
    try:
        get_baseAddress()
    except:
        print("游戏未启动，请先启动游戏，baseAddress not_found")

    # keyboard.add_hotkey(switch_hotkey, status_change, args=(True, False, False))
    keyboard.add_hotkey(exit_hotkey, status_change, args=(False, False, True))
    keyboard.add_hotkey(pause_hotkey, status_change, args=(False, True, False))

    p = Thread(target=translate_check_thread)
    p.start()
    p.join()
