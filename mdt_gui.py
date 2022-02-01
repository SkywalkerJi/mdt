import ctypes, sys
import PySimpleGUI as sg
import mdt_service as service
import pyperclip
import configparser
import webbrowser
import i18n
import os
import time

config_file = "config.ini"
font_size = 12
window_alpha = 0.96
keep_on_top = True
ui_lock = False
cfg = configparser.ConfigParser()
sync_ui = 0
show_names = True
show_types = True
borderless = True
web_search = True
x_loc = 960
y_loc = 540
x_len = 400
y_len = 600
_ = i18n.t
locale = "zh-CN"


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


def restart():
    os.execv(sys.executable, ["python"] + sys.argv)


def set_ui_lock(window, bool):
    window["-keep_on_top-"].update(disabled=bool)
    window["-window_alpha-"].update(disabled=bool)
    window["-font_size-"].update(disabled=bool)
    window["-show_names-"].update(disabled=bool)
    window["-show_types-"].update(disabled=bool)
    window["-borderless-"].update(disabled=bool)
    window["-web_search-"].update(disabled=bool)
    config_set("ui_lock", str(int(bool)))


def config_load():
    global font_size
    global window_alpha
    global keep_on_top
    global borderless
    global ui_lock
    global show_names
    global show_types
    global web_search
    global x_loc
    global y_loc
    global x_len
    global y_len
    global cfg
    global locale
    try:
        cfg.read(config_file, encoding="utf-8")
        config = cfg.items("gui")
        config = dict(config)
        font_size = int(config["font_size"])
        window_alpha = float(config["window_alpha"])
        keep_on_top = bool(int(config["keep_on_top"]))
        ui_lock = bool(int(config["ui_lock"]))
        borderless = bool(int(config["borderless"]))
        show_names = bool(int(config["show_names"]))
        show_types = bool(int(config["show_types"]))
        web_search = bool(int(config["web_search"]))
        x_loc = int(config["x_loc"])
        y_loc = int(config["y_loc"])
        x_len = int(config["x_len"])
        y_len = int(config["y_len"])
        locale = config["locale"]
    except:
        pass
        # print(f"未找到{config_file}配置文件或配置文件格式有误。")


def config_set(option: str, value: str):
    cfg.set("gui", option, value)
    with open(config_file, "w+") as f:
        cfg.write(f)


def i18n_set(locale: str):
    i18n.set("locale", locale)


def main():
    global sync_ui
    global web_search
    global locale
    settings_active = False
    uac_reload()
    service.start()
    config_load()
    i18n.set("filename_format", "{locale}.{format}")
    i18n.set("available_locales", ["zh-CN", "zh-TW"])
    i18n.set("file_format", "json")
    i18n.set("locale", locale)
    i18n.load_path.append("./locales")
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
    sg.theme("Dark")
    card_frame = [
        [
            sg.Frame(
                _("卡名"),
                [
                    [
                        sg.T(
                            text=_("等待检测"),
                            key="-cn_name-",
                            enable_events=True,
                            expand_x=True,
                        )
                    ],
                ],
                title_color="#61E7DC",
                expand_x=True,
                tooltip=_("右键选择更多功能"),
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    _("灵摆"),
                    [
                        [
                            sg.Multiline(
                                key="-pdesc-",
                                s=(None, 5),
                                background_color="#3F3F3F",
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
                    tooltip=_("右键选择更多功能"),
                ),
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                _("描述"),
                [
                    [
                        sg.Multiline(
                            key="-desc-",
                            background_color="#3F3F3F",
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
                tooltip=_("右键选择更多功能"),
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    _("类型"),
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
                    visible=show_types,
                    key="-types_frame-",
                    tooltip=_("右键选择更多功能"),
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    _("英文名"),
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
                    visible=show_names,
                    key="-en_name_frame-",
                    tooltip=_("右键选择更多功能"),
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    _("日文名"),
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
                    visible=show_names,
                    key="-jp_name_frame-",
                    tooltip=_("右键选择更多功能"),
                ),
                expand_x=True,
            )
        ],
        [
            sg.pin(
                sg.Frame(
                    _("卡密"),
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
                    visible=show_names,
                    key="-id_frame-",
                    tooltip=_("右键选择更多功能"),
                ),
                expand_x=True,
            )
        ],
    ]
    right_click_menu = [
        "&Right",
        [
            _("设置"),
            _("保存窗口位置"),
            _("恢复默认"),
            _("切换语言"),
            _("重启检测"),
            _("检查更新"),
            _("反和谐补丁"),
            _("联系开发者"),
            _("关闭"),
        ],
    ]
    layout = [[card_frame]]
    window = sg.Window(
        "MDT v0.2.5 @SkywalkerJi GPLv3",
        layout,
        default_element_size=(12, 1),
        font=("Microsoft YaHei", font_size),
        right_click_menu_font=("Microsoft YaHei", font_size),
        keep_on_top=keep_on_top,
        resizable=True,
        alpha_channel=window_alpha,
        right_click_menu=right_click_menu,
        location=(x_loc, y_loc),
        size=(x_len, y_len),
        no_titlebar=borderless,
        grab_anywhere=True,
        debugger_enabled=False,
    )
    # 判断屏幕尺寸
    screen = window.get_screen_dimensions()
    if screen[0] < x_loc or screen[1] < y_loc:
        config_set("x_loc", str(screen[0] / 2))
        config_set("y_len", str(screen[1] / 2))
        uac_reload(True)

    while True:
        event, values = window.read(timeout=100)
        cid = service.get_cid()
        # print(event, values)
        # 载入db

        if not cards_db:
            cards_db = service.get_cards_db(locale)
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
                # print("数据库中未查到该卡")
        if event in (sg.WIN_CLOSED, "Exit", _("关闭")):
            break
        elif event in text_keys:
            pyperclip.copy(window[event].get())
            if web_search:
                id = window["-id-"].get()
                if id:
                    if event == "-cn_name-":
                        webbrowser.open(f"https://ygocdb.com/?search={id}")
                    elif event == "-id-":
                        webbrowser.open(f"https://www.ourocg.cn/search/{id}/")
                if cid:
                    if event == "-en_name-":
                        webbrowser.open(
                            f"https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid={cid}&request_locale=en"
                        )
                    elif event == "-jp_name-":
                        webbrowser.open(
                            f"https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid={cid}&request_locale=ja"
                        )
        # 切换语言
        elif event == _("切换语言"):
            if locale == "zh-CN":
                locale = "zh-TW"
            elif locale == "zh-TW":
                locale = "zh-CN"
            i18n.set("locale", locale)
            config_set("locale", locale)
            restart()
        # 重启
        elif event == _("重启检测"):
            restart()
        # 恢复默认
        elif event == _("恢复默认"):
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
            config_set("show_names", "1")
            config_set("show_types", "1")
            config_set("web_search", "1")
            # 只恢复窗口UI，不恢复窗口属性
            # config_set("x_loc", "960")
            # config_set("y_loc", "540")
            # config_set("x_len", "400")
            # config_set("y_len", "600")
            # config_set("borderless", "0")
        elif event == _("保存窗口位置"):
            win_loc = window.CurrentLocation()
            win_size = window.size
            config_set("x_loc", str(win_loc[0]))
            config_set("y_loc", str(win_loc[1]))
            config_set("x_len", str(win_size[0]))
            config_set("y_len", str(win_size[1]))
        elif event == _("检查更新"):
            webbrowser.open("https://github.com/SkywalkerJi/mdt/releases/latest")
        elif event == _("反和谐补丁"):
            webbrowser.open(
                "https://github.com/SkywalkerJi/mdt/releases/tag/v1.0.1-UncensorPatch"
            )
        elif event == _("联系开发者"):
            webbrowser.open("https://github.com/SkywalkerJi/mdt#contact-us")
        if not settings_active and event == _("设置"):
            settings_active = True
            sync_ui = 0
            option_slider = [
                [
                    sg.Frame(
                        _("透明度"),
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
                                    tooltip=_("调整透明度"),
                                )
                            ]
                        ],
                        title_color="#61E7DC",
                    )
                ],
                [
                    sg.Frame(
                        _("字体尺寸"),
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
                                    tooltip=_("调整字体尺寸"),
                                )
                            ]
                        ],
                        title_color="#61E7DC",
                    )
                ],
            ]
            option_checkbox = [
                [sg.Checkbox(key="-keep_on_top-", text=_("置顶"), enable_events=True)],
                [
                    sg.Checkbox(
                        key="-show_types-",
                        text=_("卡片类型"),
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-show_names-",
                        text=_("原始卡名"),
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-borderless-",
                        text=_("无边框"),
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-ui_lock-",
                        text=_("界面锁定"),
                        enable_events=True,
                    )
                ],
                [
                    sg.Checkbox(
                        key="-web_search-",
                        text=_("网页卡查"),
                        enable_events=True,
                    )
                ],
            ]

            settings_layout = [
                [sg.Column(option_slider), sg.Column(option_checkbox)],
                [
                    sg.Column(
                        [
                            [
                                sg.Button(
                                    _("关闭"),
                                    button_color=("white", "#238636"),
                                    border_width=1,
                                )
                            ]
                        ]
                    ),
                    sg.Column(
                        [
                            [
                                sg.Button(
                                    _("保存卡组"),
                                    button_color=("white", "#238636"),
                                    border_width=1,
                                )
                            ]
                        ]
                    ),
                ],
            ]
            settings_win = sg.Window(
                _("功能 & 设置"),
                settings_layout,
                font=("Microsoft YaHei", 12),
                keep_on_top=keep_on_top,
                debugger_enabled=False,
            )
        if settings_active:
            ev, vals = settings_win.read(timeout=100)
            # 设置页面载入选项初始值
            if sync_ui == 0 or event == _("恢复默认"):
                config_load()
                settings_win["-keep_on_top-"].update(value=keep_on_top)
                settings_win["-window_alpha-"].update(value=window_alpha)
                settings_win["-font_size-"].update(value=font_size)
                settings_win["-ui_lock-"].update(value=ui_lock)
                settings_win["-borderless-"].update(value=borderless)
                settings_win["-show_names-"].update(value=show_names)
                settings_win["-show_types-"].update(value=show_types)
                settings_win["-web_search-"].update(value=web_search)
                set_ui_lock(settings_win, ui_lock)
                sync_ui = 1
            if ev == sg.WIN_CLOSED or ev == _("关闭"):
                settings_active = False
                settings_win.close()
            # 透明度滑块
            elif ev == "-window_alpha-":
                window.set_alpha(vals["-window_alpha-"])
                config_set("window_alpha", str(vals["-window_alpha-"]))
            # 字体滑块
            elif ev == "-font_size-":
                for key in text_keys:
                    window[key].update(
                        font=("Microsoft YaHei", int(vals["-font_size-"]))
                    )
                config_set("font_size", str(int(vals["-font_size-"])))
            # 显示额外卡名
            elif ev == "-show_names-":
                window["-en_name_frame-"].update(visible=vals["-show_names-"])
                window["-jp_name_frame-"].update(visible=vals["-show_names-"])
                window["-id_frame-"].update(visible=vals["-show_names-"])
                config_set("show_names", str(int(vals["-show_names-"])))
            # 显示类型
            elif ev == "-show_types-":
                window["-types_frame-"].update(visible=vals["-show_types-"])
                config_set("show_types", str(int(vals["-show_types-"])))
            # 无边框
            elif ev == "-borderless-":
                config_set("borderless", str(int(vals["-borderless-"])))
                restart()
            # 网页卡查
            elif ev == "-web_search-":
                web_search = vals["-web_search-"]
            # 置顶选项
            elif ev == "-keep_on_top-":
                if vals["-keep_on_top-"] == True:
                    window.keep_on_top_set()
                elif vals["-keep_on_top-"] == False:
                    window.keep_on_top_clear()
                config_set("keep_on_top", str(int(vals["-keep_on_top-"])))
            # ui锁定
            elif ev == "-ui_lock-":
                if vals["-ui_lock-"] == True:
                    set_ui_lock(settings_win, True)
                else:
                    set_ui_lock(settings_win, False)
            elif ev == _("保存卡组"):
                now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
                deck = service.get_deck_dict()
                deck_string = service.get_deck_string(locale)
                ydk = "#created by MDT https://github.com/SkywalkerJi/mdt \n#main\n"
                for cid in deck["ma_cid_list"]:
                    ydk += f"{cards_db[str(cid)]['id']}\n"
                ydk += "#extra\n"
                for cid in deck["ex_cid_list"]:
                    ydk += f"{cards_db[str(cid)]['id']}\n"
                with open(_("ygopro卡组") + now + ".ydk", "w", encoding="utf8") as f:
                    f.write(ydk)
                    f.close()
                with open(_("卡组文本") + now + ".txt", "w", encoding="utf8") as f:
                    f.write("#created by MDT https://github.com/SkywalkerJi/mdt \n"+deck_string)
                    f.close()
    service.exit()
    window.close()


if __name__ == "__main__":
    main()
