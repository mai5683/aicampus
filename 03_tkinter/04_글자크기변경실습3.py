"""
글자크기 변경 실습
"""
import tkinter as tk
from tkinter import font

# --------------------------
# 콜백 함수들 (버튼에 연결)
# --------------------------
def click_btn_small():
    window.geometry("300x400")
    label.config(font=("Binggrae", 8))

def click_btn_normal():
    window.geometry("500x400")
    label.config(font=("Binggrae", 16))

def click_btn_large():
    window.geometry("700x400")
    label.config(font=("Binggrae", 24))

def click_btn_increase():
    # label의 현재 폰트 정보를 조회
    # 정보 확인 명령 - .cget(항목)
    font_str = label.cget("font")
    font_obj = font.Font(font=font_str) # font_str을 줄테니 글꼴 객체를 만들어라
    current_size = font_obj.actual("size") # 글꼴 객체에서 사이즈를 뽑고
    if current_size == 24:
        return
    font_obj.config(size=current_size+1) # 글꼴 객체의 사이즈만 1 증가한 값으로 교체
    label.config(font=font_obj) # 변경 완료된 글꼴 객체로 라벨 글꼴을 다시 갱신시켜라
    # print(font_obj.actual("family")) #글꼴
    # print(font_obj.actual("size")) #크기
    # print(font_obj.actual("weight")) #두께
    # print(font_obj.actual("slant")) #기울임
    # print(font_obj.actual("underline")) #밑줄

def click_btn_decrease():
    font_obj = font.Font(font=label.cget("font")) #설정된 글꼴 추출
    current_size = font_obj.actual("size") # 현재 크기
    if current_size == 8:
        return
    font_obj.config(size=current_size-1) # 크기 변경
    label.config(font=font_obj) #글꼴 재설정


# --------------------
# 화면 구성
# --------------------
window = tk.Tk()
window.title("tkinter 실습")
# window.geometry("wxh+x+y")
window.geometry("500x400")

# 라벨
label = tk.Label(
    window,
    text="tkinter는 파이썬 표준 GUI 라이브러리 입니다",
    font=("Binggrae", 16)
)
label.pack(pady=20)

# 버튼
btn_small = tk.Button(
    window, text="작게 보기", font=("Binggrae", 12),
    command=click_btn_small
)
btn_small.pack(pady=10)

btn_normal = tk.Button(
    window, text="보통 보기", font=("Binggrae", 12),
    command=click_btn_normal
)
btn_normal.pack(pady=10)

btn_large = tk.Button(
    window, text="크게 보기", font=("Binggrae", 12),
    command=click_btn_large
)
btn_large.pack(pady=10)

# (추가) +, - 버튼을 추가
btn_increase = tk.Button(
    window, text="+", font=("Binggrae", 12),
    command=click_btn_increase
)
btn_decrease = tk.Button(
    window, text="-", font=("Binggrae", 12),
    command=click_btn_decrease
)
btn_increase.pack(pady=10)
btn_decrease.pack(pady=10)

# ---------------------
# 창 구동
# ---------------------
window.mainloop()