import tkinter as tk

window = tk.Tk()
window.title("지하철 요금 계산기")
window.geometry("500x400")

main_font = ("Binggrae", 17)

card = 500
total = card

def click_btn_adult():
    global card
    card += 1450
def click_btn_youth():
    global youth
def click_btn_child():
    global child
def click_btn_kid_elder():
    global kid_elder

btn_adult = tk.Button(window, text="성인 1매 (1,450원)", font=main_font,
                      command=click_btn_adult)
btn_adult.pack(pady=10)

btn_youth = tk.Button(window, text="청소년 1매 (900원)", font=main_font,
                      command=click_btn_youth)
btn_youth.pack(pady=10)

btn_child = tk.Button(window, text="어린이 1매 (450원)", font=main_font,
                      command=click_btn_child)
btn_child.pack(pady=10)

btn_kid_elder = tk.Button(window, text="영유아 및 어르신 (0원)", font=main_font,
                      command=click_btn_kid_elder)
btn_kid_elder.pack(pady=10)


label_result = tk.Label(
    window, text="", font=main_font)
label_result.pack(pady=10)

total = int(card+adult+youth+child+kid_elder)
label_result.config(text=f"최종 결제 금액 : {total}원 (카드 보증금 포함)")

window.mainloop()