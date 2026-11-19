
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

#------------------------------------------------
# 콜백 함수
#------------------------------------------------
def open_image(event=None):
    try:
        file_path = filedialog.askopenfilename(
            parent=window,
            title="이미지 선택",
            filetypes=[
                ("이미지 파일", "*.png *.jpg *.gif"),
                ("모든 파일", "*.*")]
        )
        if file_path == "":
            return
        with Image.open(file_path) as file:
            image_pillow = file.convert("RGB")
        image_thumb = image_pillow.copy()
        w = label_preview.winfo_width()
        h = label_preview.winfo_height()
        image_thumb.thumbnail((w, h))
        image_tkinter = ImageTk.PhotoImage(image_thumb)
        label_preview.config(image=image_tkinter)
        label_preview.thumb = image_tkinter
        label_preview.image = image_pillow

        label_path.config(text=f"현재 이미지 : {str(file_path)}")

    except Exception:
        messagebox.showerror(
            "이미지 열기 오류",
            "읽을 수 없는 이미지입니다.\n올바른 형식의 파일을 선택하세요.",
            parent=window
        )
        reset_image()

    label_preview.origin = image_pillow.copy()

def save_image(event=None):
    print("이미지 저장")

def reset_image(event=None):
    label_path.config(text="현재 이미지 : 없음")
    label_preview.config(image=None)
    label_preview.image = None
    label_preview.thumb = None

def close_window(event=None):
    window.destroy()

def resize_thumbnail(event):
    if label_preview.image is None:
        return

    image_thumb = label_preview.image.copy()
    w = label_preview.winfo_width()
    h = label_preview.winfo_height()
    image_thumb.thumbnail((w, h))
    image_tkinter = ImageTk.PhotoImage(image_thumb)
    label_preview.config(image=image_tkinter)
    label_preview.thumb = image_tkinter
#------------------------------------------------
def convert_gray(event=None):
    print("흑백 변환")
def convert_otsu(event=None):
    print("이진화(OTSU)")
def apply_blur(event=None):
    print("블러")
def apply_morphology(event=None):
    print("모폴로지")
def apply_canny(event=None):
    print("캐니")
def undo(event=None):
    print("되돌리기")

#------------------------------------------------
# 창 생성
#------------------------------------------------
window = tk.Tk()
window.title("이미지 편집기 v0.1")
window.geometry("900x500")

#------------------------------------------------
# 메뉴 생성
#------------------------------------------------
font_menu = ("Binggrae", 12)

menubar = tk.Menu(window, font=font_menu)

menu_file = tk.Menu(menubar, tearoff=False, font=font_menu)
menu_edit = tk.Menu(menubar, tearoff=False, font=font_menu)

#------------------------------------------------
# 메뉴바 설정
#------------------------------------------------
menubar.add_cascade(label="파일", menu=menu_file)
menubar.add_cascade(label="편집", menu=menu_edit)
window.config(menu=menubar)

#------------------------------------------------
# 하위 메뉴 설정
#------------------------------------------------
menu_file.add_command(label="이미지 열기", command=open_image, accelerator="Ctrl+O")
menu_file.add_separator()
menu_file.add_command(label="이미지 저장", command=save_image, accelerator="Ctrl+S")
menu_file.add_command(label="이미지 초기화", command=reset_image, accelerator="Ctrl+R")
menu_file.add_separator()
menu_file.add_command(label="프로그램 종료", command=close_window, accelerator="Alt+F4")

menu_edit.add_command(label="흑백 변환", command=convert_gray, accelerator="F1")
menu_edit.add_command(label="이진화(OTSU)", command=convert_otsu, accelerator="F2")
menu_edit.add_separator()
menu_edit.add_command(label="블러", command=apply_blur, accelerator="F3")
menu_edit.add_command(label="모폴로지", command=apply_morphology, accelerator="F4")
menu_edit.add_command(label="캐니", command=apply_canny, accelerator="F5")
menu_edit.add_separator()
menu_edit.add_command(label="되돌리기", command=undo, accelerator="F6")

#------------------------------------------------
# 함수 연결
#------------------------------------------------
window.bind("<Control-o>", open_image)
window.bind("<Control-s>", save_image)
window.bind("<Control-r>", reset_image)
window.protocol("WM_DELETE_WINDOW", close_window)

window.bind("<F1>", convert_gray)
window.bind("<F2>", convert_otsu)
window.bind("<F3>", apply_blur)
window.bind("<F4>", apply_morphology)
window.bind("<F5>", apply_canny)
window.bind("<F6>", undo)

#------------------------------------------------
# 이미지 파일 경로 표시
#------------------------------------------------
label_path = tk.Label(
    window, text="현재 이미지 : 없음",
    font=font_menu,
    anchor="w"
)
label_path.pack(padx=10, pady=5, fill="x")

#------------------------------------------------
# 이미지 표시
#------------------------------------------------
label_preview = tk.Label(window, bg="white")
label_preview.pack(padx=20, pady=10,fill="both", expand=True)
label_preview.bind("<Configure>", resize_thumbnail)

#------------------------------------------------
window.mainloop()
