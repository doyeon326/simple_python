#Section02-2
#파이썬 기초 코딩

#import this
import sys

#파이선 기본 입력과 출력은 utf-8 이다 3버전부터
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#출력문
print('My name is Goodboy')

#변수선언
myName = 'Goodboy'

#조건문
if myName == "Goodboy":
    print('OK')

#반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

#변수(한글OK)
이름 = "도연"
print(이름)

#함수선언

def greeting():
    print("안녕하세요, 반갑습니다")

greeting()

#클래스

class Cookie:
    pass

#객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))