"""
Tkinter의 입력창

Entry 위젯을 이용하여 한 줄 짜리 입력을 받을 수 있다.
"""

# 목표 : 닉네임 입력 후 확인을 누르면 "000님 환영합니다!"를 출력하는 화면

import tkinter as tk

#------------------------------------------
# 콜백 함수
#------------------------------------------
def click_btn_save():
    text = nickname_entry.get()         # 닉네임 엔트리에 입력된 글자를 가져 와서
    text = text.strip()                 # 앞뒤 불필요한 공백 없애주고
    if len(text) == 0:                  # 입력한 글자가 없을 때는
        label_result.config(text="닉네임을 작성하세요")
    else:                               # 입력한 글자가 있을 때는
        text += "님 환영합니다!"          # 그 뒤에 "님 환영합니다"를 추가하고
        label_result.config(text=text, fg="blue")    # 결과를 라벨에 표시

#------------------------------------------
# 화면 배치
#------------------------------------------
window = tk.Tk()
window.title("입력 위젯 배우기")
window.geometry("500x400")

# 제목 라벨
title = tk.Label(
    window,
    text="닉네임을 설정하세요",
    font=("Binggrae", 24)
)
title.pack(pady=20)

# 입력창
nickname_entry = tk.Entry(
    window,
    font=("Binggrae", 20),
    justify="center",   # 좌(left), 중(center), 우(right)
)
nickname_entry.pack(pady=10, ipady=10)

# 설정 버튼
btn_save = tk.Button(
    window, text="저장", command=click_btn_save
)
btn_save.pack(pady=10)

# 결과 표시 라벨
label_result = tk.Label(
    window, text="", font=("Binggrae", 20)
)
label_result.pack(pady=20)

#------------------------------------------
# 화면 구동
#------------------------------------------
window.mainloop()