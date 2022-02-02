from threading import Thread
import pymem
import keyboard
import time
import json
import win32gui
import win32con
import configparser
import ctypes, sys
from click import clear

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
show_all_info = 1
cards_db = {}
exit_hotkey = "ctrl+q"
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
            oppo_pointer_value = (
                read_longlongs(pm, oppo_addr, [0xB8, 0x0, 0xF8, 0x140]) + 0x20
            )
            oppo_cid = pm.read_int(oppo_pointer_value)
            return oppo_cid
        except:
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
    global show_all_info
    if baseAddress is None:
        try:
            get_baseAddress()
        except:
            print("游戏未找到，请打开游戏")
            return
    cid_deck = get_cid(1)
    cid_duel = get_cid(2)
    cid_oppo = get_cid(3)
    cid_update = False

    if valid_cid(cid_oppo) and cid_oppo != cid_temp_oppo:
        cid_temp_oppo = cid_oppo
        cid_update = True
        cid_show_gui = cid_oppo
    if valid_cid(cid_deck) and cid_deck != cid_temp_deck:
        cid_temp_deck = cid_deck
        cid_update = True
        cid_show_gui = cid_deck
    if valid_cid(cid_duel) and cid_duel != cid_temp_duel:
        cid_temp_duel = cid_duel
        cid_update = True
        cid_show_gui = cid_duel
    if cid_update:
        clear()
        if show_all_info == 1:
            get_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"检测时间:{get_at}")
            print("-----------------------------------")
        print_card(cid_show_gui)
        # print("----------↓回放模式↓----------------")
        # print_card(cid_oppo)
        # print("----------↓决斗模式↓----------------")
        # print_card(cid_duel)
        # print("----------↓卡组模式↓-----------------")
        # print_card(cid_deck)
        if show_all_info == 1:
            print("-----------------------------------")
            print(f"{switch_hotkey}开启检测,{pause_hotkey}暂停检测,{exit_hotkey}退出程序\n")


def print_card(cid: int):
    global show_all_info
    if valid_cid(cid):
        try:
            card_t = cards_db[str(cid)]
            print(f"{card_t['cn_name']}(密码:{card_t['id']})")
            if show_all_info == 1:
                try:
                    print(
                        f"英文名:{card_t['en_name']}\n日文名:{card_t['jp_name']})\n{card_t['text']['types']}"
                    )
                except:
                    print(f"cid:{cid}卡信息有误，请提交issue。\n")
            if card_t["text"]["pdesc"]:
                print(f"灵摆效果:{card_t['text']['pdesc']}\n")
            print(f"{card_t['text']['desc']}\n")
        except:
            print(f"数据库中未查到该卡,cid:{cid}，如果是新卡请提交issue。如果是token衍生物请忽略。")
    else:
        return 0


def translate_check_thread():
    global pause
    global process_exit
    global sleep_time
    while not process_exit:
        if pause:
            clear()
            print("暂停检测")
            print(f"{switch_hotkey}开启检测,{pause_hotkey}暂停检测,{exit_hotkey}退出程序\n")
        else:
            translate()
        time.sleep(sleep_time)
    print("程序结束")


def status_change(switch: bool, need_pause: bool, exit: bool):
    global pause
    global process_exit
    process_exit = exit
    pause = need_pause
    if switch:
        print("已开启检测，请点击一张卡片")


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
    # deck 组卡界面 duel 决斗界面 oppo 回放
    deck_addr = baseAddress + int("0x01CCD278", base=16)
    duel_addr = baseAddress + int("0x01cb2b90", base=16)
    oppo_addr = baseAddress + int("0x01CCD278", base=16)


# UAC判断
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
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
    global exit_hotkey
    global switch_hotkey
    global show_all_info
    global cards_db
    con = configparser.ConfigParser()
    try:
        con.read(config_file, encoding="utf-8")
        config = con.items("cli")
        config = dict(config)
        pause_hotkey = config["pause_hotkey"]
        exit_hotkey = config["exit_hotkey"]
        switch_hotkey = config["switch_hotkey"]
        show_all_info = int(config["show_all_info"])
    except:
        print(f"未找到{config_file}配置文件或配置文件格式有误。")
    # cli置顶功能
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
            print(f"CLI窗口置顶成功,如需调整默认位置大小，可配置{config_file}")
        except:
            print(
                f"CLI置顶失败,目前配置中窗口名为：{config['lp_window_name']}。请在{config_file}配置文件中更改lp_window_name与CLI窗口名一致，一般等于mdt.exe路径。"
            )
    elif config["window_on_top"] == "0":
        print(f"CLI置顶功能已关闭,如有需要请在{config_file}中开启")
    else:
        print(f"置顶功能配置异常，请检查{config_file}")
    # 加载卡片文本
    try:
        with open("./locales/zh-CN/cards.json", "rb") as f:
            cards_db = json.load(f)
    except:
        print(f"未找到cards_db.json,请下载后放在/locales/zh-CN/下")


def main():
    uac_reload()
    # 加载游戏
    try:
        get_baseAddress()
    except:
        print("未找到地址，可能是游戏未启动 或 没有使用管理员权限运行MDT")
    config_load()
    keyboard.add_hotkey(switch_hotkey, status_change, args=(True, False, False))
    keyboard.add_hotkey(exit_hotkey, status_change, args=(False, False, True))
    keyboard.add_hotkey(pause_hotkey, status_change, args=(False, True, False))
    p = Thread(target=translate_check_thread)
    p.start()
    p.join()


if __name__ == "__main__":
    main()
