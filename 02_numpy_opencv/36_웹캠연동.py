"""
웹캠에서 이미지 한 장을 읽어서 출력하는 코드

- 웹캠이 설치되어 있어야함
- 웹캠이 없으면 DroidCam과 같은 가상 웹캠 연결 필요
- 웹캠이 여러개면 웹캠 번호가 다를 수 있음
"""

import cv2

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

# 화면 한 장(1프레임) 읽기
success, frame = cap.read()

if success: #읽기 성공
    print("프레임 읽기 성공")

    cv2.imshow("frame", frame)
    cv2.waitKey(0)
else: #읽기 실패
    print("프레임 읽기 실패")

# 웹캠에 대한 점유 해제
cap.release()
cv2.destroyAllWindows()



