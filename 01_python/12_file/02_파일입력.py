"""
파일 입력
- 동일하게 파일을 open()
- 모드는 r(read)를 적용
- 읽고 나서 마지막에 close() 역시 동일하게 진행
"""

file = open("hello.txt", "r", encoding="utf-8")

# 전부 다 읽기
content = file.read()

file.close()

print(content)
