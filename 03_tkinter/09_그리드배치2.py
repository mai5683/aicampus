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
# - Frame은 내부 위젯의 크기 만큼 자동으로 증가한다.
# - pack()으로 배치할 때 가로를 꽉 채우고 싶다면 fill="x" 옵션을 설정
frame_buttons = tk.Frame(window, bg="yellow")
frame_buttons.pack(pady=10, fill="x")

# - frame 내부에 grid를 배치할 때 사용할 폭의 설정을 따로 해줘야 한다.
# - frame_buttons.columnconfigure(위치, 가중치, 그룹명)
# - 위치 : 0부터 시작하는 순서
# - 가중치 : 남는 공간을 얼만큼의 비율로 차지할 것인가
# - 그룹명 : 같은 공간 비율을 유지시킬 것인가 (같은 그룹은 공간을 동일하게 나눠 가진다.)
frame_buttons.columnconfigure(0, weight=1, uniform="same")
frame_buttons.columnconfigure(1, weight=1, uniform="same")
frame_buttons.columnconfigure(2, weight=1, uniform="same")
frame_buttons.columnconfigure(3, weight=1, uniform="same")

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

# 배치 코드
# - grid 배치에서 sticky 옵션에 값을 설정하면 영역을 어떻게 채울지 설정할 수 있다.
# - n(north), s(south), e(east), w(west)
btn_adult.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
btn_teen.grid(row=0, column=1, sticky="nsew")
btn_child.grid(row=0, column=2, sticky="nsew")
btn_free.grid(row=0, column=3, sticky="nsew")

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


