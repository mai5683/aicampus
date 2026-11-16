"""
실습 문제 : 물체탐지
파일명 : 42_물체탐지.py

conveyor.avi 영상을 읽어온 뒤 다음 처리를 추가하여 conveyor_detect.avi 파일로 저장하세요

grayscale
binarize
contour (find + draw)

가능하다면 텍스트 출력 명령을 찾아서 위치를 같이 이미지에 출력해보세요

동영상 속에서 움직이는 사각형을 찾아 표시 및 정보 표기
"""

import numpy as np
import cv2

# 동영상 파일 열기
# cap = cv2.VideoCapture("./videos/conveyor.avi")
# cap = cv2.VideoCapture("./videos/01_circle_horizontal.avi")
# cap = cv2.VideoCapture("./videos/02_triangle_vertical.avi")
cap = cv2.VideoCapture("./videos/03_pentagon_diagonal.avi")
# cap = cv2.VideoCapture("./videos/04_hexagon_orbit.avi")
# cap = cv2.VideoCapture("./videos/05_star_wave.avi")

if not cap.isOpened():
    print("동영상을 읽을 수 없습니다")
    exit(1)

# 동영상 정보
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
# print(width, height, fps)

if width <=0 or height <=0:
    print("동영상 정보를 읽을 수 없습니다")
    exit(1)
if fps <= 0:
    fps = 30

# 저장 도구 설정
# fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
# filename = "./videos/conveyor_detect.avi"
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
filename = "./videos/conveyor_detect.avi"
writer = cv2.VideoWriter(
    filename, fourcc, fps, (width, height), isColor=True
)

if not writer.isOpened():
    print("저장 파일에 접근할 수 없습니다")
    exit(1)

# 재생 간격 설정
delay = max(1, round(1000 / fps))

# 한 장씩 읽어서 처리 후 저장
try:
    while True:
        success, frame = cap.read()  # 한 장면 읽기
        if not success:
            break

        # 영상 처리
        result = frame.copy()
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # print("윤곽선 개수", len(contours))
        if len(contours) == 0:  # 윤곽선이 없으면 (탐지가 안 되었으면)
            continue
        # 그림은 result에 그린다.
        for contour in contours:
            # 면적으로 필터링
            area = cv2.contourArea(contour)
            print(f"면적, {area}")
            if area < 500:
                continue
            # 위치 정보 추출
            x, y, w, h = cv2.boundingRect(contour)
            # 윤곽선 그리기
            cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)
            # (추가) 좌표를 글자로 표시
            cv2. putText(result, f"({x}, {y})", (x-20, y-20),
                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )

        writer.write(result)
        cv2.imshow("before", frame)
        cv2.imshow("after", result)

        # if cv2.waitKey(delay) & 0xFF == ord('q'):
        if cv2.waitKey(delay) & 0xFF in [ord('q'), ord('Q')]:
            break
finally:
    cap.release()
    writer.release()
    cv2.destroyAllWindows()