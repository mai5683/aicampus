"""
캔버스(Canvas)

좌표를 이용해서 이미지, 도형, 선, 글자 등을 그려주는 위젯
표시에 특화된 라벨과 달리 캔버스는 마우스를 이용해서 조작하는 것에 특화되어 있다.
"""

import tkinter as tk

# 마우스로 선을 그릴 수 있도록 처리 (+ 임시선 표시까지 추가)
# 마우스로 선을 그리려면 (마우스를 누르고) - (마우스를 이동하고) - (마우스를 떼야 한다)
line_id = None      # 많은 선 중에 특정한 선만 변경하려면 그릴 때 ID를 같이 저장해 줘야 한다.
start_x = None
start_y = None
finish_x = None
finish_y = None

#----------------------------------------------------------
# 콜백 함수
#----------------------------------------------------------
def mouse_down(event):
    global start_x, start_y, line_id
    start_x = event.x
    start_y = event.y
    # 처음부터 임시선을 그려 둔다.
    line_id = canvas.create_line(
        start_x, start_y, start_x, start_y, fill="red", width=5, tags="temp"
    )
    print("임시선ID", line_id)

def mouse_up(event):
    # 기존에 그리고 있던 임시선을 최종 좌표로 확정, 색상 변경, 태그를 "temp"에서 "line"으로 변경
    if line_id is None:
        return
    canvas.coords(line_id, start_x, start_y, event.x, event.y)
    # canvas.itemconfig(고유ID, 바꾸고 싶은 속성 작성)
    canvas.itemconfig(line_id, fill="black", tags="line")
    print("마우스 뗌", event.x, event.y)
    line_id = None

def mouse_move(event):
    # 마우스를 눌렀을 때 만들어진 임시선의 끝점을 변경해야 한다.
    if line_id is None:
        return

    # line_id에 해당하는 선의 위치를 조정
    # canvas.coords(고유ID, 시작x, 시작y, 종료x, 종료y)
    canvas.coords(line_id, start_x, start_y, event.x, event.y)
    print("마우스 움직임", event.x, event.y)

def clear_canvas():
    # canvas.delete("태그")    # 그림을 그릴 때 해당 그림에 부여해 놓은 글자
    # canvas.delete("all")      # 태그 무시하고 전부 지우기
    canvas.delete("line")   # tags="line" 이라고 설정된 그림만 제거

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
canvas.bind("<B1-Motion>", mouse_move)

#----------------------------------------------------------
# 화면 구동
#----------------------------------------------------------
window.mainloop()

