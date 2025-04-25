# 여러값 return
def fx1():
    return ["함수1", "함수2", "함수3"] # 튜플이 됨, 튜플 안하고 싶으면 [] 괄호하기

r1, r2, r3 = fx1()
print(r1, r2, r3)

r4, r5, r6 = "함수4", "함수5", "함수6" # 리스트가 됨
print(r4, r6, r5)

r7 = "함수7", "함수8" # 튜플이 됨
print(r7)

# 기본값 매개변수
def fx2(name ="익명", membershipType="일반회원"):  # 매개변수에 디폴트값 넣을수있음 이제 값안넣어도 일반회원 뜸, 단 맨뒤로 가야함 -
    return {
        "회원등급": membershipType,
        "이름": name
    }
member1 = fx2( "김준일")
print(member1)
member2 = fx2()
print(member2)
memebr3 = fx2("김준삼", "골드회원")
print(memebr3)

# 키워드 매개변수(인자) -> 내가 어떤 매개변수에 값을 전달할지 명시
def fx3(name, membershipType, address, phone, startDate):
    return  {
        "회원등급": membershipType,
        "이름": name
    }
# 매번 순서에 맞춰 쓰지않아도 직접명시해주면됨, 하지만 다른 회원들도 매번 다 써줘야함, 디폴트는 안적어도 됨
member4 = fx3("김준사", "VIP","주소","번호","날짜")
member4 = fx3(phone= "번호", name="이름", startDate="날짜", address="주소", membershipType="일반회원")

# 가변 인자 *args 변수명 매개변수, ** kwargs 여러개받을수있는 매개변수
def fx4(*aa):
    print(aa)

fx4(1,2,3,4,5,6,7) # 튜플로 전달됨

def fx5(*aa, bb):
    print(f"aa: {aa}")
    print(f"bb: {bb}")

fx5(9,8,9,4,5,6, bb= 90) # 가변인자가 우선순위여서 다들어가기때문에 나머지 매개변수는 명시를 해줘야함

def fx6(address, **cc):
        print(f"cc: {cc}")
        print(f"address: {address}")
# **는 딕셔너리가 됨 그리고 앞에 출력됨
fx6(address="주소", name= "jenny", age= 32)

"""
매개변수 순서 요약
1. 일반 인자 (아무것도없는 매개변수): 제일 앞
2. 기본값이 있는 인자 : 두번째
3. *args 가변인자 : 세번째
4. 키워드를 명시한 경우 : 네번쨰 ex) address="주소"
5. **kwargs 이건 제일 뒤에
"""

def fx(a, b = 0, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")


