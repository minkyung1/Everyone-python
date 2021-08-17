import turtle as t

def turn_right():   #오른쪽으로 이동하는 함수
    t.setheading(0)
    t.fd(10)

def turn_up():    #위로 이동하는 함수
    t.seth(90)
    t.fd(10)

def turn_left():   #왼쪽으로 이동하는 함수
    t.seth(180)
    t.fd(10)

def turn_down():   #아래로 이동하는 함수
    t.seth(270)
    t.fd(10)

def blank():   #화면 지우는 함수
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")   #->누르면 함수 실행
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen()

