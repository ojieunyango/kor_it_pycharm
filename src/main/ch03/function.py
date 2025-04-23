result = 10 + 20

def get10():
    return 5+3+2

result = get10() + 20


if get10() < 20:
    pass # 비워두고 싶을때
def isEmpty(value):
    return  str(value).strip()== ""

for text in ["", "a", "  ", "b"]:
    if isEmpty(text):
        print("비었음")
        continue
    print(text)