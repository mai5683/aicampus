"""
목표 : 이미지를 불러와서 원하는 대상을 마우스로 마킹하고 위치와 크기를 txt로 저장
"""

import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageOps, ImageTk
from pathlib import Path

# 불러온 파일의 원래 위치
file_path = None

# 그리기를 위한 데이터
box_id = None
start_x = None
start_y = None

# 그리기 콜백 함수
def mouse_down(event):
    # print("마우스 누름", event)
    if canvas.image_origin is None: #이미지가 없으면
        return #시작하지마세요

    global box_id, start_x, start_y
    # 시작지점을 기록
    start_x = event.x
    start_y = event.y
    # 사각형을 그린다
    box_id = canvas.create_rectangle(
        start_x, start_y, #사각형 시작지점
        start_x, start_y, #사각형 끝지점
        outline="yellow", width=3, dash=(5,3), tags="temp" #기타 정보
    )

def mouse_move(event):
    # print("마우스 움직임", event)
    if box_id is None:
        return
    # 임시 사각형의 좌표 조정
    canvas.coords(box_id, start_x, start_y, event.x, event.y)

def mouse_up(event):
    # print("마우스 뗌", event)
    if box_id is None:
        return
    # 마지막으로 임시 사각형의 좌표 조정
    canvas.coords(box_id, start_x, start_y, event.x, event.y)
    # 임시 사각형을 bbox로 변경
    canvas.itemconfig(box_id, outline="yellow", dash=(), tags="bbox")

# 콜백 함수
def open_file(event=None):
    global file_path
    try:
        file_path = filedialog.askopenfilename(
            parent=window,
            title="불러올 이미지 선택",
            filetypes=[
                ("이미지 파일", "*.jpg *.jpeg *.png"),
                ("모든 파일", "*.*")
            ]
        )
        if file_path == "":  # 미 선택시 중지
            file_path = None
            return

        # 이미지 읽기(pillow)
        with Image.open(file_path) as file:
            image_pillow = file.convert("RGB")

        # 이미지 변환 및 표시 (캔버스에 맞는 크기로 표시)
        canvas_width = canvas.winfo_width()  # 캔버스 폭
        canvas_height = canvas.winfo_height()  # 캔버스 높이
        image_thumb = ImageOps.contain(image_pillow, (canvas_width, canvas_height))

        image_tkinter = ImageTk.PhotoImage(image_thumb)

        canvas.delete("all") # 기존에 작성한 내역들을 모두 제거

        #이미지를 가운데 배치
        canvas.create_image(
            canvas_width // 2, canvas_height // 2,
            image=image_tkinter, anchor="center", tags="img"
        )
        canvas.image_thumbnail = image_tkinter  # 이미지 참조 유지를 위해
        canvas.image_origin = image_pillow # 크기변경 시 사용
    except Exception:
        messagebox.showerror("오류", "파일을 열 수 없습니다", parent=window)

# 이미지 크기를 캔버스에 맞게 재조정하는 작업
def resize_image(event):
    # 이미지를 캔버스 크기에 맞게 배치
    image_pillow = canvas.image_origin
    if image_pillow is None:
        return
    image_thumb = ImageOps.contain(image_pillow, (event.width, event.height))
    image_tkinter = ImageTk.PhotoImage(image_thumb)
    canvas.itemconfig("img", image=image_tkinter) # 이미지 속성 변경
    canvas.image_thumbnail = image_tkinter
    canvas.image_origin = image_pillow

    # 이미지를 중앙에 배치
    x = event.width // 2 # 중심x 계산
    y = event.height // 2 # 중심y 계산
    canvas.coords("img", x, y) # 캔버스 좌표변경

def save_file(event=None):
    if file_path is None:
        return
    # 불러온 이미지와 같은 위치에 같은 이름으로 확장자만 .txt인 파일을 만들어야 한다
    print("현재 이미지 경로", file_path)
    # 이미지의 확장자를 제거하고 .txt를 붙인다
    # name = Path(file_path).stem # 경로가 사라짐
    name = Path(file_path).with_suffix(".txt")
    print("확장자 제거", name)

    # tags="bbox"인 항목들을 가져와서 1개라도 있다면 저장을 위한 계산과 처리를 구현
    boxes = canvas.find_withtag("bbox")
    if len(boxes) == 0: # 1개도 없다면
        messagebox.showinfo(
            "알림", "생성한 bbox가 한개도 없어요!", parent=window
        )
        return # 중지하세요

    # 이미지의 위치와 크기를 구하고, 각 bbox의 위치와 크기를 구해서 0~1로 변환한 뒤 저장
    # x1, y1, x2, y2 = canvas.bbox("img")
    # print(x1, y1, x2, y2)

    # 위치는 coords()로 구하고, 크기는 canvas.image_thumbnail로 구하자
    x, y = canvas.coords("img")
    w = canvas.image_thumbnail.width()
    h = canvas.image_thumbnail.height()
    # print(x, y, w, h)

    # 이미지의 시작점 구하기
    image_start_x = x - w/2
    image_start_y = y - h/2
    image_finish_x = x + w/2
    image_finish_y = y + h/2

    # boxes의 정보를 꺼내서 비율을 계산해서 리스트에 담아두자
    box_list = []
    for box in boxes:
        x1, y1, x2, y2 = canvas.bbox(box) # 좌표 추출

        # (+추가) bbox가 이미지를 벗어났는지 판정해서 skip 처리
        if x1 < image_start_x:
            continue
        if y1 < image_start_y:
            continue
        if x2 > image_finish_x:
            continue
        if y2 > image_finish_y:
            continue

        # 폭과 높이, 중심점을 구해야한다
        box_width = x2 - x1 # 박스의 실제폭
        box_height = y2 - y1 # 박스의 실제높이
        box_cx = (x1 + x2) / 2 # 박스의 실제중심X (캔버스에서)
        box_cy = (y1 + y2) / 2 # 박스의 실제중심Y (캔버스에서)
        box_cx -= image_start_x # 박스의 중심X (이미지부터)
        box_cy -= image_start_y # 박스의 중심Y (이미지부터)

        # cx, cy, width, height를 0~1사이의 비율로 변환
        # - 폭과 높이는 큰 문제가 없음
        # - cx, cy는 canvas의 cx, cy와 이미지를 비교해야함
        box_cx = box_cx / w
        box_cy = box_cy / h
        box_width = box_width / w
        box_height = box_height / h
        # print(box_cx, box_cy, box_width, box_height)
        # print(f"0 {box_cx:.6f} {box_cy:.6f} {box_width:.6f} {box_height:.6f}")
        box_list.append(f"0 {box_cx:.6f} {box_cy:.6f} {box_width:.6f} {box_height:.6f}")

    # 리스트에 담긴 결과를 최종 파일로 내보내자
    with open(name, "w", encoding="utf-8") as file:
        for box in box_list:
            file.write(box)
            file.write("\n")
    messagebox.showinfo(
        "저장 완료", "생성한 bbox 정보가 저장되었습니다", parent=window
    )

def clear_work(event=None):
    # canvas.delete("all") # 이미지도 지워짐
    canvas.delete("bbox") # 상자만 지워짐
    canvas.delete("temp")  # 상자만 지워짐

def undo_work(event=None):
    # tags="bbox"인 항목들을 모두 꺼내서 마지막 항목만 삭제
    boxes = canvas.find_withtag("bbox")
    if len(boxes) == 0:
        return
    # print("boxes", boxes)
    canvas.delete(boxes[-1]) # 마지막 녀석을 지워라!

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
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<ButtonRelease-1>", mouse_up)
canvas.bind("<B1-Motion>", mouse_move)

# 창 구동
window.mainloop()

