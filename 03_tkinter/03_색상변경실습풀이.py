"""
색상변경 실습 GUI 구현 풀이
"""

import tkinter as tk

#---------------------------------
# 버튼이 눌러지면서 실행될 함수
#---------------------------------
def click_btn_red():
    # label의 글자색상(fg)을 "red" 또는 팔레트의 색상(#c0392b)으로 변경
    label.config(fg="#c0392b")
def click_btn_green():
    label.config(fg="#27ae60")
def click_btn_blue():
    label.config(fg="#3498db")
def click_btn_black():
    label.config(fg="black")

#---------------------------------
# 창 생성
#---------------------------------
window = tk.Tk()
window.title("tkinter 실습 문제")
window.geometry("700x500+200+200")

#---------------------------------
# 위젯 배치
#---------------------------------
label = tk.Label(
    window,     # 소속
    text = "tkinter는 파이썬 표준 GUI 라이브러리 입니다",
    font = ("굴림", 24),
    fg = "black"
)
label.pack(pady=50)

btn_red = tk.Button(
    window,
    text = "빨강",
    font = ("굴림", 20),
    # 색상은 fg(foreground), bg(background) 두 가지 설정 가능 : fg는 글자색, bg는 글자 배경색
    fg = "#c0392b",
    command = click_btn_red     # 연결은 이름만!
)
btn_red.pack(pady=10)

btn_green = tk.Button(
    window,
    text = "초록", font = ("굴림", 20), fg = "#27ae60",
    command = click_btn_green)
btn_green.pack(pady=10)

btn_blue = tk.Button(
    window,
    text = "파랑", font = ("굴림", 20), fg = "#3498db",
    command = click_btn_blue)
btn_blue.pack(pady=10)

btn_black = tk.Button(
    window,
    text = "검정", font = ("굴림", 20), fg = "black",
    command = click_btn_black)
btn_black.pack(pady=10)

#---------------------------------
# 창 구동(표시)
#---------------------------------
window.mainloop()
