def fx1():
    print("함수1 호출")

fx1()
# 변수에 함수를 담는 방법 , 자바에선 안됨
fx2 = fx1
print(id(fx1)) # 주소값쓸때 id함수 씀
print(id(fx2))
fx2()

# 콜백 함수
def fx3(data):
    print("함수3 호출")
    return f"{data} 처리완료"

def fx3_2(data):
    print("함수3-2 호출")
    return f"{data} 처리실패"

def fx4(callbackFx):
    print("함수4 호출")
    print(callbackFx("새로운 데이터"))
    print("함수4 호출 끝")
fx4(fx3)
fx4(fx3_1)
fx4(fx3_2)