import mdt as mdt
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


def get_cards_db():
    if mdt.cards_db:
        return mdt.cards_db
    else:
        return None
