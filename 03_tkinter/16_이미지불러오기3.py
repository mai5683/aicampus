"""
파일 선택창을 열고 이미지를 선택하여 불러와 표시하는 문제
"""
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

#-----------------------------------------
# 콜백 함수
#-----------------------------------------
def open_image():
    try: # 플랜 A
        # 파일 선택 창을 표시
        file_path = filedialog.askopenfilename(
            parent=window,
            title="이미지 선택",
            filetypes=[
                ("이미지 파일", "*.png *.jpg *.gif"),
                ("모든 파일", "*.*")
            ]
        )
        # 파일 선택하지 않았다면 중지시킨다
        if file_path == "":
            return

        # 선택한 파일을 Pillow로 열기
        # image_pillow = Image.open(file_path)
        with Image.open(file_path) as file:
            image_pillow = file.convert("RGB")

        # 라벨에 이미지를 표시
        image_thumb = image_pillow.copy() #썸네일용 이미지 생성
        # image_thumb.thumbnail((400, 400)) #썸네일로 변경
        w = label_preview.winfo_width() # mainloop() 이후부터 나옴 (이전은 1)
        h = label_preview.winfo_height()
        image_thumb.thumbnail((w, h)) #썸네일로 변경
        image_tkinter = ImageTk.PhotoImage(image_thumb) #Tkinter용 이미지
        # (중요) 이미지 참조 유지를 위해 이미지가 표시되는 영역에 연결
        label_preview.config(image=image_tkinter)
        label_preview.thumb = image_tkinter #썸네일이 사라지지 않게 하기 위해
        label_preview.image = image_pillow #나중에 혹시모를 편집을 위해

        label_path.config(text=f"현재 이미지 : {str(file_path)}")
    except Exception: #플랜 B
        # 메세지 출력
        messagebox.showerror(
            "이미지 열기 오류",
            "읽을 수 없는 이미지입니다.\n올바른 형식의 파일을 선택하세요",
            parent=window
        )

        # 리셋 (선택)
        reset_image()

def reset_image():
    # 이미지를 표시하면서 설정한 정보들을 제거
    # label_path, label_preview(config, image, thumb)
    label_path.config(text="현재 이미지 : 없음")
    label_preview.config(image=None)
    label_preview.image = None
    label_preview.thumb = None

def close_window():
    # 이미지가 있을 때만 종료할건지 물어봐라!
    if label_preview.image is not None:
        answer = messagebox.askyesno(
            "종료 확인", "정말 종료하시겠어요?", parent=window
        )
        if answer == False:
            return

    window.destroy()

# (중요) bind로 지정된 함수는 이벤트 정보를 받아야 한다
def resize_thumbnail(event):
    if label_preview.image is None: # 썸네일이 없으면
        return

    # 원본이미지(pillow)를 불러와서 썸네일 생성 후 재설정
    image_thumb = label_preview.image.copy()
    w = label_preview.winfo_width()
    h = label_preview.winfo_height()
    image_thumb.thumbnail((w, h)) # 라벨의 크기에 맞게 썸네일 변경
    image_tkinter = ImageTk.PhotoImage(image_thumb)
    label_preview.config(image=image_tkinter)
    label_preview.thumb = image_tkinter

#-----------------------------------------
# 화면 배치
#-----------------------------------------

# 글꼴 설정
font_main = ("Binggrae", 16)

# 창 생성
window = tk.Tk()
window.title("이미지 불러오기 문제")
window.geometry("500x500")

# window의 x버튼에 대한 동작을 close_window 함수로 변경
window.protocol("WM_DELETE_WINDOW", close_window)

# 버튼들 배치
frame_btns = tk.Frame(window)
frame_btns.pack(pady=10, fill="x")
frame_btns.columnconfigure(0, weight=1, uniform="same")
frame_btns.columnconfigure(1, weight=1, uniform="same")
frame_btns.columnconfigure(2, weight=1, uniform="same")

btn_open = tk.Button(
    frame_btns, text="이미지 열기", font=font_main, command=open_image
)
btn_reset = tk.Button(
    frame_btns, text="초기화", font=font_main, command=reset_image
)
btn_close = tk.Button(
    frame_btns, text="종료", font=font_main, command=close_window
)

btn_open.grid(row=0, column=0, sticky="nsew", padx=10)
btn_reset.grid(row=0, column=1, sticky="nsew", padx=(0, 0))
btn_close.grid(row=0, column=2, sticky="nsew", padx=10)

# 선택된 파일 위치를 표시할 라벨
label_path = tk.Label(
    window, text="현재 이미지 : 없음",
    font=font_main,
    anchor="w"
)
label_path.pack(padx=10, pady=10, fill="x")

# 이미지를 미리보기 하기 위한 라벨
label_preview = tk.Label(window, bg="white")
label_preview.pack(padx=10, pady=10, fill="both", expand=True)
reset_image() #미리 한번 불러서 image, thumb과 같은 원래 없는 속성을 설정

# (+추가) 이미지 미리보기 영역의 크기가 변경되면 어떤 함수를 실행하겠다
# 특정 상황(이벤트)에 대한 처리 방식을 등록 --> bind(이벤트종류, 함수이름)
label_preview.bind("<Configure>", resize_thumbnail)

#-----------------------------------------
# 화면 구동
#-----------------------------------------
window.mainloop()