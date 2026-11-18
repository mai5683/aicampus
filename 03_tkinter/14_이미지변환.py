"""
opencv와 pillow의 이미지 상호 변환
- opencv : NumPy의 ndarray 형태로 이미지 사용, 컬러 이미지는 BGR 채널
- pillow : PIL.Image 형태로 이미지 사용, 컬러 이미지는 RGB 채널
"""

import cv2
from PIL import Image, ImageTk
import tkinter as tk

# opencv --> pillow
image_cv = cv2.imread("./images/cat.jpg")
if image_cv is None:
    print("이미지가 없습니다")
    exit(1)

# 현재 상태는 BGR이므로 RGB로 교체한다.
# image_change = image_cv[:, :, ::-1].copy()
image_change = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

# Pillow 이미지로 변환
image_pil = Image.fromarray(image_change)

# 썸네일, 리사이즈, ... 할 거 하고 GUI(Label, Button)에 표시
# print(type(image_pil))

window = tk.Tk()
window.title("opencv 이미지를 pillow로 변환")
window.geometry("500x500")

# pillow --> tkinter 이미지
image_preview = image_pil.copy()
image_preview.thumbnail((400, 400))
photo = ImageTk.PhotoImage(image_preview)

label_viewer = tk.Label(window, image=photo)
label_viewer.pack(fill="both", expand=True)

window.mainloop()
