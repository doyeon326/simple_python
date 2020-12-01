# 파이썬 흐름제어(반복문)
# 반복문 실습

#코딩의 핵심 -> 조건 해결 중요

#기본 반복문: for, while

v1 = 1

while v1 < 11:
    print("v1 is:", v1)
    v1 += 1

for v2 in range(10): #0부터9까지
    print("v2 is :", v2)

for v3 in range(1,11):
    print("v3 is :", v3)

# 1 ~ 100합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100:', sum1)
print('1 ~ 100:',sum(range(1,101)))
print('1 ~ 100:',sum(range(1, 101, 2))) #두개씩 건너뜀

#시퀀스(순서가 있는) 자료형 반복
#문자열, 리스트, 튜플, 집합, 사전
#iterable 리턴 함수, range, reversed, enumerate, filter, map, zip

names = ["Kim","Park","Cho","Choi"]

for v in names:
    print("you are:", v)

word = "dreams"
for s in word:
    print("Word:",s)

#딕셔너리
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

for key in my_info:
    print("my_info", key) #키값출력

for key in my_info.values():
    print("my_info", key)

for key in my_info.keys():
    print("my_info", key)
for k,v in my_info.items():
    print("my_info", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

#break
numbers = [14,3,4,5,10,24,17,2,37,15,34,36,38]
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found: 33!")
else:
    print("Not found 33.....") #결국 다 뒤졌는데 못찾았어

#continue

lt = ["1", 2 ,5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print("타입: ", type(v))