"""
파일 입력
- 동일하게 파일을 open()
- 모드는 r(read)를 적용
- 읽고 나서 마지막에 close() 역시 동일하게 진행
"""

file = open("hello.txt", "r", encoding="utf-8")

# 한 번에 모든 줄을 다 읽기
lines = file.readlines()

file.close()

# print(type(lines))
for line in lines:
    print(line.strip())
