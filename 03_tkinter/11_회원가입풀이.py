

import tkinter as tk


#---------------------------------------------
# 화면 구성
#---------------------------------------------
window = tk.Tk()
window.title("회원 가입 정보 입력")
window.geometry("600x400")
window.resizable(False, False)

# 글꼴 설정
font_title = ("Binggrae", 30)
font_widget = ("Binggrae", 20)
font_widget_small = ("Binggrae", 12)

# 위젯 배치
label_title = tk.Label(
    window, text="회원 가입", font=font_title,
    anchor="w", padx=10
)
label_title.pack(pady=10, ipady=10, fill="x")

# 아이디 관련 위젯들
frame_id = tk.Frame(window)
frame_id.pack(fill="x")
frame_id.columnconfigure(0, weight=3, uniform="input") #uniform은 그룹이름(자유)
frame_id.columnconfigure(1, weight=7, uniform="input")

label_id = tk.Label(frame_id, text="ID", font=font_widget)
label_id.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

entry_id = tk.Entry(frame_id, font=font_widget)
entry_id.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# 비밀번호 관련 위젯들
frame_pw = tk.Frame(window)
frame_pw.pack(fill="x")
frame_pw.columnconfigure(0, weight=3, uniform="input")
frame_pw.columnconfigure(1, weight=7, uniform="input")

label_pw = tk.Label(frame_pw, text="Password", font=font_widget)
label_pw.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

entry_pw = tk.Entry(frame_pw, font=font_widget, show="●")
entry_pw.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# 비밀번호 확인 관련 위젯들
frame_pw2 = tk.Frame(window)
frame_pw2.pack(fill="x")
frame_pw2.columnconfigure(0, weight=3, uniform="input")
frame_pw2.columnconfigure(1, weight=7, uniform="input")

label_pw2 = tk.Label(frame_pw2, text="Password Again", font=font_widget_small)
label_pw2.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

entry_pw2 = tk.Entry(frame_pw2, font=font_widget, show="●")
entry_pw2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# 버튼들 관련 위젯
frame_buttons = tk.Frame(window)
frame_buttons.pack(fill="x")
frame_buttons.columnconfigure(0, weight=5, uniform="same")
frame_buttons.columnconfigure(1, weight=5, uniform="same")

btn_reset = tk.Button(
    frame_buttons,
    text="초기화",
    font=font_widget,
    bg="#e74c3c",
    fg="white",
    command=None
)
btn_reset.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

btn_signup = tk.Button(
    frame_buttons,
    text="회원가입",
    font=font_widget,
    bg="#3498db",
    fg="white",
    command=None
)
btn_signup.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# 결과 라벨 위젯
label_result = tk.Label(window, text="회원 가입 완료", font=font_widget)
label_result.pack(fill="x", pady=10)

#---------------------------------------------
# 화면 구동
#---------------------------------------------
window.mainloop()

