"""
# 이미지를 편집할 수 있는 프로그램을 개발하세요

# 메뉴의 형태

파일
+- 이미지 열기 (Ctrl+O)
+- 최근 열어본 이미지 +- 이미지1
|                  +- 이미지2
+- 이미지 저장 (Ctrl+S)
+- 이미지 초기화 (Ctrl+R)
+- 프로그램 종료 (Alt+F4)

편집
+- 흑백 변환 (F1)
+- 이진화 (F2)
+- 블러 (F3)
+- 모폴로지 (F4)
+- 캐니 (F5)
+- 되돌리기(undo) (F6)

<기능 설명>
- 최근 열어본 이미지 : 이미지를 열 때마다 기록을 남겨 최신순으로 출력
- 되돌리기 : 이미지 변경이 있을 때마다 직전 이미지를 기록에 추가하여 관리하고 되돌리도록 처리
- 열기, 초기화, 종료 시 이미지가 존재한다면 저장할지 물어보고 결정하기
- 창의 크기가 변경되면 그에 맞게 이미지가 바뀌도록 처리
- 이미지 파일이 선택되었을 때만 편집 메뉴들이 활성화 되도록 처리
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from functools import partial
import cv2
import numpy as np

# 최근 열어본 이력을 조회할 수 있도록 구현
# - 파일을 열 때마다 경로를 어딘가(list)에 저장
# - 저장된 내용을 메뉴로 표시
# - 최신순으로 표시 및 개수제한? 추가 할 수 있음
recent_files = []
def add_history(file_path):
    if file_path in recent_files: # 이미 열어본적이 있는 파일이라면
        recent_files.remove(file_path) # 기존 내역을 지워라
    recent_files.append(file_path) # 가장 마지막에 기록을 추가해라
    # print("현재 이력 : ", len(recent_files))

    # 최근 열어본 파일들 메뉴에 대한 정리
    menu_recent.delete(0, "end") # 전체 하위 메뉴를 삭제
    for history in get_history(): # 설정된 최근목록을 가져와서
        menu_recent.add_command( # 메뉴에 추가
            label=history, #표시될 글자 설정
            command=partial(open_recent_image, history) #눌렀을 때 열 파일 전달
        )

def get_history():
    # return recent_files # 전체
    return recent_files[::-1][:10] #뒤집기(최신순)

#---------------------------------------------
# 일반 함수들
#---------------------------------------------
def show_image(image_pillow):
    if image_pillow is None:
        image_tkinter = None
    else:
        image_thumb = image_pillow.copy() # 썸네일 제작을 위해 사본을 생성
        viewer_width = viewer.winfo_width() # 표시될 뷰어(라벨)의 폭
        viewer_height = viewer.winfo_height() # 표시될 뷰어(라벨)의 높이
        image_thumb.thumbnail((viewer_width, viewer_height)) # 썸네일 크기 조절
        image_tkinter = ImageTk.PhotoImage(image_thumb) # Tkinter 용으로 변환
    # image_tkinter를 표시하고, image_tkinter와 image_pillow를 뷰어에 숨겨놓는다
    viewer.config(image=image_tkinter)
    viewer.image_thumbnail = image_tkinter
    viewer.image_origin = image_pillow

    update_menu_status() # 메뉴 갱신 (알아서해!)

def is_working():
    # if viewer.image_origin is not None:       # 이미지가 없으면
    #     return True                           # 작업중인거고
    # else:                                     # 아니면
    #     return False                          # 작업중이 아닌거야
    return viewer.image_origin is not None      # 이미지가 있는지 확인해서 알려줄게

def get_image():
    return viewer.image_origin

def check_save():
    if not is_working(): # 작업중이 아니면
        return True # 그냥 진행해도 돼~

    # 사용자의 의사를 물어봐 → 예(True), 아니오(False), 취소(None)가 나올거야~
    answer = messagebox.askyesnocancel(
        "저장 확인", "작업중인 내용을 저장하시겠습니까?",
        parent=window
    )
    if answer is None: #취소면
        return False #그만 진행해~

    if answer: # 저장하겠다고 하면
        save_image() # 저장 함수좀 실행해줘
    else: # 저장 안하겠다고 하면
        pass # 아무것도 하지마

    return True # 다 했어? 그럼 계속 진행해

def open_recent_image(file_path):
    if check_save() == False:
        return
    # 파일 선택창만 제외하고 open_image와 동일한 코드
    if file_path == "":
        return

    # pillow로 이미지 읽기
    with Image.open(file_path) as file:
        image_pillow = file.convert("RGB")

    # 읽은 이미지를 viewer에 표시
    # 사본 만들어서... 썸네일 처리해서... 라벨에 config설정하고... 참조 연결하고...
    # 힘드니까 함수를 만들어서 부르자!
    show_image(image_pillow)

    # 이미지가 열리고 나서 최근 열어본 이미지 기록에 추가
    add_history(file_path)

def deactivate_menu():
    menu_file.entryconfig("이미지 저장", state="disabled")
    menu_file.entryconfig("이미지 초기화", state="disabled")
    # menubar.entryconfig("편집", state="disabled")
    menu_edit.entryconfig("흑백 변환", state="disabled")
    menu_edit.entryconfig("이진화", state="disabled")
    menu_edit.entryconfig("블러", state="disabled")
    menu_edit.entryconfig("모폴로지", state="disabled")
    menu_edit.entryconfig("캐니", state="disabled")

def activate_menu():
    menu_file.entryconfig("이미지 저장", state="normal")
    menu_file.entryconfig("이미지 초기화", state="normal")
    # menubar.entryconfig("편집", state="normal")
    menu_edit.entryconfig("흑백 변환", state="normal")
    menu_edit.entryconfig("이진화", state="normal")
    menu_edit.entryconfig("블러", state="normal")
    menu_edit.entryconfig("모폴로지", state="normal")
    menu_edit.entryconfig("캐니", state="normal")

def update_menu_status():
    if is_working():
        activate_menu()
    else:
        deactivate_menu()

def pillow_to_cv(image_pillow):
    image_np = np.array(image_pillow)                       # NumPy 배열로 바꾸고
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)    # RGB를 BGR로 바꾸고
    return image_cv                                         # 반환

def cv_to_pillow(image_cv):
    if image_cv.ndim == 3:
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)          # BGR을 RGB로 바꾸고
    image_pillow = Image.fromarray(image_cv)                # NumPy 배열 → Pillow 이미지로 변환
    return image_pillow

#---------------------------------------------
# 콜백 함수들
#---------------------------------------------
def open_image(event=None):
    if check_save() == False:
        return

    # 파일 선택창을 열어서 불러올 이미지 파일을 선택하게 한다
    file_path = filedialog.askopenfilename(
        parent=window,
        title="불러올 이미지 선택",
        filetypes=[
            ("이미지 파일", "*.jpg *.jpeg *.png *.bmp"),
            ("모든 파일", "*.*")
        ]
    )
    # 취소를 눌렀으면 더이상의 진행을 하지 않는다
    if file_path == "":
        return

    # pillow로 이미지 읽기
    with Image.open(file_path) as file:
        image_pillow = file.convert("RGB")

    # 읽은 이미지를 viewer에 표시
    # 사본 만들어서... 썸네일 처리해서... 라벨에 config설정하고... 참조 연결하고...
    # 힘드니까 함수를 만들어서 부르자!
    show_image(image_pillow)

    # 이미지가 열리고 나서 최근 열어본 이미지 기록에 추가
    add_history(file_path)

def reset_image(event=None):
    if check_save() == False:
        return

    # viewer에 설정된 이미지를 모두 제거
    show_image(None)

def close_window(event=None):
    if check_save() == False:
        return

    window.destroy()

def save_image(event=None):
    if not is_working():
        return

    # filedialog에서 저장용 창을 띄운다
    file_path = filedialog.asksaveasfilename(
        title="파일 저장 위치 확인",
        filetypes=[
            ("PNG 파일", "*.png"),
            ("JPG 파일", "*.jpg"),
            ("모든 파일", "*.*")
        ]
    )
    # print("file_path", file_path)
    if file_path == "":
        return

    # 이미지 추출
    image = get_image()
    image.save(file_path)

def resize_image(event):
    # 현재 설정된 이미지를 가져와서 화면에 맞게 다시 표시하는것
    if is_working():
        image = get_image()
        show_image(image)

def edit_grayscale(event=None):
    # image = get_image()     # 이미지를 꺼내온다.
    # image_np = np.array(image)  # pillow → numpy
    # image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)  # RGB → BGR
    # image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    # image_pillow = Image.fromarray(image_gray)
    # show_image(image_pillow)

    image = get_image()
    image_cv = pillow_to_cv(image)
    image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    image_pillow = cv_to_pillow(image_gray)
    show_image(image_pillow)

def edit_binarize(event=None):
    image = get_image()
    image_cv = pillow_to_cv(image)
    image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    _, image_binary = cv2.threshold(
        image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    image_pillow = cv_to_pillow(image_binary)
    show_image(image_pillow)

def edit_blur(event=None):
    image = get_image()
    image_cv = pillow_to_cv(image)
    image_blur = cv2.GaussianBlur(image_cv, (9, 9), 0)
    image_pillow = cv_to_pillow(image_blur)
    show_image(image_pillow)

def edit_morphology(event=None):
    image = get_image()
    image_cv = pillow_to_cv(image)
    kernel = np.ones((9, 9), dtype=np.uint8)
    image_morph = cv2.morphologyEx(image_cv, cv2.MORPH_CLOSE, kernel)
    image_pillow = cv_to_pillow(image_morph)
    show_image(image_pillow)

def edit_canny(event=None):
    image = get_image()
    image_cv = pillow_to_cv(image)
    image_canny = cv2.Canny(image_cv, 50, 150)
    image_pillow = cv_to_pillow(image_canny)
    show_image(image_pillow)

#---------------------------------------------
# 화면 배치
#---------------------------------------------
window = tk.Tk()
window.title("이미지 편집기 v0.1")
window.geometry("500x500")

viewer = tk.Label(window, bg="white")
viewer.pack(fill="both", expand=True)
viewer.image_thumbnail = None # 썸네일로 표시되는 이미지를 붙잡아두기 위해
viewer.image_origin = None # 원본 이미지를 붙잡아두기 위해

#---------------------------------------------
# 메뉴 배치
#---------------------------------------------
menubar = tk.Menu(window) # 메뉴바
menu_file = tk.Menu(menubar, tearoff=False) # 파일 메뉴
menu_edit = tk.Menu(menubar, tearoff=False) # 편집 메뉴

window.config(menu=menubar) # 창에 메뉴바 설정
menubar.add_cascade(label="파일", menu=menu_file) # 메뉴바에 파일 메뉴 추가
menubar.add_cascade(label="편집", menu=menu_edit) # 메뉴바에 편집 메뉴 추가

menu_file.add_command(label="이미지 열기", accelerator="Ctrl+O", command=open_image)

menu_recent = tk.Menu(menu_file, tearoff=False)
menu_file.add_cascade(label="최근 열어본 파일...", menu=menu_recent)
menu_file.add_command(label="이미지 저장", accelerator="Ctrl+S", command=save_image)
menu_file.add_command(label="이미지 초기화", accelerator="Ctrl+R", command=reset_image)
menu_file.add_separator()
menu_file.add_command(label="프로그램 종료", accelerator="Alt+F4", command=close_window)

menu_edit.add_command(label="흑백 변환", accelerator="F1", command=edit_grayscale)
menu_edit.add_command(label="이진화", accelerator="F2", command=edit_binarize)
menu_edit.add_command(label="블러", accelerator="F3", command=edit_blur)
menu_edit.add_command(label="모폴로지", accelerator="F4", command=edit_morphology)
menu_edit.add_command(label="캐니", accelerator="F5", command=edit_canny)

#---------------------------------------------
# 이벤트 바인딩
#---------------------------------------------
window.bind("<Control-o>", open_image)
window.bind("<Control-r>", reset_image)
window.bind("<Control-s>", save_image)
window.bind("<Configure>", resize_image)

window.bind("<F1>", edit_grayscale)
window.bind("<F2>", edit_binarize)
window.bind("<F3>", edit_blur)
window.bind("<F4>", edit_morphology)
window.bind("<F5>", edit_canny)

# window.bind("<Alt-F4>", close_window)
window.protocol("WM_DELETE_WINDOW", close_window)

update_menu_status()

#---------------------------------------------
# 화면 구동
#---------------------------------------------
window.mainloop()



