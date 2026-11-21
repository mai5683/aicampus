

import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# 콜백 함수
def save_bbox():
    # 현재 이미지의 크기를 구하고 그려진 상자(box)의 위치를 구해서
    # 원래 이미지일 때의 상자 위치와 크기로 바꾼 뒤
    # 텍스트로 이 정보를 저장 (목적은 인공지능 학습용)

    # 현재 이미지의 크기
    x1, y1, x2, y2 = canvas.bbox("img")
    # print(x1, y1, x2, y2)
    w = x2 - x1 # 이미지의 폭
    h = y2 - y1 # 이미지의 높이

    # screw라는 태그가 붙은 모든 객체를 가져오기
    screws = canvas.find_withtag("screw")
    # print(screws, len(screws))

    # screw=0 (정답지)
    screw_record = []
    for screw in screws:
        x1, y1, x2, y2 = canvas.bbox(screw) # screw는 그려진 고유ID
        # print("screw", x1, y1, x2, y2)
        screw_width = x2 - x1 # 나사의 폭
        screw_height = y2 - y1 # 나사의 높이
        screw_cx = (x1 + x2) / 2 # 나사의 중심x
        screw_cy = (y1 + y2) / 2 # 나사의 중심y
        # print(f"0 {screw_cx} {screw_cy} {screw_width} {screw_height}") #수치
        # 저장을 원하는건 "비율" : 0~1 사이로 변환(정규화)한 값
        screw_width = screw_width / w
        screw_height = screw_height / h
        screw_cx = screw_cx / w
        screw_cy = screw_cy / h
        # print(f"0 {screw_cx:.6f} {screw_cy:.6f} {screw_width:.6f} {screw_height:.6f}")  # 수치
        screw_record.append(f"0 {screw_cx:.6f} {screw_cy:.6f} {screw_width:.6f} {screw_height:.6f}")  # 수치

    # 구해낸 screw_record 정보를 txt로 저장
    with open("./images/screws.txt", "w", encoding="utf-8") as file:
        for screw in screw_record:
            file.write(screw)
            file.write("\n")

# 창 생성
window = tk.Tk()
window.title("이미지 그리기")
window.geometry("500x500")

# 메뉴 생성
menubar = tk.Menu(window, tearoff=False)
window.config(menu=menubar)

menu_file = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="파일", menu=menu_file)

menu_file.add_command(label="저장", command=save_bbox)

# 캔버스 배치
canvas = tk.Canvas(window, cursor="crosshair", bg="white")
canvas.pack(fill="both", expand=True)

# 캔버스에 이미지를 그린다 (Tkinter용 이미지만 가능, pillow 이용)
image_pillow = Image.open("./images/screws.jpg").convert("RGB")

# image_thumb = image_pillow.copy() # 이미지 복사
# image_thumb.thumbnail((400, 400)) # 썸네일 처리

image_thumb = ImageOps.contain(image_pillow, (400, 400)) # 최소로 채움
# image_thumb = ImageOps.fit(image_pillow, (400, 400)) # 최대로 채움

# thumbnail은 원본보다 커질 수 없지만, contain과 fit은 가능하다

image_tkinter = ImageTk.PhotoImage(image_thumb) # Tkinter용으로 변환
# 라벨은 설정하는 것이지만, 캔버스는 그려야 한다
# canvas.create_image(시작x, 시작y, image=이미지, anchor="정렬방향")
canvas.create_image(0, 0, image=image_tkinter, anchor="nw", tags="img")
# 라벨과 마찬가지로 이미지 사라짐 주의
canvas.image_thumbnail = image_tkinter # 썸네일
canvas.image_origin = image_pillow # 원본

# bbox 사각형 그리기
canvas.create_rectangle(35, 55, 70, 110, outline="yellow", width=1, tags="screw")
canvas.create_rectangle(65, 95, 100, 150, outline="yellow", width=1, tags="screw")
canvas.create_rectangle(100, 135, 135, 190, outline="yellow", width=1, tags="screw")

window.mainloop()




