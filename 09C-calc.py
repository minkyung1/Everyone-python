import random

a=random.randint(1,30)
b=random.randint(1,30)

print(a, "+", b, "=")
x=input()  #답 입력받아 x에 저장(문자열)
c=int(x)   #비교 위해 정수로 바꿔 c에 저장

if a+b==c:
    print("천재!")
else:
    print("바보?")
