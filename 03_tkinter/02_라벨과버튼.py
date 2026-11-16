"""
Tkinter의 라벨과 버튼

창을 생성했다면 내부에 위젯(widget)을 배치해야 한다.

Label : 글자 또는 이미지를 표시하는 위젯
Button : 클릭하면 함수를 실행하는 위젯

위젯 생성 → 옵션 설정 → 배치
"""

import tkinter as tk

#---------------------------------------------------------------
# btn_kor을 눌렀을 때 실행할 함수
# - 누르면 label의 글자를 "안녕"이라고 바꿀 예정
# - config로 이미 만든 대상의 정보를 변경할 수 있다.
# - 이렇게 만든 함수를 버튼의 command 속성에 연결해 두면 알아서 실행된다.
#---------------------------------------------------------------
def click_btn_kor():
    label.config(text="안녕~")
    # print("안녕~")

#---------------------------------------------------------------
# btn_eng를 눌렀을 때 실행할 함수
#---------------------------------------------------------------
def click_btn_eng():
    label.config(text="Hello~")

# 창 생성
window = tk.Tk()
window.title("Label 그리고 Button")
window.geometry("500x300")

# 창에 위젯을 배치하는 코드
# - 생성한 이후에 pack() 명령을 호출해야 창에 배치됨
# - pakc()을 하면서 옵션으로 여백을 지정할 수 있다.
label = tk.Label(
    window,     # 소속 (부모, 상위위젯 또는 창)
    text= "버튼을 눌러 보세요"   # 표시될 글자
)
label.pack(pady=20)     # pady : 줄 간격

btn_kor = tk.Button(
    window,
    text= "한국어",
    command=click_btn_kor   # 이 버튼이 작동하면 click_btn_kor을 실행해라. (콜백함수)
)
btn_kor.pack(pady=10)

btn_eng = tk.Button(
    window,
    text= "English",
    command=click_btn_eng
)
btn_eng.pack(pady=10)

# 모든 준비를 마쳤다면 창을 표시
window.mainloop()

