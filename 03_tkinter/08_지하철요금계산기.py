

import tkinter as tk

#-------------------------------
# 콜백 함수
#-------------------------------
def calculate():
    try:
        # 모든 입력창의 값을 불러 와서 합계를 계산한 뒤에 라벨에 출력 (문제가 생기면 오류 표시)
        # adult_str = entry_adult.get().strip()
        # if adult_str == "":
        #     adult_str = 0
        # adult = int(adult_str)        → 이 4줄의 코드를 아래 1줄 코드로 바꿀 수 있다.
        adult = int(entry_adult.get().strip() or 0)  # 비어 있으면 or 뒤의 값이 적용  / or 은 플랜B 값이라고 보면 됨
        teen = int(entry_teen.get().strip() or 0)
        child = int(entry_child.get().strip() or 0)
        free = int(entry_free.get().strip() or 0)
        if adult < 0 or teen < 0 or child < 0:
            raise Exception

        adult_price = adult * (1450 + 500)
        teen_price = teen * (900 + 500)
        child_price = child * (450 + 500)
        free_price = free * 500

        total = adult_price + teen_price + child_price + free_price
        label_result.config(text=f"최종 결제 금액 : {total}원", fg="blue")

    except Exception:
        label_result.config(text=f"올바른 인원수를 입력하세요")

# (추가) 초기화 버튼 함수
def entry_reset():
    # entry_adult.config(text="")   # 작동 안 됨
    entry_adult.delete(0, tk.END)   # 가능
    entry_teen.delete(0, tk.END)
    entry_child.delete(0, tk.END)
    entry_free.delete(0, tk.END)

#-------------------------------
# 화면 배치
#-------------------------------
window = tk.Tk()
window.title("지하철 요금 계산기")
window.geometry("600x700")

font_main = ("Binggrae", 16)

# label_adult_entry = tk.Label()
# label_adult_entry.pack(pady=10)
tk.Label(window, text="성인 인원 수", font=font_main).pack(pady=10)
entry_adult= tk.Entry(window, font=font_main)
entry_adult.pack(pady=10)

tk.Label(window, text="청소년 인원 수", font=font_main).pack(pady=10)
entry_teen = tk.Entry(window, font=font_main)
entry_teen.pack(pady=10)

tk.Label(window, text="어린이 인원 수", font=font_main).pack(pady=10)
entry_child = tk.Entry(window, font=font_main)
entry_child.pack(pady=10)

tk.Label(window, text="무료 인원 수", font=font_main).pack(pady=10)
entry_free = tk.Entry(window, font=font_main)
entry_free.pack(pady=10)

# 계산 버튼
tk.Button(window, text="금액 계산", font=font_main, command=calculate).pack(pady=20)

# (추가) 초기화 버튼
tk.Button(window, text="모두 지우기", font=font_main, command=entry_reset).pack(pady=20)

# 최종 결과 표시 라벨
label_result = tk.Label(window, text="테스트문장", font=font_main)
label_result.pack(pady=10)

#-------------------------------
# 화면 구동
#-------------------------------
window.mainloop()