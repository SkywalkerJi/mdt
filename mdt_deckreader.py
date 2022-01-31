import pymem
import json


ma_count_static = 0x01CCD278
ma_count_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x90, 0x18]
ex_count_static = 0x01CCD278
ex_count_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x98, 0x18]
ma_cards_static = 0x01CCD278
ma_cards_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x90, 0x10, 0x20]
ex_cards_static = 0x01CCD278
ex_cards_offsets = [0xB8, 0x00, 0xF8, 0x1C0, 0x98, 0x10, 0x20]

pm = pymem.Pymem("masterduel.exe")
base_address = pymem.process.module_from_name(
    pm.process_handle, "GameAssembly.dll"
).lpBaseOfDll


def read_memory_int(process, base, offsets):
    offset_final = offsets.pop()
    address_next = process.read_longlong(base)
    for offset in offsets:
        address_next = process.read_longlong(address_next + offset)
    value = process.read_int(address_next + offset_final)
    return value


def read_memory_bytes(process, base, offsets, count):
    inc = 0x18
    offset_final = offsets.pop()
    address_next = process.read_longlong(base)
    for offset in offsets:
        address_next = process.read_longlong(address_next + offset)
    value = process.read_bytes(address_next + offset_final, count * inc)
    return value


def deck_bytes_to_list(bytes: bytes, count: int):
    inc = 0x18
    card_list = []
    for i in range(count):
        card_list.append(int.from_bytes(bytes[i * inc:i * inc + 2], byteorder="little"))
    return card_list


with open("cards.json", "rb") as f:
    cards_db = json.load(f)


ma_count_addr = base_address + ma_count_static
ex_count_addr = base_address + ex_count_static
ma_cards_addr = base_address + ma_cards_static
ex_cards_addr = base_address + ex_cards_static
ma_count = read_memory_int(pm, ma_count_addr, ma_count_offsets)
ex_count = read_memory_int(pm, ex_count_addr, ex_count_offsets)
print(f"Main Deck Count: {ma_count} Extra Deck Count: {ex_count}")
ma_cid_list = deck_bytes_to_list(read_memory_bytes(pm, ma_cards_addr, ma_cards_offsets, ma_count),ma_count)
print(ma_cid_list)
for cid in ma_cid_list:
    print(cards_db[str(cid)]['jp_name'])

ex_cid_list = deck_bytes_to_list(read_memory_bytes(pm, ex_cards_addr, ex_cards_offsets, ex_count),ex_count)
print(ex_cid_list)
for cid in ex_cid_list:
    print(cards_db[str(cid)]['jp_name'])

