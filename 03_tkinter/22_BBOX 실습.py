

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


photo_image = None
image_file_path = None

image_width = 0
image_height = 0

start_x = None
start_y = None
rect_id = None

bbox_list = []


#---------------------------------------------------------------
# 콜백 함수
#---------------------------------------------------------------
def open_image():
    global photo_image, image_file_path
    global image_width, image_height
    global bbox_list, rect_id

    image_file_path = filedialog.askopenfilename(
        filetypes=[("PNG Files", "*.png")]
    )

    if image_file_path == "":
        return

    image = Image.open(image_file_path)

    image_width = image.width
    image_height = image.height

    photo_image = ImageTk.PhotoImage(image)

    canvas.delete("all")

    canvas.configure(
        width=image_width,
        height=image_height
    )

    canvas.create_image(
        0, 0,
        image=photo_image, anchor="nw"
    )

    bbox_list = []
    rect_id = None

def mouse_down(event):
    global start_x, start_y, rect_id

    if photo_image is None:
        return

    start_x = event.x
    start_y = event.y

    rect_id = canvas.create_rectangle(
        start_x, start_y,
        start_x, start_y,
        outline="red", width=5
    )

def mouse_move(event):
    if rect_id is None:
        return

    canvas.coords(
        rect_id,
        start_x, start_y,
        event.x, event.y
    )

def mouse_up(event):
    global rect_id

    if rect_id is None:
        return

    if start_x < event.x:
        x1 = start_x
        x2 = event.x
    else:
        x1 = event.x
        x2 = start_x

    if start_y < event.y:
        y1 = start_y
        y2 = event.y
    else:
        y1 = event.y
        y2 = start_y

    canvas.coords(rect_id, x1, y1, x2, y2)

    if x1 != x2 and y1 != y2:
        bbox_list.append((x1, y1, x2, y2))

    rect_id = None

def clear_all():
    global bbox_list, rect_id

    if photo_image is None:
        return

    bbox_list = []
    rect_id = None

    canvas.delete("all")

    canvas.create_image(
        0, 0,
        image=photo_image, anchor="nw"
    )

def save_image():
    if photo_image is None:
        return

    save_path = image_file_path.replace(".png", ".txt")

    with open(save_path, "w", encoding="utf-8") as file:

        for x1, y1, x2, y2 in bbox_list:

            x = ((x1 + x2) / 2) / image_width
            y = ((y1 + y2) / 2) / image_height

            w = (x2 - x1) / image_width
            h = (y2 - y1) / image_height

            file.write(
                f"0 {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n"
            )

#---------------------------------------------------------------
# 화면 배치
#---------------------------------------------------------------
window = tk.Tk()
window.title("BBOX 실습")

canvas = tk.Canvas(window, bg="white")
canvas.pack()


#---------------------------------------------------------------
# 메뉴 배치
#---------------------------------------------------------------
menubar = tk.Menu(window)

menu_file = tk.Menu(menubar, tearoff=False)
menu_file.add_command(label="이미지 열기", command=open_image)
menu_file.add_command(label="이미지 저장", command=save_image)

menubar.add_cascade(label="파일", menu=menu_file)

menu_edit = tk.Menu(menubar, tearoff=False)
menu_edit.add_command(label="모두 지우기", command=clear_all)

menubar.add_cascade(label="편집", menu=menu_edit)

window.config(menu=menubar)


#---------------------------------------------------------------
# 이벤트 바인딩
#---------------------------------------------------------------
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<ButtonRelease-1>", mouse_up)



window.mainloop()


