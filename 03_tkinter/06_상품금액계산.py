import tkinter as tk


def click_btn_save():
    sell = entry_sell.get().strip()
    buy = entry_buy.get().strip()
    if sell == "" or buy == "":
        label_result.config(text="금액과 수량을 모두 정확히 입력하세요", fg="red")
    elif not sell.isdigit() or not buy.isdigit():
        label_result.config(text="금액과 수량을 모두 정확히 입력하세요", fg="red")
    else:
        sell = int(sell)
        buy = int(buy)
        total = sell * buy
        label_result.config(text=f"최종 구매 금액 : {total:,}원", fg="blue")

window = tk.Tk()
window.title("상품금액계산")
window.geometry("500x400")

# 입력창
title1 = tk.Label(
    window,
    text="판매 금액을 입력하세요",
    font=("Binggrae", 18)
)
title1.pack(pady=10)

entry_sell = tk.Entry(
    window,
    font=("Binggrae", 18)
)
entry_sell.pack(pady=8)

title2 = tk.Label(
    window,
    text="구매 수량을 입력하세요",
    font=("Binggrae", 18)
)
title2.pack(pady=10)

entry_buy = tk.Entry(
    window,
    font=("Binggrae", 18)
)
entry_buy.pack(pady=8)


# 설정버튼
btn_save = tk.Button(
    window, text="계산", font=("Binggrae", 16),
    command=click_btn_save
)
btn_save.pack(pady=10)


label_result = tk.Label(
    window, text="", font=("Binggrae", 16),
)
label_result.pack(pady=10)



window.mainloop()