"""
윤곽선(contours) 탐지
"""

import numpy as np
import cv2

# 이미지 생성
image = np.zeros((500, 600, 3), dtype=np.uint8)

# 도형 그리기
# 사각형 : cv2.rectangle(이미지, 시작점, 끝점, 색상, 두께)
cv2.rectangle(image, (50, 50), (250, 250), (255, 255, 255), -1)
# 원 : cv2.circle(이미지, 중심점, 반지름, 색상, 두께)
cv2.circle(image, (400, 300), 100, (255, 255, 255), -1)
cv2.circle(image, (400, 300), 50, (0, 0, 0), -1)   # 도넛 만들기 (중심점은 같으니 반지름, 색상만 변경)

# 전처리(grayscale → binarize(이진화))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 윤곽선 추출
# 명령 : cv2.findContours(이미지, 윤곽선 인식범위, 윤곽선 좌표처리방식)
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,      # 가장 바깥 윤곽선만 찾는 모드
    # cv2.RETR_TREE,        # 모든 윤곽선을 계층구조로 찾는 모드
    cv2.CHAIN_APPROX_SIMPLE
)
print("검출된 윤곽선 수 :", len(contours))

# 이미지 사본 생성
result = image.copy()

# 감지한 정보를 가지고 무엇을 할 것인가?
# - 윤곽선 별로 분석을 해서 정보를 얻어내거나 표시를 하거나...
for contour in contours:
    print("<윤곽선 분석 정보>")
    # 면적
    area = cv2.contourArea(contour)
    # if area < 40000:
    #     continue
    print("면적 :", area)

    # 둘레
    perimeter = cv2.arcLength(contour, True)    # 둘레가 닫혀 있으면 True, 열려 있으면 False
    print("둘레 :", perimeter)

    # 감지영역 표시 (감싸는 사각형)
    x, y, w, h = cv2.boundingRect(contour)
    print("감싸는 사각형 :", x, y, w, h)

    # 중심좌표
    # - moments 계산 (물체의 면적분포를 표현한 값)
    m = cv2.moments(contour)

    # m10 - x좌표의 모멘트(면적분포)
    # m01 - y좌표의 모멘트(면적분포)
    # m00 - 윤곽선의 면적
    if m["m00"] != 0:
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
    else:
        # 만약 m00이 0이어서 중심 계산이 불가능하다면
        cx = x + w // 2
        cy = y + h // 2
    print("중심좌표 :", cx, cy)

    # 위와 같은 정보들을 다 추출했다면
    # (1) 시각적으로 표시
    # (2) CSV에 저장

    # 윤곽선 표시
    # cv2.drawContours(사본이미지, [contour], -1, 색상, 두께)
    # -1은 전달된 윤곽선을 모두 그리라는 뜻
    cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)

    # 감싸는 사각형 (바운딩 박스) 표시
    # cv2.rectangle(result, 시작점, 끝점, 색상, 두께)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # 중심 표시
    cv2.circle(result, (cx, cy), 5, (0, 0, 255), -1)

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

