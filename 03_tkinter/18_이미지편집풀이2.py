"""
# 이미지를 편집할 수 있는 프로그램을 개발하세요.

# 메뉴의 형태

[파일]
+- 이미지 열기 (Ctrl+O)
+- 최근 열어본 이미지 +-  이미지1
                   +-  이미지2
+- 이미지 저장 (Ctrl+S)
+- 이미지 초기화 (Ctrl+R)
+- 프로그램 종료 (Alt+F4)

[편집]
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
- 이미지 파일이 선택되었을 때만 편집 메뉴들이 활성화되도록 처리
"""


import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

#---------------------------------------------------------------------
# 일반 함수들
#---------------------------------------------------------------------
def show_image(image_pillow):
    if image_pillow is None:
        image_tkinter = None
    else:
        image_thumb = image_pillow.copy()      # 썸네일 제작을 위해 사본을 생성
        viewer_width = viewer.winfo_width()    # 표시될 뷰어(라벨)의 폭
        viewer_height = viewer.winfo_height()  # 표시될 뷰어(라벨)의 높이
        image_thumb.thumbnail((viewer_width, viewer_height))    # 썸네일 크기 조절
        image_tkinter = ImageTk.PhotoImage(image_thumb)         # Tkinter용으로 변환
    # image_tkinter를 표시하고, image_tkinter와 image_pillow를 뷰어에 숨겨 놓는다.
    viewer.config(image=image_tkinter)
    viewer.image_thumbnail = image_tkinter
    viewer.image_origin = image_pillow

def is_working():
    # if viewer.image_origin is None:           # 이미지가 없으면
    #     return False                          # 작업중인 거고
    # else:                                     # 아니면
    #     return True                           # 작업 중이 아닌 것이다.
    return viewer.image_origin is not None      # 이미지가 있는지 확인해서 알려줄게.

def get_image():
    return viewer.image_origin

def check_save():
    if not is_working():    # 작업 중이 아니라면
        return True         # 그냥 진행해도 돼.

    # 사용자의 의사를 물어본다 → 예(True), 아니오(False), 취소(None)가 나올 거야.
    answer = messagebox.askyesnocancel(
        "저장 확인", "작업 중인 내용을 저장하시겠습니까?",
        parent=window)

    if answer is None:     # 취소면
        return False       # 그만 진행해.

    if answer:             # 저장하겠다고 하면
        save_image()       # 저장 함수 좀 실행해 줘.
    else :                 # 저장 안 하겠다고 하면
        pass               # 아무것도 하지 마.

    return True            # 다 했어? 그럼 계속 진행해.

#---------------------------------------------------------------------
# 콜백 함수들
#---------------------------------------------------------------------
def open_image(event=None):
    if check_save() == False:
        return

    # 파일 선택창을 열어서 불러올 이미지 파일을 선택하게 한다.
    file_path = filedialog.askopenfilename(
        parent=window,
        title="불러올 이미지 선택",
        filetypes=[
            ("이미지 파일", "*.jpg *jpeg *.png *.bmp"),
            ("모든 파일", "*.*")
        ]
    )
    # 취소를 눌렀으면 더 이상의 진행을 하지 않는다.
    if file_path == "":
        return

    # pillow로 이미지 읽기
    with Image.open(file_path) as file:
        image_pillow = file.convert("RGB")

    # 읽은 이미지를 viewer에 표시
    # 사본 만들고... 썸네일 처리해서... 라벨에 config 설정하고... 참조 연결하고...
    # 힘드니까 함수를 만들어서 부르자!
    show_image(image_pillow)

def reset_image(event=None):
    if check_save() == False:
        return

    # viewer에 설정된 이미지를 모두 제거
    show_image(None)

def close_window(event=None):
    if is_working():
        answer = messagebox.askyesnocancel(
            "저장 확인", "작업 중인 내용을 저장하시겠습니까?",
            parent=window)
        # 예(True), 아니오(False), 취소(None)
        if answer is None:
            return      # 취소면 중지

        if answer:
            # print("파일 저장 로직을 추가")
            save_image()
        else :
            pass

    window.destroy()

def save_image(event=None):
    if not is_working():
        return

    # filedialog에서 저장용 창을 띄운다.
    file_path = filedialog.asksaveasfilename(
        title="파일 저장 위치 확인",
        filetypes=[
            ("PNG 파일", "*.png"),
            ("JPG 파일", "*.jpg"),
            ("모든 파일", "*.*"),
        ]
    )
    # print("file_path", file_path)
    if file_path == "":
        return

    # 이미지 추출
    image = get_image()
    image.save(file_path)

    if file_path == "":
        return

#---------------------------------------------------------------------
# 화면 배치
#---------------------------------------------------------------------
window = tk.Tk()
window.title("이미지 편집기 v0.1")
window.geometry("500x500")

viewer = tk.Label(window, bg="white")
viewer.pack(fill="both", expand=True)
viewer.image_thumbnail = None    # 썸네일로 표시되는 이미지를 붙잡아 두기 위해
viewer.image_origin = None       # 원본 이미지를 붙잡아 두기 위해

#---------------------------------------------------------------------
# 메뉴 배치
#---------------------------------------------------------------------
menubar = tk.Menu(window)     # 메뉴바
menu_file = tk.Menu(menubar, tearoff=False)    # 파일 메뉴
menu_edit = tk.Menu(menubar, tearoff=False)    # 편집 메뉴

window.config(menu=menubar)    # 창에 메뉴바 설정
menubar.add_cascade(label="파일", menu=menu_file)    # 메뉴바에 파일 메뉴 추가
menubar.add_cascade(label="편집", menu=menu_edit)    # 메뉴바에 편집 메뉴 추가

menu_file.add_command(label="이미지 열기", accelerator="Ctrl+O", command=open_image)
menu_file.add_command(label="이미지 저장", accelerator="Ctrl+S", command=save_image)
menu_file.add_command(label="이미지 초기화", accelerator="Ctrl+R", command=reset_image)
menu_file.add_separator()
menu_file.add_command(label="프로그램 종료", accelerator="Alt+F4", command=close_window)

menu_edit.add_command(label="흑백 변환", accelerator="", command=None)
menu_edit.add_command(label="이진화", accelerator="", command=None)
menu_edit.add_command(label="블러", accelerator="", command=None)
menu_edit.add_command(label="모폴로지", accelerator="", command=None)
menu_edit.add_command(label="캐니", accelerator="", command=None)

#---------------------------------------------------------------------
# 이벤트 바인딩
#---------------------------------------------------------------------
window.bind("<Control-o>", open_image)
window.bind("<Control-s>", save_image)
window.bind("<Control-r>", reset_image)
# window.bind("<Alt-F4>", close_window)
window.protocol("WM_DELETE_WINDOW", close_window)


#---------------------------------------------------------------------
# 화면 구동
#---------------------------------------------------------------------
window.mainloop()


