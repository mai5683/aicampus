import tkinter as tk


def click_btn_small():
    label.configure(font=("", 7))
def click_btn_normal():
    label.configure(font=("", 8.5))
def click_btn_large():
    label.configure(font=("", 12))


window = tk.Tk()
window.title("tkinter 실습")
window.geometry("500x300")

label = tk.Label(
    window,
    text="tkinter는 파이썬 표준 GUI 라이브러리 입니다"
)
label.pack(pady=20)

btn_small = tk.Button(
    window, text="작게",
    command=click_btn_small)
btn_small.pack(pady=10)

btn_normal = tk.Button(
    window, text="보통",
    command=click_btn_normal)
btn_normal.pack(pady=10)

btn_large = tk.Button(
    window, text="크게",
    command=click_btn_large)
btn_large.pack(pady=10)

btn_plus = tk.Button(
    window, text="+",
    command=click_btn_plus)
btn_plus.pack(pady=10)


window.mainloop()