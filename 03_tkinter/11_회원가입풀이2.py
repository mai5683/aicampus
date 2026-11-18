
import re
import tkinter as tk
from tkinter import messagebox

#---------------------------------------------
# 콜백 함수
#---------------------------------------------
def click_btn_reset():
    # 지워지거나 변경될 때는 사용자의 진짜 의도가 맞는지 확인하는 작업이 필요
    # tkinter의 messagebox로 처리
    # answer = messagebox.askyesno("창제목", "보여줄문구", parent=소속창)
    answer = messagebox.askyesno(
        "삭제 확인",
        "정말 입력된 값을 지우시겠습니까?",
        parent=window
    )
    # print("answer", answer)
    # if not answer:
    if answer == False:
        return

    entry_id.delete(0, tk.END)
    entry_pw.delete(0, tk.END)
    entry_pw2.delete(0, tk.END)

def click_btn_signup():
    # 아이디 검사
    input_id = entry_id.get()
    regexp_id = r"^[a-z][a-z0-9]{4,19}$"
    match_id = re.fullmatch(regexp_id, input_id)
    if match_id is None:
        label_result.config(text="아이디가 형식에 맞지 않아요", fg="#e74c3c")
        return

    # 비밀번호 검사
    input_pw = entry_pw.get()
    regexp_pw = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[\!\@\#\$\%\^])[A-Za-z0-9\!\@\#\$\%\^]{8,16}$"
    match_pw = re.fullmatch(regexp_pw, input_pw)
    if match_pw is None:
        label_result.config(text="비밀번호가 형식에 맞지 않아요", fg="#e74c3c")
        return

    # 비밀번호 확인 검사
    input_pw2 = entry_pw2.get()
    if input_pw != input_pw2: # 비밀번호랑 확인에 입력값이 서로 다르면
        label_result.config(text="비밀번호가 일치하지 않아요", fg="#e74c3c")
        return

    # 이곳이 실행된다면 검사를 모두 통과했다고 볼 수 있다
    label_result.config(text="회원가입이 완료되었습니다", fg="#3498db")
    # return

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
    command=click_btn_reset
)
btn_reset.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

btn_signup = tk.Button(
    frame_buttons,
    text="회원가입",
    font=font_widget,
    bg="#3498db",
    fg="white",
    command=click_btn_signup
)
btn_signup.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# 결과 라벨 위젯
label_result = tk.Label(window, text="회원 가입 완료", font=font_widget)
label_result.pack(fill="x", pady=10)

#---------------------------------------------
# 화면 구동
#---------------------------------------------
window.mainloop()

