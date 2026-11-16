"""
Tkinter

파이썬에서 그래픽으로 화면을 만드는 내장 라이브러리
별도 설치가 필요하지 않다.

- CUI : Character User Interface. 터미널과 같은 키보드만 이용 가능한 환경의 프로그램
- TUI : Text-based User Interface. 위아래 화살표 등으로 움직여서 선택 가능한 형태의 프로그램
- GUI : Graphical User Interface. 마우스에 기반한 그래픽 화면 요소로 프로그램을 구동
"""

# 그래픽에서 가장 기본이 되는 요소는 창(window)이다.

import tkinter as tk

# 1. 창 생성
window = tk.Tk()

# 2. 정보 설정
# (1) 창 제목
window.title("첫 번째 프로그램")

# (2) 창의 크기
window.geometry("640x480")

# (3) 크기 변경 여부를 설정
window.resizable(False, True)   # True: 전부 허용 / False: 해당값은 미허용

# (4) 창 내부 배경색 설정 (색상키워드 또는 #000000형태(hex string) 가능)
# window.configure(bg="gray")
window.configure(bg="#2c3e50")

# 3. 화면에 표시 (구동 시작)
window.mainloop()
print("프로그램 종료")

