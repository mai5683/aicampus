"""
Tkinter의 이미지 처리 방법

label이나 button 등에 image라는 속성이 있다.
여기에 이미지를 불러 와서 설정해 주면 표시된다.

이미지를 원본 크기 그대로만 쓰면 문제가 없는데...
이미지를 편집(크기변경, 썸네일 추출 등)하려면 별도의 도구가 필요하다.

[Pillow]
이미지 읽기, 크기 조절 등을 지원하는 라이브러리
설치 명령 : pip install pillow
"""

import tkinter as tk


# 창 배치
window = tk.Tk()
window.title("이미지 원본 표시")
window.geometry("500x500")

# 이미지 읽기
# Tkinter의 기본명령을 사용하며 .png, .gif 등을 읽을 수 있지만 .jpg(.jpeg)는 읽을 수 없다.
pet = tk.PhotoImage(file="./images/banana.png")

label_viewer = tk.Label(window, image=pet)
label_viewer.pack(fill="both", expand=True)

# 창 구동
window.mainloop()

