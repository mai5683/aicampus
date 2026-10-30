"""
누적합계

1씩 증가하는 카운트와 달리 어떤 값이 계속 더해지는 상황
"""

# (ex) 10을 10번 더하면 얼마인가요?
# total  = 10+10+10+10+10+10+10+10+10+10

total = 0

for i in range(10) :
    total += 10

print("합계 :", total)

print()
# (Q) 1부터 100까지 더해서 출력
# total = 1+2+3+4+...+98+99+100

total = 0
for i in range(1, 101) :
    total += i

print("1부터 100까지 합계 :", total)