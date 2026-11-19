"""
파일 선택창을 열고 이미지를 선택하여 불러와 표시하는 문제
"""
import tkinter as tk

#-----------------------------------------
# 콜백 함수
#-----------------------------------------



#-----------------------------------------
# 화면 배치
#-----------------------------------------

# 글꼴 설정
font_main = ("Binggrae", 16)

# 창 생성
window = tk.Tk()
window.title("이미지 불러오기 문제")
window.geometry("500x500")

# 버튼들 배치
frame_btns = tk.Frame(window)
frame_btns.pack(pady=10, fill="x")
frame_btns.columnconfigure(0, weight=1, uniform="same")
frame_btns.columnconfigure(1, weight=1, uniform="same")
frame_btns.columnconfigure(2, weight=1, uniform="same")

btn_open = tk.Button(
    frame_btns, text="이미지 열기", font=font_main, command=None
)
btn_reset = tk.Button(
    frame_btns, text="초기화", font=font_main, command=None
)
btn_close = tk.Button(
    frame_btns, text="종료", font=font_main, command=None
)

btn_open.grid(row=0, column=0, sticky="nsew", padx=10)
btn_reset.grid(row=0, column=1, sticky="nsew", padx=(0, 0))
btn_close.grid(row=0, column=2, sticky="nsew", padx=10)

# 선택된 파일 위치를 표시할 라벨
label_path = tk.Label(
    window, text="현재 이미지 : 없음",
    font=font_main,
    anchor="w"
)
label_path.pack(padx=10, pady=10, fill="x")

# 이미지를 미리보기 하기 위한 라벨
label_preview = tk.Label(window, bg="white")
label_preview.pack(padx=10, pady=10, fill="both", expand=True)

#-----------------------------------------
# 화면 구동
#-----------------------------------------
window.mainloop()