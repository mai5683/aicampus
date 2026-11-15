"""
웹캠에서 이미지를 계속 읽어서 출력하는 코드

- 웹캠이 설치되어 있어야함
- 웹캠이 없으면 DroidCam과 같은 가상 웹캠 연결 필요
- 웹캠이 여러개면 웹캠 번호가 다를 수 있음
"""

import cv2
import numpy as np

# 웹캠 연결
# cv2.VideoCapture(웹캠접속주소)
# 웹캠접속주소는 휴대폰마다 다릅니다.
# http://192.168.0.xx:4747/video 형태입니다.
# (xx가 휴대폰마다 다릅니다)

cap = cv2.VideoCapture("http://192.168.0.39:4747/video")
# print(cap.isOpened())
# if cap.isOpened() == False:
if not cap.isOpened():
    print("카메라가 없어요")
    exit(1)

print("카메라가 연결되었습니다")

while True:
    # 화면 한장(1프레임) 읽기
    success, frame = cap.read()

    # 실패하면 반복 탈출
    if not success:
        print("프레임 읽기 실패")
        break

    # 전처리
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((9,9), dtype=np.uint8)
    morph = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    edge = cv2.Canny(morph, 50, 150)

    contours, _h = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = frame.copy()
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # 실패하지 않았다면
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("blur", blur)
    cv2.imshow("binary", binary)
    cv2.imshow("morph", morph)
    cv2.imshow("edge", edge)
    cv2.imshow("result", result)

    # 1ms초 동안 기다려 (q를 입력했는지 확인해)
    # `& 0xFF` 하위 8비트만 추출하는 코드
    # `ord('q')`는 글자 q를 숫자로 바꾸는 코드 (=113)
    # (정리) 1ms 안에 입력이 발생했는데 마침 q면 나가라
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 웹캠에 대한 점유 해제
cap.release()
cv2.destroyAllWindows()



