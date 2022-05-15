from threading import Thread

import pyperclip
import mdt as mdt
import mdt_control
import mdt_deck_reader as reader


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


def ydk_converter(
    ydk_deck: str, window, game_client_locale: str = "en", locale: str = "zh-CN"
):
    tmp = reader.ydk_converter(ydk_deck, game_client_locale)
    if tmp is None:
        window.write_event_value("CARD_NOT_FOUND_ERROR", None)
    tmp.sort(key=lambda tup: tup[0])

    def ydk_converter_callback():
        print(ydk_deck)
        pyperclip.copy(ydk_deck)
        start()

    pause()
    # TODO: 防止二次生成
    thread = Thread(target=mdt_control.ydk_converter, args=(tmp, locale, window, ydk_converter_callback))
    thread.start()


if __name__ == "__main__":
    ydk_converter("", "")
