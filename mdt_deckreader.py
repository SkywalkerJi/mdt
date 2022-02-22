import pymem
import json


def pointer_to_address(process, base, offsets):
    offset_final = offsets.pop()
    address_next = process.read_longlong(base)
    for offset in offsets:
        address_next = process.read_longlong(address_next + offset)
    address_final = address_next + offset_final
    return address_final


def read_memory_int(process, address):
    value = process.read_int(address)
    return value


def read_memory_bytes(process, address, count):
    inc = 0x18
    value = process.read_bytes(address, count * inc)
    return value


def deck_bytes_to_list(bytes: bytes, count: int):
    inc = 0x18
    card_list = []
    for i in range(count):
        card_list.append(int.from_bytes(bytes[i * inc:i * inc + 2], byteorder="little"))
    return card_list


def get_process(process_name):
    process = pymem.Pymem(process_name)
    return process


def get_base_address(process, module):
    base_addr = pymem.process.module_from_name(
        process.process_handle, module
    ).lpBaseOfDll
    return base_addr


def get_database(path):
    with open(path, "rb") as f:
        cards_db = json.load(f)
    return cards_db


def get_deck_string():
    main_name = "masterduel.exe"
    module_name = "GameAssembly.dll"
    db_name = "./locales/zh-CN/cards.json"
    ma_count_static = 0x01CCE3C0
    ma_count_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x90, 0x18]
    ex_count_static = 0x01CCE3C0
    ex_count_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x98, 0x18]
    ma_cards_static = 0x01CCE3C0
    ma_cards_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x90, 0x10, 0x20]
    ex_cards_static = 0x01CCE3C0
    ex_cards_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x98, 0x10, 0x20]
    deck_string = ""
    try:
        pm = get_process(main_name)
        base_address = get_base_address(pm, module_name)
        cards_db = get_database(db_name)
        ma_count_addr = base_address + ma_count_static
        ex_count_addr = base_address + ex_count_static
        ma_cards_addr = base_address + ma_cards_static
        ex_cards_addr = base_address + ex_cards_static
        ma_count = read_memory_int(pm, pointer_to_address(pm, ma_count_addr, ma_count_offsets))
        ex_count = read_memory_int(pm, pointer_to_address(pm, ex_count_addr, ex_count_offsets))
        ma_cid_list = deck_bytes_to_list(
            read_memory_bytes(pm, pointer_to_address(pm, ma_cards_addr, ma_cards_offsets), ma_count), ma_count
        )
        ex_cid_list = deck_bytes_to_list(
            read_memory_bytes(pm, pointer_to_address(pm, ex_cards_addr, ex_cards_offsets), ex_count), ex_count
        )
    except Exception as e:
        print(e)
        deck_string += "无法读取卡组信息"
        return deck_string

    deck_string += f"----------------主卡组: {ma_count}----------------\n"
    c = 0
    for cid in ma_cid_list:
        c += 1
        card_string = ""
        try:
            card_info = cards_db[str(cid)]
        except:
            card_string += "查无此卡"

        try:
            card_string += f"{card_info['cn_name']}    "
            card_string += f"{card_info['jp_name']}    "
            card_string += f"{card_info['en_name']}"
        except:
            card_string += "    该卡信息有缺失"
        deck_string += f"{c:<2} {card_string}\n"

    deck_string += f"----------------额外卡组: {ex_count}----------------\n"
    c = 0
    for cid in ex_cid_list:
        c += 1
        card_string = ""
        try:
            card_info = cards_db[str(cid)]
        except:
            card_string += "查无此卡"

        try:
            card_string += f"{card_info['cn_name']}    "
            card_string += f"{card_info['jp_name']}    "
            card_string += f"{card_info['en_name']}"
        except:
            card_string += "    该卡信息有缺失"
        deck_string += f"{c:<2} {card_string}\n"

    return deck_string


print(get_deck_string())
