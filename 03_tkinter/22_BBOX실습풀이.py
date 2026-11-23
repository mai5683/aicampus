"""
목표 : 이미지를 불러와서 원하는 대상을 마우스로 마킹하고 위치와 크기를 txt로 저장
"""

import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageOps, ImageTk

# 콜백 함수
def open_file(event=None):
    # try:
        file_path = filedialog.askopenfilename(
            parent=window,
            title="불러올 이미지 선택",
            filetypes=[
                ("이미지 파일", "*.jpg *.jpeg *.png"),
                ("모든 파일", "*.*")
            ]
        )
        if file_path == "":  # 미 선택시 중지
            return

        # 이미지 읽기(pillow)
        with Image.open(file_path) as file:
            image_pillow = file.convert("RGB")

        # 이미지 변환 및 표시 (캔버스에 맞는 크기로 표시)
        canvas_width = canvas.winfo_width()  # 캔버스 폭
        canvas_height = canvas.winfo_height()  # 캔버스 높이
        image_thumb = ImageOps.contain(image_pillow, (canvas_width, canvas_height))

        image_tkinter = ImageTk.PhotoImage(image_thumb)
        #이미지를 가운데 배치
        canvas.create_image(
            canvas_width // 2, canvas_height // 2,
            image=image_tkinter, anchor="center", tags="img"
        )
        canvas.image_thumbnail = image_tkinter  # 이미지 참조 유지를 위해
        canvas.image_origin = image_pillow # 크기 변경 시 사용
    # except Exception:
    #     messagebox.showerror("오류", "파일을 열 수 없습니다", parent=window)

# 이미지 크기를 캔버스에 맞게 재조정하는 작업
def resize_image(event):
    # 이미지를 캔버스 크기에 맞게 배치
    image_pillow = canvas.image_origin
    if image_pillow is None:
        return
    image_thumb = ImageOps.contain(image_pillow, (event.width, event.height))
    image_tkinter = ImageTk.PhotoImage(image_thumb)
    canvas.itemconfig("img", image=image_tkinter)   # 이미지 속성 변경
    canvas.image_thumbnail = image_tkinter
    canvas.image_origin = image_pillow

    # 이미지를 중앙에 배치
    x = event.width // 2 # 중심x 계산
    y = event.height // 2 # 중심y 계산
    canvas.coords("img", x, y) # 캔버스 좌표변경

def save_file(event=None):
    pass

def clear_work(event=None):
    pass

def undo_work(event=None):
    pass

# 창 배치
window = tk.Tk()
window.title("BBOX 실습")
window.geometry("500x500")

# 메뉴 배치
menubar = tk.Menu(window, tearoff=False)
window.config(menu=menubar)

menu_file = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="파일", menu=menu_file)

menu_edit = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="편집", menu=menu_edit)

menu_file.add_command(label="파일 열기", accelerator="Ctrl+O", command=open_file)
menu_file.add_command(label="파일 저장", accelerator="Ctrl+S", command=save_file)

menu_edit.add_command(label="모두 지우기", accelerator="Ctrl+R", command=clear_work)
menu_edit.add_command(label="마지막 지우기", accelerator="Ctrl+Z", command=undo_work)

# 메뉴 이벤트 연결(바인딩)
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-r>", clear_work)
window.bind("<Control-z>", undo_work)

# 캔버스 배치
canvas = tk.Canvas(window, cursor="crosshair", bg="white")
canvas.pack(fill="both", expand=True)
canvas.image_thumbnail = None
canvas.image_origin = None

# 캔버스 이벤트
canvas.bind("<Configure>", resize_image)

# 창 구동
window.mainloop()