import random

def make_question():
    a=random.randint(1,40)   #a에 1~40 사이 임의의 수 저장
    b=random.randint(1,20)
    op=random.randint(1,4)

    #문자열 변수 q에 문제 만듬
    #첫번째 숫자를 q에 저장
    q=str(a)   #a값을 문자열로 바꾸어 저장

    #연산자 추가
    if op==1:
        q=q+ "+"
    if op==2:
        q=q+ "-"
    if op==3:
        q=q+"*"
    if op==4:
        q=q+"%"

    #두번째 숫자 q에 저장
    q=q+str(b)

    #만들어진 문제 돌려줌
    return q

#정답, 오답 횟수 저장할 변수 sc1, sc2를 0으로 초기화
sc1=0
sc2=0

for x in range(5):
    q=make_question()
    print(q)
    ans=input("=")  #정답 입력 받음
    r=int(ans)

    #컴퓨터 계산 결과인 eval(q)와 입력한 결과 r비교
    if eval(q)==r:
        print("정답!")
        sc1=sc1+1
    else:
        print("오답!")
        sc2=sc2+1

print("정답:", sc1, "오답:", sc2)
if sc2==0:
    print("당신은 천재입니다!")
    
        
