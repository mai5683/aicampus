import tkinter as tk

window = tk.Tk()
window.title("키패드 만들기")
window.geometry("400x600")

font_main = ("Binggrae", 22)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10, fill="x")

def entry_clear():
    entry_clear.delete(0, tk.END)


# 첫 번째 줄
frame_btns1 = tk.Frame(window)
frame_btns1.pack(pady=20, fill="x")
frame_btns1.columnconfigure(0, weight=1, uniform="same")
frame_btns1.columnconfigure(1, weight=1, uniform="same")
frame_btns1.columnconfigure(2, weight=1, uniform="same")

btn_1 = tk.Button(frame_btns1, text="1", font=font_main)
btn_1.grid(row=0, column=0, sticky="nsew", pady=1, padx=10)
btn_2 = tk.Button(frame_btns1, text="2", font=font_main)
btn_2.grid(row=0, column=1, sticky="nsew", pady=1, padx=10)
btn_3 = tk.Button(frame_btns1, text="3", font=font_main)
btn_3.grid(row=0, column=2, sticky="nsew", pady=1, padx=10)

# 두 번째 줄
frame_btns2 = tk.Frame(window)

frame_btns2.pack(pady=20, fill="x")
frame_btns2.columnconfigure(0, weight=1, uniform="same")
frame_btns2.columnconfigure(1, weight=1, uniform="same")
frame_btns2.columnconfigure(2, weight=1, uniform="same")

btn_4 = tk.Button(frame_btns2, text="4", font=font_main)
btn_4.grid(row=0, column=0, sticky="nsew", pady=1, padx=10)
btn_5 = tk.Button(frame_btns2, text="5", font=font_main)
btn_5.grid(row=0, column=1, sticky="nsew", pady=1, padx=10)
btn_6 = tk.Button(frame_btns2, text="6", font=font_main)
btn_6.grid(row=0, column=2, sticky="nsew", pady=1, padx=10)

# 세 번째 줄
frame_btns3 = tk.Frame(window)

frame_btns3.pack(pady=20, fill="x")
frame_btns3.columnconfigure(0, weight=1, uniform="same")
frame_btns3.columnconfigure(1, weight=1, uniform="same")
frame_btns3.columnconfigure(2, weight=1, uniform="same")

btn_7 = tk.Button(frame_btns3, text="7", font=font_main)
btn_7.grid(row=0, column=0, sticky="nsew", pady=1, padx=10)
btn_8 = tk.Button(frame_btns3, text="8", font=font_main)
btn_8.grid(row=0, column=1, sticky="nsew", pady=1, padx=10)
btn_9 = tk.Button(frame_btns3, text="9", font=font_main)
btn_9.grid(row=0, column=2, sticky="nsew", pady=1, padx=10)

# 네 번째 줄
frame_btns4 = tk.Frame(window)

frame_btns4.pack(pady=20, fill="x")
frame_btns4.columnconfigure(0, weight=1, uniform="same")
frame_btns4.columnconfigure(1, weight=1, uniform="same")
frame_btns4.columnconfigure(2, weight=1, uniform="same")

btn_star = tk.Button(frame_btns4, text="*", font=font_main)
btn_star.grid(row=0, column=0, sticky="nsew", pady=1, padx=10)
btn_zero = tk.Button(frame_btns4, text="0", font=font_main)
btn_zero.grid(row=0, column=1, sticky="nsew", pady=1, padx=10)
btn_sharp = tk.Button(frame_btns4, text="#", font=font_main)
btn_sharp.grid(row=0, column=2, sticky="nsew", pady=1, padx=10)

# 다섯 번째 줄
frame_btns5 = tk.Frame(window)

frame_btns5.pack(pady=20, fill="x")
frame_btns5.columnconfigure(0, weight=1, uniform="same")
frame_btns5.columnconfigure(1, weight=1, uniform="same")

btn_back = tk.Button(frame_btns5, text="←", font=font_main, command=entry_clear)
btn_back.grid(row=0, column=0, sticky="nsew", pady=1, padx=10)
btn_clear = tk.Button(frame_btns5, text="clear", font=font_main)
btn_clear.grid(row=0, column=1, sticky="nsew", pady=1, padx=10)




window.mainloop()
