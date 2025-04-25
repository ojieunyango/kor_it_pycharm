# python의 class 정의

class Student:
    # 파이썬은 클래스 메서드와 static 메서드를 구분했음
    # 클래스 변수(java의 static 변수)
    name = "김준일(클래스변수)"
    age = "32(클래스변수)"
    def __init__(self):    # 멤버변수 초기화
        # 인스턴스 변수
        self.name = "김준일"
        self.age = 32

    def toString(self): # 인스턴스 변수 호출 (객체를 통해서) #clsName: {self.__class__.name} 이렇게 클래스 접근해서 호출도 가능
        return f"Student(name:{self.name}, age: {self.age}, clsName: {self.__class__.name})"
    @classmethod
    def toString2(cls): # 클래스 메서드 (클래스를 통해 호출)
        return f"Student(name:{cls.name}, age: {cls.age})"

    @staticmethod
    def toString3(): # 정적 메서드 (클래스나 메서드 상관없이 호출)
        return f"Student(name: {name}, age: {age})"
# 클래스 변수 출력 (클레스 통해 접근)
print(Student.name)
print(Student.age)
# 객체 생성
s1 = Student()
# 인스턴스 변수 출력 (객체를 통해 접근)
print(s1.name)
print(s1.age)

print(s1.toString())