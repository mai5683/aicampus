

import tkinter as tk

#-------------------------------
# 콜백 함수
#-------------------------------
def click_btn_calc():
    try:
        # 1. 금액 입력창의 입력값을 가져온다
        price = int(entry_price.get())
        if price <= 0:
            raise Exception
        # 2. 수량 입력창의 입력값을 가져온다
        qty = int(entry_qty.get())
        if qty <= 0:
            raise Exception
        # 3. 둘을 곱한다
        result = price * qty
        # 4. 결과 라벨에 값을 표시한다
        label_result.config(text=f"최종 구매 금액 : {result:,}원", fg="#3498db")
    except Exception:
        label_result.config(text="금액 또는 수량을 정확하게 입력하세요", fg="#e74c3c")

#-------------------------------
# 화면 배치
#-------------------------------
window = tk.Tk()
window.title("상품 금액 계산")
window.geometry("500x400")

main_font = ("Binggrae", 20)

# 상품금액 입력 위젯
label_price = tk.Label(window, text="상품 금액을 입력하세요", font=main_font)
label_price.pack(pady=10)
entry_price = tk.Entry(window, font=main_font)
entry_price.pack(pady=10)

# 구매수량 입력 위젯
label_qty = tk.Label(window, text="구매 수량을 입력하세요", font=main_font)
label_qty.pack(pady=10)
entry_qty = tk.Entry(window, font=main_font)
entry_qty.pack(pady=10)

# 계산 버튼
btn_calc = tk.Button(window, text="계산", font=main_font, command=click_btn_calc)
btn_calc.pack(pady=10)

# 결과 라벨
label_result = tk.Label(window, font=main_font)
label_result.pack(pady=10)

#-------------------------------
# 화면 구동
#-------------------------------
window.mainloop()