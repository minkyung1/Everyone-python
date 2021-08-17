import turtle as t


n=50
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(n):#밑에거를 n번 반복
    t.circle(80)   #반지름 80인 원 그림
    t.lt(360/n)    #왼쪽으로 회전
