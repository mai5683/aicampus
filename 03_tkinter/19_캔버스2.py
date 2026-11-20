"""
캔버스(Canvas)

좌표를 이용해서 이미지, 도형, 선, 글자 등을 그려주는 위젯
표시에 특화된 라벨과 달리 캔버스는 마우스를 이용해서 조작하는 것에 특화되어 있다.
"""

import tkinter as tk

# 마우스로 선을 그릴 수 있도록 처리
# 마우스로 선을 그리려면 (마우스를 누르고) - (마우스를 이동하고) - (마우스를 떼야 한다)
start_x = None
start_y = None
finish_x = None
finish_y = None

#----------------------------------------------------------
# 콜백 함수
#----------------------------------------------------------
def mouse_down(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
    print("마우스 누름", event.x, event.y)

def mouse_up(event):
    global finish_x, finish_y
    finish_x = event.x
    finish_y = event.y
    # 좌표가 준비되었으니 선을 그려보자
    canvas.create_line(
        start_x, start_y, finish_x, finish_y,
        fill="black", width=5, tags="line")
    print("마우스 뗌", event.x, event.y)

def mouse_move(event):
    print("마우스 움직임", event.x, event.y)

def clear_canvas():
    # canvas.delete("태그")    # 그림을 그릴 때 해당 그림에 부여해 놓은 글자
    canvas.delete("all")      # 태그 무시하고 전부 지우기
    # canvas.delete("line")   # tags="line" 이라고 설정된 그림만 제거

#----------------------------------------------------------
# 화면 구성
#----------------------------------------------------------
window = tk.Tk()
window.title("캔버스 배우기")
window.geometry("500x500")

# 메뉴 배치
menubar = tk.Menu(window)
window.config(menu=menubar)

menu_task = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="작업", menu=menu_task)

menu_task.add_command(label="전부 지우기", command=clear_canvas)

# 캔버스를 전체 화면에 배치
# - cursor : crosshair(십자), pencil(펜), dotbox(점), arrow(화살표)
canvas = tk.Canvas(window, bg="white", cursor="crosshair")
canvas.pack(fill="both", expand=True)

# 마우스 이벤트 설정
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<ButtonRelease-1>", mouse_up)
canvas.bind("<Motion>", mouse_move)

#----------------------------------------------------------
# 화면 구동
#----------------------------------------------------------
window.mainloop()

