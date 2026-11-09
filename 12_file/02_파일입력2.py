"""
파일 입력
- 동일하게 파일을 open()
- 모드는 r(read)를 적용
- 읽고 나서 마지막에 close() 역시 동일하게 진행
"""

file = open("hello.txt", "r", encoding="utf-8")

# 한 줄씩 다 읽기
# - 줄 단위로 읽을 때는 엔터를 버리면서 읽어야 한다.
# - strip()
content = file.readline().strip()
print(content)
content = file.readline().strip()
print(content)
content = file.readline().strip()
print(content)

file.close()

