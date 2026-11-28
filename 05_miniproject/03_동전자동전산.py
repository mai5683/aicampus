
import cv2
import pandas as pd
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import coin_core as cc


# ------------------------------------------------
# 이미지 관리 변수
# ------------------------------------------------
image_file_path = None  # 이미지 파일 경로
folder_path = None      # 선택한 폴더 경로
file_list = []          # 폴더 내 이미지 파일 목록
file_index = 0          # 현재 이미지의 인덱스

image_original = None   # 원본 이미지
image_result = None     # 판정 결과 이미지
image_tk = None         # Canvas 표시용 이미지

coin_list = []          # 검출된 동전 상세 정보


# ------------------------------------------------
# 일반 함수
# ------------------------------------------------
def show_image(image):
    global image_tk

    # OpenCV 이미지를 RGB로 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Pillow 이미지로 변환
    image_pillow = Image.fromarray(image_rgb)
    # Canvas의 가로, 세로 크기 확인
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    # 이미지 비율을 유지하면서 크기 조절
    image_pillow.thumbnail((w, h))
    # Tkinter 이미지로 변환
    image_tk = ImageTk.PhotoImage(image_pillow)
    # 기존 Canvas 내용 삭제
    canvas.delete("all")
    # Canvas 중앙에 이미지 표시
    canvas.create_image(w // 2, h // 2, image=image_tk)


# ------------------------------------------------
# 콜백 함수
# ------------------------------------------------
def open_image(event=None):
    global image_file_path, image_original
    global image_result, coin_list

    file_path = filedialog.askopenfilename(
        parent=window,
        title="이미지 선택",
        filetypes=[
            ("이미지 파일", "*.jpg"),
            ("모든 파일", "*.*")
        ]
    )

    if file_path == "":
        return

    image = cv2.imread(file_path)

    if image is None:
        messagebox.showerror("오류", "이미지를 읽을 수 없습니다.")
        return

    image_file_path = Path(file_path)
    image_original = image
    image_result = None
    coin_list = []

    show_image(image_original)

def open_folder(event=None):
    global folder_path, file_list, file_index
    global image_file_path, image_original, image_result, coin_list

    path = filedialog.askdirectory(parent=window, title="폴더 선택")

    if path == "":
        return

    folder_path = Path(path)
    file_list = cc.load_files(folder_path)

    if len(file_list) == 0:
        messagebox.showwarning("경고", "폴더에 이미지가 없습니다.")
        return

    file_index = 0
    file_path = file_list[file_index]  # 이미지 경로 가져오기
    file_path = str(file_path)  # 문자열로 변환하기
    image = cv2.imread(file_path)  # 이미지 불러오기

    if image is None:
        messagebox.showerror("오류", "이미지를 읽을 수 없습니다.")
        return

    image_file_path = Path(file_path)
    image_original = image
    image_result = None
    coin_list = []

    show_image(image_original)


def save_result(event=None):
    pass

def close_window(event=None):
    window.destroy()

def inspect_image(event=None):
    pass

def inspect_all_images(event=None):
    pass

def show_statistics(event=None):
    pass

def save_report(event=None):
    pass


# ------------------------------------------------
# 폰트 설정
# ------------------------------------------------
font_title = ("Malgun Gothic", 16, "bold")
font_main = ("Malgun Gothic", 12)
font_menu = ("Malgun Gothic", 10)


# ------------------------------------------------
# 화면 배치
# ------------------------------------------------
window = tk.Tk()
window.title("무인 동전 정산 시스템")
window.geometry("1000x700")


# ------------------------------------------------
# 이미지 표시 영역 생성
# ------------------------------------------------
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill="both", expand=True)


# ------------------------------------------------
# 메뉴바 생성
# ------------------------------------------------
menubar = tk.Menu(window, font=font_menu)

menu_file = tk.Menu(menubar, tearoff=False, font=font_menu)
menu_inspect = tk.Menu(menubar, tearoff=False, font=font_menu)
menu_analyze = tk.Menu(menubar, tearoff=False, font=font_menu)

menubar.add_cascade(label="파일", menu=menu_file)
menubar.add_cascade(label="검사", menu=menu_inspect)
menubar.add_cascade(label="분석", menu=menu_analyze)

window.config(menu=menubar)


#------------------------------------------------
# 하위 메뉴 설정
#------------------------------------------------
menu_file.add_command(label="이미지 열기", command=open_image, accelerator="Ctrl+O")
menu_file.add_command(label="폴더 열기", command=open_folder, accelerator="Ctrl+Shift+O")
menu_file.add_command(label="결과 저장", command=save_result, accelerator="Ctrl+S")
menu_file.add_separator()
menu_file.add_command(label="종료", command=close_window, accelerator="Ctrl+Q")

menu_inspect.add_command(label="현재 이미지 판정", command=inspect_image, accelerator="F5")
menu_inspect.add_command(label="전체 이미지 일괄 정산", command=inspect_all_images, accelerator="F6")

menu_analyze.add_command(label="정산 통계 조회", command=show_statistics, accelerator="F7")
menu_analyze.add_command(label="보고서 저장", command=save_report, accelerator="F8")


# ------------------------------------------------
# 단축키 설정
# ------------------------------------------------
window.bind("<Control-o>", open_image)
window.bind("<Control-Shift-O>", open_folder)
window.bind("<Control-s>", save_result)
window.bind("<Control-q>", close_window)

window.bind("<F5>", inspect_image)
window.bind("<F6>", inspect_all_images)

window.bind("<F7>", show_statistics)
window.bind("<F8>", save_report)


window.mainloop()