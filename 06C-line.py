import turtle as t


angle=89
t.bgcolor("yellow")
t.color("black")
t.speed(0)
for x in range(200):   #0부터 199까지 실행
    t.fd(x)            #x만큼 전진
    t.lt(angle)        #저 값만큼 회전
