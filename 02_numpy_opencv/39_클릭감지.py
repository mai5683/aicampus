"""
이미지를 표시하고 클릭하면 해당 지점의 좌표가 표시되도록 처리

[클릭] ---------> 함수 실행

위 로직을 예약작업으로 등록해 두어야 한다.
이걸 "이벤트 핸들링(event handling)"이라고 부른다.
"""

import cv2

# 이미지 입력
image = cv2.imread("./images/tilted.png")
if image is None:
    print("이미지 없음")
    exit(1)

image = cv2.resize(image, (800, 600))

# 마우스 동작이 발생할 떄 호출할 함수 (형태가 정해져 있음)
def mouse_event(event, x, y, flags, param):
    # print("마우스 이벤트 발생")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스클릭", x, y)

# 내가 함수를 호출하는 게 아니라 opencv에게 불러달라고 "예약"해야 함.
# → 콜백(callback) 함수
cv2.namedWindow("image")   # 창에 대한 내부적인 이름
cv2.setMouseCallback("image", mouse_event)

# 이미지 출력
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

