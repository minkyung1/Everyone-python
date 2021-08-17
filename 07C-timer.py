import time  #시간 관련 기능 사용하고 싶다 요청

input("엔터를 누르고 20초를 셉니다.")
start = time.time()  #start 변수에 시간 저장 

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end - start  # 실제시간 et에 저장
print("실제시간:", et, "초")
print("차이:", abs(et-20), "초")  #abs는 절댓값
