import mdt as mdt
import mdt_deck_reader as reader
from threading import Thread


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


def get_deck_dict():
    return reader.get_deck_dict()


def get_deck_string(locale: str):
    return reader.get_deck_string(locale)
