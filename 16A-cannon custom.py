def turn_up():
    t.left(2)
	
def turn_down():
    t.right(2)

def re_set():
    t.clear()

    global target
    
    t.pensize(1)
    t.goto(-300,0)
    t.down()
    t.goto(300,0)
    
    target = random.randint(50,150)
    t.pensize(3)
    t.color("purple")
    t.up()
    t.goto(target-25,0)
    t.down()
    t.goto(target+25,0)

    t.color("black")
    t.up()
    t.goto(-200,10)
    t.setheading(20)
    
def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.fd(15)
        t.right(5)
    d = t.distance(target,0)
    t.sety(random.randint(10,100))
    if d <25:
        t.color("blue")
        t.write("Good", False, "center", ("", 15))
        t.sety(200)
        t.write("다시 시작하려면 R을 누르세요.", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("",15))
    t.color("black")
    t.goto(-200,10)
    t.setheading(ang)

print("거북이 대포 게임에 오신 것을 환영합니다.")

import turtle as t
import random

print("시작하려면 R을 눌러주세요.")

t.onkeypress(fire, "space")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(re_set, "R")

t.listen()
             
