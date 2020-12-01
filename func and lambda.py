#함수 정의 및 람다(lambda) 사용
#함수명(parameter)

#함수 선언 위치 중요

#예제1

def hello(word):
    print(">>>>hello", word)

hello("python!") 


#예제2
def hello_return(word):
    val = "Hello" + str(word)
    return val

str2 = hello_return("python!!!")
print(str2)

#예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    return y1, y2

val1, val2 = func_mul(100)
print(val1,val2)

#예제4(데이터 타입 변환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    return [y1, y2] # ()

lt = func_mul(100)
print(type(lt))

# 예제 4
# *args, *kwargs

def args_func(*args): #어떤 변수가 들어올지 모를때
    #print(args) #튜풀형태! ! ! 
    for i,v in enumerate(args):
        print(i,v)
    for t in args:
        print(t)


args_func('kim')
args_func('kim', 'park')
args_func('kim','park','shin')

#kwargs
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k,v)
kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2="Park", name3='lee')

#전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10,20,30,40, 'park', 'kim','shin', age1=24, age2 = 35)

#예제5 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

#예제6 힌트!
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    return [y1, y2] # ()

print(func_mul3(5))

#람다식 예제
#람다식: 메모리 절약, 가독성 향상, 코드 간결
#함수는 객체생성 -> 리소스 (메모리) 할당
#람다는 즉시 실행 (Heap 초기화) -> 메모리 초기화
# 가독성이 떨어질 수 있다. 

#일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

lambda_mul_10 = lambda num: num * 10 
print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    return( x * y * func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda  x:  x * 10000 ))