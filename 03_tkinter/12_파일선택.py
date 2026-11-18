"""
이 예제의 목표 : 파일을 사용자가 선택하도록 해서, 선택 완료시 해당 파일의 내용을 화면에 표시

(메모장st)

- 여러 줄을 입력하는 위젯은 Entry가 아니라 Text이다
- 파일을 선택하는 창은 filedialog라는 것을 사용한다
"""

import tkinter as tk
from tkinter import filedialog, messagebox

#-------------------------------------------
# 콜백 함수
#-------------------------------------------
def load_file():
    # 파일 열기 창의 결과는 "절대경로"가 나온다. 취소 혹은 x를 누르면 empty string이 나옴
    file_path = filedialog.askopenfilename(
        parent=window,
        title="불러올 파일 선택",
        filetypes=[ #불러올 파일 유형 지정
            ("텍스트 파일", "*.txt"),
            ("모든 파일", "*.*")
        ]
    )
    # print(file_path, type(file_path))
    if file_path == "":
        return

    # 파일을 열지 않는 상황을 모두 제거했으니 파일을 열어서 내용을 채워준다
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            content = file.read() # 전부다 한번에 읽기
    except Exception as e:
        # messagebox.showerror(창제목, 내용, parent=부모)
        messagebox.showerror("파일 읽기 오류", str(e), parent=window)
        return

    # 다 읽었다면 content를 Text위젯(editor)에 표시
    # editor.delete(시작위치, 종료위치)
    editor.delete("1.0", tk.END) #처음부터 끝까지
    # editor.insert(시작위치, 내용)
    editor.insert("1.0", content)

def reset_file():
    # current = editor.get("1.0", tk.END).strip()
    current = editor.get("1.0", "end-1c") #마지막 \n 빼고 불러오기
    if current == "":
        return

    answer = messagebox.askyesno(
        "삭제 확인", "내용을 지우시겠습니까?", parent=window
    )
    if answer == False:
        return

    editor.delete("1.0", tk.END)

def close_window():
    current = editor.get("1.0", "end-1c")
    if current == "":
        window.destroy()
        return

    answer = messagebox.askyesno(
        "종료 확인", "정말 종료하시겠습니까?", parent=window
    )
    if answer == False:
        return

    window.destroy() # 창 닫기

#-------------------------------------------
# 화면 배치
#-------------------------------------------
window = tk.Tk()
window.title("파일 다루기")
window.geometry("600x500")

# window의 x버튼에 대한 동작을 close_window 함수로 변경
window.protocol("WM_DELETE_WINDOW", close_window)

font_main = ("고딕", 16)

# 버튼들
frame_buttons = tk.Frame(window)
frame_buttons.pack(fill="x", pady=15)

btn_open = tk.Button(
    frame_buttons, text="파일 열기", font=font_main, command=load_file
)
btn_reset = tk.Button(
    frame_buttons, text="초기화", font=font_main, command=reset_file
)
btn_quit = tk.Button(
    frame_buttons, text="종료하기", font=font_main, command=close_window
)
# btn_open.grid(row=0, column=0)
# btn_reset.grid(row=0, column=1)
# btn_quit.grid(row=0, column=2)
btn_open.pack(side="left")
btn_reset.pack(side="left")
btn_quit.pack(side="left")

# Text 위젯 : 여러 줄을 표시하거나 작성할 수 있는 위젯
editor = tk.Text(window, font=font_main)
editor.pack(pady=10)

# 화면 구동
window.mainloop()

