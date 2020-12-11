#파이썬 예외처리의 이해

#예외 종류
#문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
#linter: 코드 스타일, 문법 체크

#SyntaxError: 잘못된 문법 
#print('Tes)
# x=>y

#NameError : 참조변수가 없음
a = 10
b = 15

#print(c)

#ZeoDivisionError : 0 나누기에러
#print(10 / 0)

#IndexError: 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
#print(x[3]) #예외 발생

#keyError
dic = {"name":"kim", "age":"33","city":"seoul"}

#print(dic['hobby])
print(dic.get('hobby'))

#AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
#print(time.month())

#valueError : 참조값이 없을때 발생
x = [1,5,9]

#x.remove(10)
#x.index(10)

#FileNotFoundError
#f = open('text.txt',r) #예외발생

#TypeError

x = [1,2]
y = (1,2)
z = "test"
#print(x + y ) #예외 결합 불가능

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
#그 후 런타임 예외 발생시 예외처리 코딩 권장 (EAFP 코딩 스타일)

#예외 처리 기본
#try: 에러가 발생할 가능성이 있는 코드 실행
#except: 예러명1
#except: 예러명2
#else : 에러가 발생하지 않았을 경우 실행
#finally: 항상 실행

#예제1

name = ['kim', 'Lee', 'Park']

try: 
    z = "kim"
    x = name.index(z)
    print('{} Found it! in name' .format(z,x+1))
except ValueError: #어떤에러가 발생했는지 모를때 except:
    print('Not found it! - Occurred ValueError!')
else:
    print("okay! else!")
finally:
    print("finally ok")

#예제4
#예외 처리는 하지 않지만, 무조건 수행되는 코당 패턴
try: 
    z = "kim"
finally:
    print("kim 실행")

#예제5
try:
    z = "kim"
    x = name.index(z)
    print('{} Found it! in name' .format(z, x+1))
except ValueError as l: # alias l 
    print(l)
except IndexError:
    print("IndexError")
except Exception:
    print("Exception")
else: 
    print("OK! else!")
finally:
    print("finally OK!")

#예제6
#예외 발생 : raise
#raise 키워드로 예외 직접 발생

try:
    a = "Kim"
    if a == "kim":
        print('Ok 허가!')
    else:
        raise ValueError #예외를 직접 만들때, 
except ValueError:
    print('문제발생')
except Exception as f:
    print(f)
else:
    print("OK!")