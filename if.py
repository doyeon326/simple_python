#파이썬 흐름제어(제어문)
#조건문 실습

print(type(type)) #Bool -> 0

#예1
if True:
    print("yes")

#예2
if False:
    print("No")

#예3 
if False:
    print("No")
    
else:
    print("Yes")

#관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)

#참 거짓 종류 (True, False)
#참: "내용, [내용], (내용), {내용}, 1"
#거짓: "", [], {}, 0

city = "1"

if city:
    print("문자있음")
else:
    print("문자없음")


#논리연산자
#and, or, not

a = 100
b = 60
c = 15

print('and:', a > b and b > c)
print('or:', a > b or c > b)
print('not', not a > b)

#산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1: ', 5 + 10 > 0 and not 7 + 3 == 10)

#다중 조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")


#중첩조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160: 
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")