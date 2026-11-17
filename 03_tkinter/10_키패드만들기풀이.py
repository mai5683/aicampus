

import tkinter as tk

#--------------------------------------------------------------
# 콜백 함수
#--------------------------------------------------------------


#--------------------------------------------------------------
# 화면 배치
#--------------------------------------------------------------
window = tk.Tk()
window.title("휴대전화 키패드")
window.geometry("400x600")

font_display = ("Binggrae", 26)
font_button = ("Binggrae", 18)

# 번호가 표시될 자리 (Label)
label_display = tk.Label(window, text=("01055555555"), font=font_display)
label_display.pack(pady=30, fill="x")

# 숫자 버튼이 위치할 자리 (Frame)
frame_numbers = tk.Frame(window)
frame_numbers.pack(pady=20, fill="x")
# 3열로 균일하게 배치
frame_numbers.columnconfigure(0, weight=1, uniform="same")
frame_numbers.columnconfigure(1, weight=1, uniform="same")
frame_numbers.columnconfigure(2, weight=1, uniform="same")

## 숫자 버튼을 배치
number_1 =tk.Button(frame_numbers, text="1", font=font_button)
number_2 = tk.Button(frame_numbers, text="2", font=font_button)
number_3 = tk.Button(frame_numbers, text="3", font=font_button)
number_4 = tk.Button(frame_numbers, text="4", font=font_button)
number_5 = tk.Button(frame_numbers, text="5", font=font_button)
number_6 = tk.Button(frame_numbers, text="6", font=font_button)
number_7 = tk.Button(frame_numbers, text="7", font=font_button)
number_8 = tk.Button(frame_numbers, text="8", font=font_button)
number_9 = tk.Button(frame_numbers, text="9", font=font_button)
number_star = tk.Button(frame_numbers, text="*", font=font_button)
number_0 = tk.Button(frame_numbers, text="0", font=font_button)
number_hash = tk.Button(frame_numbers, text="#", font=font_button)

number_1.grid(row=0, column=0, sticky="nsew")
number_2.grid(row=0, column=1, sticky="nsew")
number_3.grid(row=0, column=2, sticky="nsew")
number_4.grid(row=0, column=0, sticky="nsew")
number_5.grid(row=0, column=1, sticky="nsew")
number_6.grid(row=0, column=2, sticky="nsew")
number_7.grid(row=0, column=0, sticky="nsew")
number_8.grid(row=0, column=1, sticky="nsew")
number_9.grid(row=0, column=2, sticky="nsew")
number_star.grid(row=0, column=0, sticky="nsew")
number_0.grid(row=0, column=1, sticky="nsew")
number_hash.grid(row=0, column=2, sticky="nsew")

# 기능 버튼이 위치할 자리 (Frame)
frame_functions = tk.Frame(window)
frame_functions.pack(pady=20, fill="x")
# 2열로 균일하게 배치
frame_functions.columnconfigure(0, weight=1, uniform="same")
frame_functions.columnconfigure(1, weight=1, uniform="same")

## 기능 버튼을 배치
func_delete = tk.Button(frame_functions, text="←", font=font_button)
func_delete.grid(row=0, column=0, sticky="nsew")
func_clear = tk.Button(frame_functions, text="clear", font=font_button)
func_clear.grid(row=0, column=1, sticky="nsew")


#--------------------------------------------------------------
# 화면 구동
#--------------------------------------------------------------
window.mainloop()