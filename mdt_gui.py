import os
import ctypes, sys
import PySimpleGUI as sg
import mdt_service as service

core_path = "core"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def uac_reload():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


def main():
    cards_db = None
    cid_temp = 0
    card_frame = [
        [
            sg.Frame(
                "卡名",
                [
                    [sg.T(key="-cn_name-", s=(30, None))],
                ],
                title_color="blue",
            )
        ],
        [
            sg.Frame(
                "类型",
                [
                    [sg.T(key="-types-", s=(30, None))],
                ],
                title_color="blue",
            )
        ],
        [
            sg.Frame(
                "效果",
                [
                    [sg.T(key="-desc-", s=(30, None))],
                ],
                title_color="blue",
            )
        ],
        [
            sg.Frame(
                "灵摆",
                [
                    [sg.T(key="-pdesc-", s=(30, None))],
                ],
                title_color="blue",
                visible=False,
                key="-pdesc_frame-",
            )
        ],
    ]

    layout = [
        [card_frame],
    ]

    window = sg.Window(
        "MDT v0.2.0 @SkywalkerJi",
        layout,
        default_element_size=(12, 1),
        font=("Microsoft YaHei", 12),
        keep_on_top=True,
        resizable=True,
    )
    uac_reload()
    service.start()

    while True:
        event, values = window.read(timeout=100)
        cid = service.get_cid()
        if not cards_db:
            cards_db = service.get_cards_db()
        if cid != cid_temp:
            cid_temp = cid
            try:
                card_t = cards_db[str(cid)]
                window["-cn_name-"].update(card_t["cn_name"])
                window["-types-"].update(card_t["text"]["types"])
                if card_t["text"]["pdesc"]:
                    window["-pdesc_frame-"].update(visible=True)
                    window["-pdesc-"].update(card_t["text"]["pdesc"])
                else:
                    window["-pdesc_frame-"].update(visible=False)
                window["-desc-"].update(card_t["text"]["desc"])
            except:
                print("数据库中未查到该卡")
        if event in (sg.WIN_CLOSED, "Exit"):
            break
    service.exit()
    window.close()


if __name__ == "__main__":
    main()
