

import tkinter as tk


def reset():
    entry_id.delete(0, tk.END)
    entry_pw.delete(0, tk.END)
    entry_pw_again.delete(0, tk.END)

    result_label.config(text="회원 가입을 진행하세요")

def member_join():
    id = entry_id.get()
    pw = entry_pw.get()
    pw_again = entry_pw_again.get()

    if id != "" and pw != "" and pw == pw_again:
        result_label.config(text="가입이 완료되었습니다")
    else:
        result_label.config(text="입력한 정보가 형식에 맞지 않습니다")



window = tk.Tk()
window.title("회원 가입")
window.geometry("600x450")

font_main = ("Binggrae", 16)

label_title = tk.Label(window, text="회원 가입", font=font_main)
label_title.pack(pady=20)


#--------------------------------------------------------------------------
frame_id = tk.Frame(window)
frame_id.pack(fill="x", padx=20, pady=8)

label_id = tk.Label(frame_id, text="ID", width=15, font=font_main)
label_id.pack(side="left")

entry_id = tk.Entry(frame_id, font=font_main, width=35)
entry_id.pack(side="left")



frame_pw = tk.Frame(window)
frame_pw.pack(fill="x", padx=20, pady=8)

label_pw = tk.Label(frame_pw, text="Password", width=15, font=font_main)
label_pw.pack(side="left")

entry_pw = tk.Entry(frame_pw, font=font_main, width=35)
entry_pw.pack(side="left")



frame_pw_again = tk.Frame(window)
frame_pw_again.pack(fill="x", padx=20, pady=8)

label_pw_again = tk.Label(frame_pw_again, text="Password Again", width=15, font=font_main)
label_pw_again.pack(side="left")

entry_pw_again = tk.Entry(frame_pw_again, font=font_main, width=35)
entry_pw_again.pack(side="left")


##--------------------------------------------------------------------------
frame_buttons = tk.Frame(window)
frame_buttons.pack(fill="x", padx=20, pady=15)

frame_buttons.columnconfigure(0, weight=1, uniform="same")
frame_buttons.columnconfigure(1, weight=1, uniform="same")

btn_reset = tk.Button(frame_buttons, text="초기화", font=font_main,
                      fg="red", command=reset)
btn_reset.grid(row=0, column=0, padx=5, sticky="ew")

btn_join = tk.Button(frame_buttons, text="회원 가입", font=font_main,
                     fg="blue", command=member_join)
btn_join.grid(row=0, column=1, padx=5, sticky="ew")


##--------------------------------------------------------------------------
result_label = tk.Label(window, text="회원 가입을 진행하세요", font=font_main)
result_label.pack(fill="x", padx=25, pady=15)



window.mainloop()

