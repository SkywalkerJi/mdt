import ctypes, sys
import PySimpleGUI as sg
import mdt_service as service
import pyperclip
import configparser
import webbrowser

config_file = "config.ini"
font_size = 12
window_alpha = 0.96
keep_on_top = True
ui_lock = False
cfg = configparser.ConfigParser()
sync_ui = 0
show_all_info = True
web_search = True
x_loc = 960
y_loc = 540
x_len = 400
y_len = 600


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def uac_reload(bool=False):
    if not is_admin() or bool:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


def set_ui_lock(window, bool):
    window["-keep_on_top-"].update(disabled=bool)
    window["-window_alpha-"].update(disabled=bool)
    window["-font_size-"].update(disabled=bool)
    window["-show_all_info-"].update(disabled=bool)
    window["-web_search-"].update(disabled=bool)
    config_set("ui_lock", str(int(bool)))


def config_load():
    global font_size
    global window_alpha
    global keep_on_top
    global ui_lock
    global show_all_info
    global web_search
    global x_loc
    global y_loc
    global x_len
    global y_len
    global cfg
    try:
        cfg.read(config_file, encoding="utf-8")
        config = cfg.items("gui")
        config = dict(config)
        font_size = int(config["font_size"])
        window_alpha = float(config["window_alpha"])
        keep_on_top = bool(int(config["keep_on_top"]))
        ui_lock = bool(int(config["ui_lock"]))
        show_all_info = bool(int(config["show_all_info"]))
        web_search = bool(int(config["web_search"]))
        x_loc = int(config["x_loc"])
        y_loc = int(config["y_loc"])
        x_len = int(config["x_len"])
        y_len = int(config["y_len"])
    except:
        pass
        # print(f"未找到{config_file}配置文件或配置檔案格式有誤。")


def config_set(option: str, value: str):
    cfg.set("gui", option, value)
    with open(config_file, "w+") as f:
        cfg.write(f)


def main():
    global sync_ui
    global web_search
    settings_active = False
    uac_reload()
    service.start()
    config_load()
    cards_db = None
    cid_temp = 0
    text_keys = (
        "-cn_name-",
        "-pdesc-",
        "-desc-",
        "-types-",
        "-en_name-",
        "-jp_name-",
        "-id-",
    )
    card_frame = [
        [
            sg.Frame(
                "卡名",
                [
                    [
                        sg.T(
                            text="等待偵測",
                            key="-cn_name-",
                            enable_events=True,
                            expand_x=True,
                        )
                    ],
                ],
                title_color="#61E7DC",
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    "靈擺",
                    [
                        [
                            sg.Multiline(
                                key="-pdesc-",
                                s=(None, 5),
                                background_color="#64778D",
                                text_color="white",
                                write_only=True,
                                auto_refresh=True,
                                rstrip=True,
                            )
                        ],
                    ],
                    title_color="#61E7DC",
                    visible=False,
                    key="-pdesc_frame-",
                ),
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                "描述",
                [
                    [
                        sg.Multiline(
                            key="-desc-",
                            background_color="#64778D",
                            text_color="white",
                            write_only=True,
                            auto_refresh=True,
                            rstrip=True,
                            expand_x=True,
                            expand_y=True,
                        )
                    ]
                ],
                title_color="#61E7DC",
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    "類型",
                    [
                        [
                            sg.T(
                                key="-types-",
                                enable_events=True,
                                s=(40, 2),
                            )
                        ],
                    ],
                    title_color="#61E7DC",
                    visible=show_all_info,
                    key="-types_frame-",
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    "英文名",
                    [
                        [
                            sg.T(
                                key="-en_name-",
                                enable_events=True,
                                s=(40, 1),
                            )
                        ],
                    ],
                    title_color="#61E7DC",
                    visible=show_all_info,
                    key="-en_name_frame-",
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    "日文名",
                    [
                        [
                            sg.T(
                                key="-jp_name-",
                                enable_events=True,
                                s=(40, 1),
                            )
                        ],
                    ],
                    title_color="#61E7DC",
                    visible=show_all_info,
                    key="-jp_name_frame-",
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    "卡號",
                    [
                        [
                            sg.T(
                                key="-id-",
                                enable_events=True,
                                s=(40, 1),
                            )
                        ],
                    ],
                    title_color="#61E7DC",
                    visible=show_all_info,
                    key="-id_frame-",
                ),
                expand_x=True,
            )
        ],
    ]
    right_click_menu = [
        "&Right",
        ["設定", "保存視窗位置", "恢復預設", "檢查更新", "反和諧補丁", "聯繫開發者"],
    ]
    layout = [[card_frame]]
    window = sg.Window(
        "MDT v0.2.3 @SkywalkerJi GPLv3",
        layout,
        default_element_size=(12, 1),
        font=("Microsoft YaHei", font_size),
        keep_on_top=keep_on_top,
        resizable=True,
        alpha_channel=window_alpha,
        right_click_menu=right_click_menu,
        location=(x_loc, y_loc),
        size=(x_len, y_len),
    )
    # 判斷螢幕尺寸
    screen = window.get_screen_dimensions()
    if screen[0] < x_loc or screen[1] < y_loc:
        config_set("x_loc", str(screen[0] / 2))
        config_set("y_len", str(screen[1] / 2))
        uac_reload(True)

    while True:
        event, values = window.read(timeout=100)
        cid = service.get_cid()
        # print(event, values)
        # 載入db

        if not cards_db:
            cards_db = service.get_cards_db()
        if cid != cid_temp:
            cid_temp = cid
            try:
                card_t = cards_db[str(cid)]
                window["-cn_name-"].update(card_t["cn_name"])
                window["-en_name-"].update(card_t["en_name"])
                window["-jp_name-"].update(card_t["jp_name"])
                window["-id-"].update(card_t["id"])
                window["-types-"].update(card_t["text"]["types"])
                if card_t["text"]["pdesc"]:
                    window["-pdesc_frame-"].update(visible=True)
                    window["-pdesc-"].update(card_t["text"]["pdesc"])
                else:
                    window["-pdesc_frame-"].update(visible=False)
                window["-desc-"].update(card_t["text"]["desc"])
            except:
                pass
                # print("資料庫中未查到該卡")
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event in text_keys:
            pyperclip.copy(window[event].get())
            if web_search:
                id = window["-id-"].get()
                if event == "-cn_name-":
                    webbrowser.open(f"https://ygocdb.com/?search={id}")
                elif event == "-en_name-":
                    webbrowser.open(
                        f"https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid={cid}&request_locale=en"
                    )
                elif event == "-jp_name-":
                    webbrowser.open(
                        f"https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid={cid}&request_locale=ja"
                    )
                elif event == "-id-":
                    webbrowser.open(f"https://www.ourocg.cn/search/{id}/")
        # 恢復預設
        elif event == "恢復預設":
            window["-types_frame-"].update(visible=True)
            window["-en_name_frame-"].update(visible=True)
            window["-jp_name_frame-"].update(visible=True)
            window["-id_frame-"].update(visible=True)
            web_search = True
            window.keep_on_top_set()
            window.set_alpha(0.96)
            for key in text_keys:
                window[key].update(font=("Microsoft YaHei", 12))
            config_set("keep_on_top", "1")
            config_set("font_size", "12")
            config_set("window_alpha", "0.96")
            config_set("show_all_info", "1")
            config_set("web_search", "1")
            # config_set("x_loc", "960")
            # config_set("y_loc", "540")
            # config_set("x_len", "400")
            # config_set("y_len", "600")
        elif event == "保存視窗位置":
            win_loc = window.CurrentLocation()
            win_size = window.size
            config_set("x_loc", str(win_loc[0]))
            config_set("y_loc", str(win_loc[1]))
            config_set("x_len", str(win_size[0]))
            config_set("y_len", str(win_size[1]))
        elif event == "檢查更新":
            webbrowser.open("https://github.com/SkywalkerJi/mdt/releases/latest")
        elif event == "反和諧補丁":
            webbrowser.open(
                "https://github.com/SkywalkerJi/mdt/releases/tag/v1.0.1-UncensorPatch"
            )
        elif event == "聯繫開發者":
            webbrowser.open("https://github.com/SkywalkerJi/mdt#contact-us")
        if not settings_active and event == "設定":
            settings_active = True
            sync_ui = 0
            option_slider = [
                [
                    sg.Frame(
                        "透明度",
                        [
                            [
                                sg.Slider(
                                    key="-window_alpha-",
                                    range=[0.15, 1],
                                    default_value=0.96,
                                    resolution=0.01,
                                    orientation="horizontal",
                                    disable_number_display=False,
                                    enable_events=True,
                                    tooltip="調整透明度",
                                )
                            ]
                        ],
                        title_color="#61E7DC",
                    )
                ],
                [
                    sg.Frame(
                        "字體尺寸",
                        [
                            [
                                sg.Slider(
                                    key="-font_size-",
                                    range=(6, 25),
                                    default_value=12,
                                    resolution=1,
                                    orientation="horizontal",
                                    disable_number_display=False,
                                    enable_events=True,
                                    tooltip="調整字體尺寸",
                                )
                            ]
                        ],
                        title_color="#61E7DC",
                    )
                ],
            ]
            option_checkbox = [
                [sg.Checkbox(key="-keep_on_top-", text="置頂", enable_events=True)],
                [
                    sg.Checkbox(
                        key="-show_all_info-",
                        text="詳情顯示",
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-ui_lock-",
                        text="界面鎖定",
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-web_search-",
                        text="網頁卡查",
                        enable_events=True,
                    )
                ],
            ]

            settings_layout = [
                [sg.Column(option_slider), sg.Column(option_checkbox)],
                [sg.Button("關閉")],
            ]
            settings_win = sg.Window(
                "設定",
                settings_layout,
                font=("Microsoft YaHei", 12),
                keep_on_top=keep_on_top,
            )
        if settings_active:
            ev, vals = settings_win.read(timeout=100)
            # 設定頁面載入選項初始值
            if sync_ui == 0 or event == "恢復預設":
                config_load()
                settings_win["-keep_on_top-"].update(value=keep_on_top)
                settings_win["-window_alpha-"].update(value=window_alpha)
                settings_win["-font_size-"].update(value=font_size)
                settings_win["-ui_lock-"].update(value=ui_lock)
                settings_win["-show_all_info-"].update(value=show_all_info)
                settings_win["-web_search-"].update(value=web_search)
                set_ui_lock(settings_win, ui_lock)
                sync_ui = 1
            if ev == sg.WIN_CLOSED or ev == "關閉":
                settings_active = False
                settings_win.close()
            # 透明度滑塊
            elif ev == "-window_alpha-":
                window.set_alpha(vals["-window_alpha-"])
                config_set("window_alpha", str(vals["-window_alpha-"]))
            # 字體滑塊
            elif ev == "-font_size-":
                for key in text_keys:
                    window[key].update(
                        font=("Microsoft YaHei", int(vals["-font_size-"]))
                    )
                config_set("font_size", str(int(vals["-font_size-"])))
            # 詳情顯示
            elif ev == "-show_all_info-":
                window["-types_frame-"].update(visible=vals["-show_all_info-"])
                window["-en_name_frame-"].update(visible=vals["-show_all_info-"])
                window["-jp_name_frame-"].update(visible=vals["-show_all_info-"])
                window["-id_frame-"].update(visible=vals["-show_all_info-"])
                config_set("show_all_info", str(int(vals["-show_all_info-"])))
            # 網頁卡查
            elif ev == "-web_search-":
                web_search = vals["-web_search-"]
            # 置頂選項
            elif ev == "-keep_on_top-":
                if vals["-keep_on_top-"] == True:
                    window.keep_on_top_set()
                elif vals["-keep_on_top-"] == False:
                    window.keep_on_top_clear()
                config_set("keep_on_top", str(int(vals["-keep_on_top-"])))
            # ui鎖定
            elif ev == "-ui_lock-":
                if vals["-ui_lock-"] == True:
                    set_ui_lock(settings_win, True)
                else:
                    set_ui_lock(settings_win, False)
    service.exit()
    window.close()


if __name__ == "__main__":
    main()
