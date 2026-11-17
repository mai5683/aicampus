

import tkinter as tk

#-----------------------------------------------------
# 콜백 함수
#-----------------------------------------------------
def click_number_1():
    # label_display의 글자를 가져와서 "1"을 더한 뒤 재설정
    # print(label_display.cget("text"))
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "1"
    label_display.config(text=change)

def click_number_2():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "2"
    label_display.config(text=change)

def click_number_3():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "3"
    label_display.config(text=change)

def click_number_4():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "4"
    label_display.config(text=change)

def click_number_5():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "5"
    label_display.config(text=change)

def click_number_6():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "6"
    label_display.config(text=change)

def click_number_7():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "7"
    label_display.config(text=change)

def click_number_8():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "8"
    label_display.config(text=change)

def click_number_9():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "9"
    label_display.config(text=change)

def click_number_star():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "*"
    label_display.config(text=change)

def click_number_0():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "0"
    label_display.config(text=change)

def click_number_hash():
    origin = label_display.cget("text")
    if len(origin) == 20:
        return
    change = origin + "#"
    label_display.config(text=change)

def click_delete():
    origin = label_display.cget("text")
    change = origin[:-1]
    label_display.config(text=change)

def click_clear():
    label_display.config(text="")

#-----------------------------------------------------
# 화면 배치
#-----------------------------------------------------
window = tk.Tk()
window.title("휴대전화 키패드")
window.geometry("400x430")

font_display = ("Binggrae", 24)
font_button = ("Binggrae", 16)

# 번호가 표시될 자리 (Label)
label_display = tk.Label(window, text="01012345678", font=font_display)
label_display.pack(pady=30, fill="x")

# 숫자 버튼이 위치할 자리 (Frame)
frame_numbers = tk.Frame(window)
frame_numbers.pack(pady=20, fill="x")
# 3열로 균일하게 배치
frame_numbers.columnconfigure(0, weight=1, uniform="same")
frame_numbers.columnconfigure(1, weight=1, uniform="same")
frame_numbers.columnconfigure(2, weight=1, uniform="same")

## 숫자 버튼을 배치
number_1 = tk.Button(frame_numbers, text="1", font=font_button, command=click_number_1)
number_2 = tk.Button(frame_numbers, text="2", font=font_button, command=click_number_2)
number_3 = tk.Button(frame_numbers, text="3", font=font_button, command=click_number_3)
number_4 = tk.Button(frame_numbers, text="4", font=font_button, command=click_number_4)
number_5 = tk.Button(frame_numbers, text="5", font=font_button, command=click_number_5)
number_6 = tk.Button(frame_numbers, text="6", font=font_button, command=click_number_6)
number_7 = tk.Button(frame_numbers, text="7", font=font_button, command=click_number_7)
number_8 = tk.Button(frame_numbers, text="8", font=font_button, command=click_number_8)
number_9 = tk.Button(frame_numbers, text="9", font=font_button, command=click_number_9)
number_star = tk.Button(frame_numbers, text="*", font=font_button, command=click_number_star)
number_0 = tk.Button(frame_numbers, text="0", font=font_button, command=click_number_0)
number_hash = tk.Button(frame_numbers, text="#", font=font_button, command=click_number_hash)

number_1.grid(row=0, column=0, sticky="nsew")
number_2.grid(row=0, column=1, sticky="nsew")
number_3.grid(row=0, column=2, sticky="nsew")
number_4.grid(row=1, column=0, sticky="nsew")
number_5.grid(row=1, column=1, sticky="nsew")
number_6.grid(row=1, column=2, sticky="nsew")
number_7.grid(row=2, column=0, sticky="nsew")
number_8.grid(row=2, column=1, sticky="nsew")
number_9.grid(row=2, column=2, sticky="nsew")
number_star.grid(row=3, column=0, sticky="nsew")
number_0.grid(row=3, column=1, sticky="nsew")
number_hash.grid(row=3, column=2, sticky="nsew")

# 기능 버튼이 위치할 자리 (Frame)
frame_functions = tk.Frame(window)
frame_functions.pack(pady=20, fill="x")
# 2열로 균일하게 배치
frame_functions.columnconfigure(0, weight=1, uniform="same")
frame_functions.columnconfigure(1, weight=1, uniform="same")

## 기능 버튼을 배치
func_delete = tk.Button(frame_functions, text="←", font=font_button, command=click_delete)
func_delete.grid(row=0, column=0, sticky="nsew")
func_clear = tk.Button(frame_functions, text="clear", font=font_button, command=click_clear)
func_clear.grid(row=0, column=1, sticky="nsew")

#-----------------------------------------------------
# 화면 구동
#-----------------------------------------------------
window.mainloop()