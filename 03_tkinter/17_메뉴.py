"""
메뉴 만들기

메뉴는 창에 붙어있는 선택 가능한 위젯을 말합니다.
접혀 있을 수도 있고, 아닐 수도 있습니다.
"""

import tkinter as tk

#-------------------------------------
# 콜백 함수들
#-------------------------------------
# - 만약 command와 bind에서 같은 함수를 쓰고 싶다면 event 정보를 선택적으로 넣을 수 있어야 한다
def new_file(event=None):
    print("새파일 기능 실행")
def open_file(event=None):
    print("파일 열기 실행")
def save_file(event=None):
    print("파일 저장 실행")
def close_window(event=None):
    # print("프로그램 종료")
    window.destroy()

#-------------------------------------
# 창 생성
#-------------------------------------
window = tk.Tk()
window.title("메뉴 배우기")
window.geometry("600x400")

#-------------------------------------
# 메뉴 생성
#-------------------------------------

# font_menu = ("Binggrae", 12, "bold")
font_menu = ("Binggrae", 12)

# 창 ← 메뉴바 ← 메뉴 ← ...
menubar = tk.Menu(window, font=font_menu)

# 파일 메뉴 (tearoff가 True면 메뉴가 분리될 수 있다는 뜻. window에서는 오작동 가능성이 있음)
menu_file = tk.Menu(menubar, tearoff=False, font=font_menu)

# 실행 가능한 하위 메뉴를 추가
# - .add_command()
# - 단축키를 설정하고 싶다면 accelerator로 표시할 글자를 적고, window에 bind를 해야한다
# 구분선 - .add_seperator()
menu_file.add_command(label="새 파일", command=new_file, accelerator="Ctrl+N")
menu_file.add_separator()
menu_file.add_command(label="파일 열기", command=open_file, accelerator="Ctrl+O")
menu_file.add_command(label="파일 저장", command=save_file, accelerator="Ctrl+S")
menu_file.add_separator()
menu_file.add_command(label="프로그램 종료", command=close_window, accelerator="Alt+F4")

# 편집 메뉴
menu_edit = tk.Menu(menubar, tearoff=False, font=font_menu)

# 보기 메뉴
menu_view = tk.Menu(menubar, tearoff=False, font=font_menu)

# 메뉴바에 메뉴 설정
# menubar.add_cascade(label="보여줄글자", menu=적용시킬메뉴)
menubar.add_cascade(label="파일", menu=menu_file)
menubar.add_cascade(label="편집", menu=menu_edit)
menubar.add_cascade(label="보기", menu=menu_view)
# 창에 메뉴바 설정
window.config(menu=menubar)

# 메뉴 단축키들을 실제로 바인딩(연결) 설정
window.bind("<Control-n>", new_file)
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
# window.bind("<Alt-F4>", close_window)
window.protocol("WM_DELETE_WINDOW", close_window) #ALT+F4의 처리

#-------------------------------------
# 창 구동
#-------------------------------------
window.mainloop()