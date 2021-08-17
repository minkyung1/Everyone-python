def square(a):   #a제곱 구하는 함수
    c=a*a
    return c

def triangle(a,h):   #밑변 a, 높이 h인 삼각형 넓이
    c=a*h/2
    return c

s1=4
s2=square(s1)
print(s1, s2)

print(triangle(3, 4))
