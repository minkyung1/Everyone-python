import random

n=random.randint(1,30)

while True:     #영원히 반복
    x=input("맞혀 보세요?")
    g=int(x)
    if g==n:
        print("정답")
        break  # 정답이면 while 반복 블록 빠져 나감
    if g<n:
        print("너무 작아요.")
    if g>n:
        print("너무 커요.")
        
