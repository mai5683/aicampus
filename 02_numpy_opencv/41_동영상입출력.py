"""
동영상(video) 입출력

동영상 입력과 웹캠 입력은 동일한 코드를 사용한다.
"""

import cv2
import numpy as np

# 동영상 파일 열기
cap = cv2.VideoCapture("./videos/conveyor.avi")

# 정상적으로 열리지 않은 경우를 제거
if not cap.isOpened():
    print("동영상을 읽을 수 없습니다")
    exit(1)

# 동영상의 정보를 가져온다. - cap.get(항목)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 화면 너비
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 화면 높이
print(cap.get(cv2.CAP_PROP_FPS))            # 1초당 재생되는 장면 수

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
if fps <= 0:    # 못 읽으면
    fps = 20    # 기본값 20

print(f"크기 {width}x{height}, {fps} fps")

# 재생 간격을 계산
# - fps의 값에 맞게 재생간격을 계산 (밀리초, ms)
# - (ex) 20 fps면 1초에 20장을 보여줘야 하니까 한 장당 0.05초 (50밀리초, 50ms)
# - (ex) 30 fps면 1초에 30장을 보여줘야 하니까 한 장당 0.0333초 (33밀리초, 33ms)
# - (ex) 60 fps면 1초에 60장을 보여줘야 하니까 한 장당 0.0166초 (16밀리초, 16ms)

# fps에 따라 멈춰야 할 간격 계산
delay = max(1, round(1000 / fps))

while True:
    # 장면 하나를 읽어 온다
    # - 이미지는 imread() 이지만, 영상은 read() 이다.
    # - 이미지만 나오는 게 아니라 성공/실패가 나온다. (연속적으로 읽는 상황이므로)
    # image = cv2.imread("경로")
    success, frame = cap.read()
    if not success:    # 영상 끝 or 읽기 실패 (영상이 깨진 경우)
        break

    # 처리할 거 있으면 하고
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 화면에 표시
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)

    # 지정된 딜레이 만큼 대기
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# 나왔으면 정리
cap.release()
cv2.destroyAllWindows()