# 지하철 이용요금 계산기

import tkinter as tk

#---------------------------------------
# 기초 데이터
#---------------------------------------
total = 0

#---------------------------------------
# 콜백 함수
#---------------------------------------
def click_btn_adult():
    # 외부에 있는 total이라는 값을 읽는 건 상관이 없지만 바꾸는 건 금지되어 있다.
    global total    # 내가 말하는 total은 밖에 있는 거야!
    total += (1450 + 500)
    # print("total", total)      # 정상 작동 여부 확인 시 print 사용
    label_result.config(text=f"최종 결제 금액 : {total:,}원")

def click_btn_teen():
    global total
    total += (900 + 500)
    label_result.config(text=f"최종 결제 금액 : {total:,}원")

def click_btn_child():
    global total
    total += (450 + 500)
    label_result.config(text=f"최종 결제 금액 : {total:,}원")

def click_btn_free():
    global total
    total += (0 + 500)
    label_result.config(text=f"최종 결제 금액 : {total:,}원")

# 계산 초기화 추가
def click_btn_reset():
    global total
    total = 0
    label_result.config(text=f"최종 결제 금액 : {total:,}원")

#---------------------------------------
# 화면 배치
#---------------------------------------
window = tk.Tk()
window.title("지하철 요금 계산기")
window.geometry("800x550")

# 글꼴
font_title = ("Binggrae", 24)
font_button = ("Binggrae", 20)
font_result = ("Binggrae", 24)

# 제목
label_title = tk.Label(
    window, text="지하철 매표기", font=font_title)
label_title.pack(pady=20)

# 버튼
btn_adult = tk.Button(
    window, text="성인 1매(1,450원)", font=font_button, width=20,
    command=click_btn_adult)
btn_teen = tk.Button(
    window, text="청소년 1매(900원)", font=font_button, width=20,
    command=click_btn_teen)
btn_child = tk.Button(
    window, text="어린이 1매(450원)", font=font_button, width=20,
    command=click_btn_child)
btn_free = tk.Button(
    window, text="영유아 및 어르신(0원)", font=font_button, width=20,
    command=click_btn_free)
# 초기화 추가
btn_reset = tk.Button(
    window, text="계산 초기화", font=font_button, width=20,
)



btn_adult.pack(pady=10)
btn_teen.pack(pady=10)
btn_child.pack(pady=10)
btn_free.pack(pady=10)

# 최종 금액이 나올 라벨
label_result = tk.Label(
    window, text="최종 결제 금액 : 0원", font=font_result, fg="blue"
)
label_result.pack(pady=20)

#---------------------------------------
# 화면 구동
#---------------------------------------
window.mainloop()