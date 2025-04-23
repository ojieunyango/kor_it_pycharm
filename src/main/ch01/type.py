from multiprocessing.connection import address_type

number = 10
name ="김준일"
isOpen = False    # is는 blooean 자료형
print(number)
print(name)

print(name.index("일", 0))
print("이름: {name}, 숫자: {number}, 열림: {isOpen}" .format(name=name, number=number, isOpen=isOpen))
print(f"이름: {name}, 숫자: {number}, 열림: {isOpen}")

address = """부산 동래구 중앙대로"""

print(address)
