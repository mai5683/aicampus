import tkinter as tk

def click_btn_red():
    label.configure(bg="red")
def click_btn_green():
    label.configure(bg="green")
def click_btn_blue():
    label.configure(bg="blue")
def click_btn_black():
    label.configure(bg="black")

window = tk.Tk()
window.title("tkinter 실습")
window.geometry("500x300")

label = tk.Label(
    window,
    text="tkinter는 파이썬 표준 GUI 라이브러리 입니다"
)
label.pack(pady=20)

btn_red = tk.Button(
    window, text="빨강",
    command=click_btn_red)
btn_red.pack(pady=10)

btn_green = tk.Button(
    window, text="초록",
    command=click_btn_green)
btn_green.pack(pady=10)

btn_blue = tk.Button(
    window, text="파랑",
    command=click_btn_blue)
btn_blue.pack(pady=10)

btn_black = tk.Button(
    window, text="검정",
    command=click_btn_black)
btn_black.pack(pady=10)

window.mainloop()
