set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 & set2) # & 교집합 구하는거

text1 = "my name is jj"
text2 = "my name is joy"
textList1 = text1.split(" ")
textList2 = text2.split(" ")
textSet1 = set(textList1)
textSet2 = set(textList2)
print(textSet1 & textSet2)
print((textSet1 | textSet2) - (textSet1 & textSet2)) # 전체 | 이걸로 합치고 교집합을 빼면 이름만 나옴


