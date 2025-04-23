# 딕셔너리 선언


studentDict= dict()
studentDict= {
    "name": "심민호",
    "age": 25
}
print(studentDict)
# 딕셔너리 값 추가
studentDict["address"] = "부산"
print(studentDict)

anyList = []
anyList.append("test") # 아예 빈공간이기때문에 추가할려면 append를 써야함
print(anyList)

# 딕셔너리 값 조회

name = studentDict.get("name")
print(name)

print(studentDict["name"]) # 대괄호 써서 직접접근도 가능함

name = studentDict["name"]
print(name)

address = studentDict["address"]
print(address)

# 딕셔너리 값 수정
studentDict["address"] = "서울"
print(studentDict)

# 딕셔너리 값 삭제
del studentDict["age"]
print(studentDict)
studentDict.pop("name")
print(studentDict)

# 딕셔너리의 키, 값 한쌍 -> 아이템
studentDict["name"] = "james"
print(studentDict.items())
print(list(studentDict.items())[0])
key, value = list(studentDict.items())[0]
print(f"key: {key}, value: {value}")

# 딕셔너리 키들만 모두 뽑아 보고싶을때
print(studentDict.keys())
print(list(studentDict.keys()))

# 딕셔너리 값들만 모드 뽑아보고싶을때
print(studentDict.values())
print(list(studentDict.values()))

searchKey = "code"

students = [
    {
        "code": 1,
        "name": "jenny"
    },
    {
        "code":2,
        "name":"ash"
    },
    {
        "code":3,
        "name":"chris"
    }
]

result = []

i = 0
while i < len(students):
        student = students[i]
        result.append(student[searchKey])
i += 1

print(result)

result = {
        "code": [1,2,3],
        "name": ['jenny','ash','chris']
    }

i = 0
while i < len(students):
        student = students[i]
        keys = list(student.keys())
        j = 0
        while j < len(keys):
            key = keys[j]
            j += 1
            if key in result:
                result[key].append(student[key])
                continue
result[key] = [student[key]]
i += 1

print(result)
