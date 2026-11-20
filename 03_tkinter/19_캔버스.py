"""
캔버스(Canvas)

좌표를 이용해서 이미지, 도형, 선, 글자 등을 그려주는 위젯
표시에 특화된 라벨과 달리 캔버스는 마우스를 이용해서 조작하는 것에 특화되어 있다.
"""

import tkinter as tk

#----------------------------------------------------------
# 화면 구성
#----------------------------------------------------------
window = tk.Tk()
window.title("캔버스 배우기")
window.geometry("500x500")

# 캔버스를 전체 화면에 배치
# - cursor : crosshair(십자), pencil(펜), dotbox(점), arrow(화살표)
canvas = tk.Canvas(window, bg="white", cursor="crosshair")
canvas.pack(fill="both", expand=True)

# 캔버스에 그림 그려놓기
# - 선 : create_line(시작x, 시작y, 종료x, 종료y, fill="선색상", width=선두께)
canvas.create_line(50, 50, 300, 200, fill="red", width=3)
canvas.create_line(450, 100, 100, 250, fill="blue", width=10)

#----------------------------------------------------------
# 화면 구동
#----------------------------------------------------------
window.mainloop()

