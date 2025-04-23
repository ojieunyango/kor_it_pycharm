numbers =[1,2,3,4,5]
print(numbers[0])
print(numbers[0:3])
print(numbers[:3])
print(numbers[-3:]) #-인덱스는 0부터 시작하니 뒤로 돌아가서 -1, -2 순서로...
print(numbers[:-2])
print("부산 동래구"[3:])
print((1,2,3,4)[2:]) # 튜플은 튜플로 나옴
#print({1,2,3,4}[2:]) # set 은 오류남

anyList = [[1,"김준일",[3,4,[7,"김준이"],6]]]

print(anyList[0][2:])
print(anyList[0][2][2][1])
print(anyList[0][2][1:3])

# 연산자
"""
+, -, *, **(제곱) /, //(몫), %
"""
print(3//2)
print(3**2)
print("*","\n","*"*2,"*"*3, sep="")
i = 0
while i<5:
    print("*"*(i+1))
    i += 1

i = 0
while i<5:
    print("*"*(5-i))
    i += 1

print([1,2,3]+[4,5,6])
print([1,2,3]*3) # 빼기는 안됨

print(len([1,2,3]))

anyList = [1,2,3,4]
i = 0
while i < len(anyList):
    print(anyList[i])
    i += 1

    print(str(3) + "hi")
    print(int("1") + 2)
    print(bool("True"))



del anyList[4] # del 키워드로 삭제할때 값이 꼭 존재해야한다.

print(anyList)
anyList.remove(10)
print(anyList)

try:
    anyList.pop(4)
    print(anyList)
except Exception as e:
    print("해당 리스트의 범위를 초과한 참조이다.")

anyList = [1,5,2,3,9]
anyList.copy().sort()
#copyAnyList = anyList.copy()
copyAnyList = anyList[:]
copyAnyList.sort()
print(anyList)
print(copyAnyList)

print([1,2,3,4,5]==[1,3,2,4,5])
anyList = [1,2,3,4,5]
anyList2 = [1,2,3,4,5]
print(id(anyList) == id(anyList2))
print(id(anyList), id(anyList2))

anyList = [1,2,3]
anyList2 = [4,5]
print(id(anyList))
anyList = anyList + anyList2
print(id(anyList))
anyList.extend([6,7])
print(id(anyList))

a = 10
