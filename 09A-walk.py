#random.randint(a,b) a이상 b이하 임의의 정수 뽑기

import turtle as t
import random   # random 모듈 사용하기

t.shape("turtle")
t.speed(0)

for x in range(500):   #거북이 500번 움직임
    a=random.randint(1,360)
    t.setheading(a)    #a각도로 돌림
    t.forward(10)
                     
                
