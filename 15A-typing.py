import random
import time

#단어 리스트: 여기에 단어 추가하면 문제에 나옴
w=["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n=1  #문제 번호
print("[타자 게임] 준비되면 엔터!")
input()
start=time.time()

q=random.choice(w)
while n<=5:
    print("*문제", n)
    print(q)
    x=input()
    if q==x:
        print("통과!")
        n=n+1
        q=random.choice(w)
    else:
        print("오타! 다시 도전!")

end=time.time()
et=end-start    
et=format(et, ".2f")   #소수점 둘째 자리까지만 표시
print("타자시간:", et, "초")

        
