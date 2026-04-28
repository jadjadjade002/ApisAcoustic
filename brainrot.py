import time
from PIL import ImageGrab
import numpy as np
import ctypes

TARGET_COLORS = [
    (188, 42, 234),   # #bc2aea
    # (255, 143, 13),   # #ff8f0d
    # (68, 229, 57)
]
TOLERANCE    = 10
SCAN_INTERVAL = 1

def find_target_pixel():
    screenshot = ImageGrab.grab()
    img = np.array(screenshot)
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    combined_mask = np.zeros(r.shape, dtype=bool)
    for tr, tg, tb in TARGET_COLORS:
        mask = (
            (abs(r.astype(int) - tr) <= TOLERANCE) &
            (abs(g.astype(int) - tg) <= TOLERANCE) &
            (abs(b.astype(int) - tb) <= TOLERANCE)
        )
        combined_mask |= mask

    ys, xs = np.where(combined_mask)
    if len(xs) == 0:
        return None
    return int(xs.mean()), int(ys.mean())

def click_roblox(x, y):
    hwnd_roblox = ctypes.windll.user32.FindWindowW(None, "Roblox")
    hwnd_terminal = ctypes.windll.user32.FindWindowW(None, "Windows PowerShell")

    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)

    if hwnd_terminal:
        ctypes.windll.user32.SetForegroundWindow(hwnd_terminal)
        time.sleep(0.1)

    if hwnd_roblox:
        ctypes.windll.user32.SetForegroundWindow(hwnd_roblox)
        time.sleep(0.1)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        time.sleep(0.05)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

print("สแกนหาสีม่วงและสีส้ม — Ctrl+C เพื่อหยุด")

while True:
    pos = find_target_pixel()
    if pos:
        x, y = pos
        print(f"  พบสีที่ ({x}, {y}) — คลิก")
        click_roblox(x, y)
    time.sleep(SCAN_INTERVAL)