import tkinter as tk

# 필요한 좌표 및 도형 데이터
shape_id = None
start_x = None
start_y = None

# 콜백 함수
def mouse_down(event):
    global shape_id, start_x, start_y
    start_x = event.x # 시작x좌표
    start_y = event.y # 시작y좌표

    # 임시 도형 생성 - var_shape 변수에 저장된 도형에 따라 생성명령을 다르게 적용
    if var_shape.get() == "rect":
        shape_id = canvas.create_rectangle(
            start_x, start_y, start_x, start_y,
            outline="gray", width=2, tags="temp",
            dash=(5, 3)
        )
    elif var_shape.get() == "line":
        shape_id = canvas.create_line(
            start_x, start_y, start_x, start_y,
            fill="gray", width=2, tags="temp",
            dash=(5,3)
        )
    elif var_shape.get() == "oval":
        shape_id = canvas.create_oval(
            start_x, start_y, start_x, start_y,
            outline="gray", width=2, tags="temp",
            dash=(5,3)
        )

def mouse_move(event):
    # shape_id가 존재한다면 도형의 위치를 조정 (선하고 동일한 명령)
    if shape_id is None:
        return
    canvas.coords(
        shape_id, start_x, start_y, event.x, event.y
    )

def mouse_up(event):
    # 도형을 확정하면서 색상이나 태그를 변경하고 shape_id를 None으로 되돌린다
    global shape_id, start_x, start_y
    if shape_id is None:
        return

    # 좌표 마지막 조정
    canvas.coords(shape_id, start_x, start_y, event.x, event.y)

    if var_shape.get() == "rect":
        canvas.itemconfig(shape_id, outline="black", tags="rect", dash=())
    elif var_shape.get() == "line":
        canvas.itemconfig(shape_id, fill="black", tags="line", dash=())
    elif var_shape.get() == "oval":
        canvas.itemconfig(shape_id, outline="black", tags="oval", dash=())

    # 값 초기화
    shape_id = None
    start_x = None
    start_y = None

def delete_rect():
    canvas.delete("rect")

def delete_line():
    canvas.delete("line")

def delete_oval():
    canvas.delete("oval")

def delete_all():
    canvas.delete("all")

# 창 생성 및 배치
window = tk.Tk()
window.title("캔버스 실습")
window.geometry("500x500")

# 메뉴 배치
menubar = tk.Menu(window)
window.config(menu=menubar)

menu_draw = tk.Menu(menubar, tearoff=False)
menu_delete = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="그리기", menu=menu_draw)
menubar.add_cascade(label="지우기", menu=menu_delete)

# 도형별 그리기 메뉴
var_shape = tk.StringVar(value="rect")
menu_draw.add_radiobutton(label="사각형", value="rect", var=var_shape)
menu_draw.add_radiobutton(label="직선", value="line", var=var_shape)
menu_draw.add_radiobutton(label="원", value="oval", var=var_shape)

# 도형별 지우기 메뉴
menu_delete.add_command(label="사각형 지우기", command=delete_rect)
menu_delete.add_command(label="직선 지우기", command=delete_line)
menu_delete.add_command(label="원 지우기", command=delete_oval)
menu_delete.add_separator()
menu_delete.add_command(label="전부 지우기", command=delete_all)

# 캔버스 전체화면에 배치
canvas = tk.Canvas(window, bg="white", cursor="crosshair")
canvas.pack(fill="both", expand=True)

# 캔버스에 마우스 이벤트 등록
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<ButtonRelease-1>", mouse_up)
canvas.bind("<B1-Motion>", mouse_move)

# 창 구동
window.mainloop()
