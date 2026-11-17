"""
그리드(grid) 화면 배치

화면을 row, column으로 나눠서 배치하는 기술

주의 : pack()과 동시에 사용할 수 없다.
      (하나의 영역에는 하나의 배치 방식만 가능하다.)
"""


import tkinter as tk

window = tk.Tk()    # 창 생성
window.title("그리드 배치")
window.geometry("600x400")

# Frame : 위젯을 담을 수 있는 영역(공간), 창 내 하나의 컨테이너
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=20)

# Frame 내부에 버튼들을 배치
btn_adult = tk.Button(
    frame_buttons,  # 프레임을 상위 요소로 둔다
    text="성인 1명")
btn_adult.grid(row=0, column=0)

btn_teen = tk.Button(
    frame_buttons,
    text="청소년 1명")
btn_teen.grid(row=0, column=1)

btn_child = tk.Button(
    frame_buttons,
    text="어린이 1명")
btn_child.grid(row=0, column=2)

btn_free = tk.Button(
    frame_buttons,
    text="영유아/어르신 1명")
btn_free.grid(row=0, column=3)

# Frame 뒤에 일반 위젯 배치
btn_calc = tk.Button(
    window,
    text="요금 계산하기"
)
btn_calc.pack(pady=20)

btn_result = tk.Label(
    window,
    text="최종 결제 요금 : ?원"
)
btn_result.pack(pady=20)


# 구동
window.mainloop()


