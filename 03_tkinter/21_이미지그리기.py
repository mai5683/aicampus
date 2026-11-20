

import tkinter as tk
from PIL import Image, ImageTk

# 창 생성
window = tk.Tk()
window.title("이미지 그리기")
window.geometry("500x500")

# 캔버스 배치
canvas = tk.Canvas(window, cursor="crosshair", bg="white")
canvas.pack(fill="both", expand=True)

# 캔버스에 이미지를 그린다 (Tkinter용 이미지만 가능, pillow 이용)
image_pillow = Image.open("./images/apple.png").convert("RGB")

image_thumb = image_pillow.copy() # 이미지 복사
image_thumb.thumbnail((400, 400)) # 썸네일 처리

image_tkinter = ImageTk.PhotoImage(image_thumb)  # Tkinter용으로 변환
# 라벨은 설정하는 것이지만, 캔버스는 그려야 한다.
# canvas.create_image(시작x, 시작y, image=이미지, anchor="정렬방향")
canvas.create_image(0, 0, image=image_tkinter, anchor="nw")
# 라벨과 마찬가지로 이미지 사라짐 주의
canvas.image_thumbnail = image_tkinter  # 썸네일
canvas.image_origin = image_pillow      # 원본

window.mainloop()

