import turtle as t


n=5
t.color("blue")
t.fillcolor("skyblue")
t.begin_fill()
for x in range(n):
    t.fd(50)
    t.lt(360/n)
t.end_fill()
