import os
import sys
from ctypes import windll
from json import loads

import dhash
import win32gui
import win32ui
from PIL import Image
import cv2
import numpy as np

cid_show_gui = 0
n_flags = 3
try:
    _win_v = sys.getwindowsversion()
    if _win_v.major == 6 and _win_v.minor == 1:
        n_flags = 1
except Exception:
    pass
windll.user32.SetProcessDPIAware()
BOXES = (
    (
        (55, 159, 126, 231),
        (41, 169, 124, 253),
        (125, 192, 349, 414),
        (73, 172, 146, 245),
    ),  # 1280x720
    (
        (58, 170, 135, 246),
        (44, 181, 132, 269),
        (134, 205, 373, 442),
        (79, 183, 156, 260),
    ),  # 1366x768
    (
        (61, 179, 142, 259),
        (46, 190, 140, 284),
        (141, 216, 392, 466),
        (83, 194, 164, 275),
    ),  # 1440x810
    (
        (68, 199, 158, 288),
        (51, 212, 156, 316),
        (156, 240, 437, 518),
        (93, 215, 182, 305),
    ),  # 1600x900
    (
        (82, 239, 189, 346),
        (61, 254, 186, 379),
        (187, 288, 524, 622),
        (111, 258, 218, 366),
    ),  # 1920x1080
    (
        (87, 255, 202, 369),
        (66, 271, 199, 404),
        (200, 307, 559, 663),
        (119, 275, 233, 391),
    ),  # 2048x1152
    (
        (109, 318, 252, 461),
        (82, 339, 249, 505),
        (250, 384, 698, 829),
        (148, 344, 292, 488),
    ),  # 2560x1440
    (
        (136, 398, 316, 576),
        (102, 424, 312, 632),
        (312, 480, 874, 1036),
        (186, 430, 365, 610),
    ),  # 3200x1800
    (
        (164, 478, 378, 692),
        (122, 508, 372, 758),
        (374, 576, 1048, 1244),
        (224, 517, 438, 732),
    ),  # 3840x2160
)

last_hash = [0] * 4
art_hash = {}
with open("./data/hash.json", "r", encoding="utf-8") as f:
    art_hash = loads(f.read())


def screenshot():
    global n_flags
    if hwnd := win32gui.FindWindow(None, "masterduel"):
        box = win32gui.GetClientRect(hwnd)
        box_w = box[2] - box[0]
        box_h = box[3] - box[1]
        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        save_bitmap = win32ui.CreateBitmap()
        save_bitmap.CreateCompatibleBitmap(mfc_dc, box_w, box_h)  # 10%
        save_dc.SelectObject(save_bitmap)
        result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), n_flags)  # 58%
        bmpinfo = save_bitmap.GetInfo()
        bmpstr = save_bitmap.GetBitmapBits(True)  # 19%
        im = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )  # 12%
        win32gui.DeleteObject(save_bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwnd_dc)
        if result != 0:
            return im
    return None


def get_scan():
    global last_hash
    full_img = screenshot()
    if not full_img:
        return -1
    imgx, imgy = full_img.size
    if imgx < 1280:
        return -1
    elif imgx < 1366:
        resolution = 0
    elif imgx < 1440:
        resolution = 1
    elif imgx < 1600:
        resolution = 2
    elif imgx < 1920:
        resolution = 3
    elif imgx < 2048:
        resolution = 4
    elif imgx < 2560:
        resolution = 5
    elif imgx < 3200:
        resolution = 6
    elif imgx < 3840:
        resolution = 7
    else:
        resolution = 8

    results = []
    for i in range(4):
        _sample = full_img.crop(BOXES[resolution][i])
        _hash = dhash.dhash_int(_sample, 16)
        if dhash.get_num_bits_different(_hash, last_hash[i]) > 10:
            hash_compare = [
                (dhash.get_num_bits_different(_hash, item[0]), item[1])
                for item in art_hash
            ]
            results.append(min(hash_compare, key=lambda xx: xx[0]))
            last_hash[i] = _hash
    if results:
        result = min(results, key=lambda xx: xx[0])
        if result[0] < 60:
            return result[1]
    return 0


def get_search_button_postion():
    return position_by_template_matching("search")


def get_reset_button_postion():
    return position_by_template_matching("reset")


def get_scale():
    # 窗口分辨率可能在程序运行时改变，所以不能是静态变量
    hwnd = win32gui.FindWindow(None, "masterduel")
    box = win32gui.GetClientRect(hwnd)
    box_w = box[2] - box[0]
    scale = box_w / 1920
    return scale


def position_by_template_matching(template_name):
    # 截屏
    full_img = cv2.cvtColor(np.array(screenshot()), cv2.COLOR_RGB2BGR)
    # 高, 宽
    imgx, imgy, _ = full_img.shape
    # 按钮模板
    template_image = cv2.imread(f"./data/template/1920x1080{template_name}.png")
    template_image = cv2.resize(
        template_image,
        (
            int(get_scale() * template_image.shape[1]),
            int(get_scale() * template_image.shape[0]),
        ),
    )
    # 模板匹配
    result = cv2.matchTemplate(full_img, template_image, cv2.TM_CCOEFF_NORMED)
    # 先横后竖
    _, _, _, top_left = cv2.minMaxLoc(result)
    return int(top_left[0] + template_image.shape[1] / 2), int(
        top_left[1] + template_image.shape[0] / 2
    )


def main():
    print(get_scan())
    os.system("pause")


if __name__ == "__main__":
    main()
