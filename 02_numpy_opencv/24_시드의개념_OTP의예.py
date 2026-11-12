# OTP의 예

import time
import random

# 지금은 1970-01-01 부터 1794447347.8938606 초 지났다.
print(time.time())
print(type(time.time()))

# 시간을 5초 동안 똑같게 만들고 싶다면 어떻게?
while True:
    sd = (int(time.time())) // 5
    # print(sd, time.time())
    random.seed(sd)
    otp = random.randrange(1, 1000000)
    print(f"OTP ={otp:06d}")    # 0 부터 6 자리까지의 숫자. d=정수 f=실수