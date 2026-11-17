"""
글자크기 변경 실습
"""
import tkinter as tk

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
    font = label.cget("font")
    # print(font, type(font))

    # 안좋은 방법 - 직접 손수 노가다로 처리
    current_font = font.split(" ")[0]
    current_size = int(font.split(" ")[1])
    # print(current_font, current_size)
    label.config(font=(current_font, current_size+1))

def click_btn_decrease():
    pass


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