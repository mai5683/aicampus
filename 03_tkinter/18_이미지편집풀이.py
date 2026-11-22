"""
# 이미지를 편집할 수 있는 프로그램을 개발하세요.

# 메뉴의 형태

[파일]
+- 이미지 열기 (Ctrl+O)
+- 최근 열어본 이미지 +-  이미지1
                   +-  이미지2
+- 이미지 저장 (Ctrl+S)
+- 이미지 초기화 (Ctrl+R)
+- 프로그램 종료 (Alt+F4)

[편집]
+- 흑백 변환 (F1)
+- 이진화 (F2)
+- 블러 (F3)
+- 모폴로지 (F4)
+- 캐니 (F5)
+- 되돌리기(undo) (F6)

<기능 설명>
- 최근 열어본 이미지 : 이미지를 열 때마다 기록을 남겨 최신순으로 출력
- 되돌리기 : 이미지 변경이 있을 때마다 직전 이미지를 기록에 추가하여 관리하고 되돌리도록 처리
- 열기, 초기화, 종료 시 이미지가 존재한다면 저장할지 물어보고 결정하기
- 창의 크기가 변경되면 그에 맞게 이미지가 바뀌도록 처리
- 이미지 파일이 선택되었을 때만 편집 메뉴들이 활성화되도록 처리
"""


import tkinter as tk


#---------------------------------------------------------------------
# 화면 배치
#---------------------------------------------------------------------
window = tk.Tk()
window.title("이미지 편집기 v0.1")
window.geometry("500x500")

viewer = tk.Label(window, bg="white")
viewer.pack(fill="both", expand=True)
viewer.image_thumbnail = None    # 썸네일로 표시되는 이미지를 붙잡아 두기 위해
viewer.image_origin = None       # 원본 이미지를 붙잡아 두기 위해


#---------------------------------------------------------------------
# 메뉴 배치
#---------------------------------------------------------------------
menubar = tk.Menu(window)     # 메뉴바
menu_file = tk.Menu(menubar, tearoff=False)    # 파일 메뉴
menu_edit = tk.Menu(menubar, tearoff=False)    # 편집 메뉴

window.config(menu=menubar)    # 창에 메뉴바 설정
menubar.add_cascade(label="파일", menu=menu_file)    # 메뉴바에 파일 메뉴 추가
menubar.add_cascade(label="편집", menu=menu_edit)    # 메뉴바에 편집 메뉴 추가

menu_file.add_command(label="이미지 열기", command=open_image)
menu_file.add_command(label="이미지 저장", command=None)
menu_file.add_command(label="이미지 초기화", command=None)
menu_file.add_separator()
menu_file.add_command(label="프로그램 종료", command=None)

menu_edit.add_command(label="흑백 변환", command=None)
menu_edit.add_command(label="이진화", command=None)
menu_edit.add_command(label="블러", command=None)
menu_edit.add_command(label="모폴로지", command=None)
menu_edit.add_command(label="캐니", command=None)


#---------------------------------------------------------------------
# 화면 구동
#---------------------------------------------------------------------
window.mainloop()


