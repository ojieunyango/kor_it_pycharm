print("모듈 1번 파일 실행")
print(__name__)
name = "김준일"

def add(n1, n2):
    return n1 + n2

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    if __name__ == "__main__":
        print("모듈1번파일 실행")
        print(name)
        print(add(10,20))
        print(Student("김준일", 32)) 