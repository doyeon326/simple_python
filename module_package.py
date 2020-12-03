#모듈과 패키지

#모듈을 구조적으로 관리하는게 페키지. 

#패키지 예제 
#상대경로
#.: 현재 디랙토리
#..: 부모디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

f = Fibonacci() 
f.fib(100)

print("ex1 : ", f.fib2(200))
print("ex2 : ", Fibonacci().title) #인스턴스초기화 후 사용

#사용2 권장 하지 않음
#from pkg.fibonacci inmort *

#사용3
#from pkg.fibonacci import Fibonacci as fb
# f = fb()
# f.fib(100)

#사용4(함수)
import pkg.calculations as c
print("ex4: ", c.add(10,100))
print("ex5: ", c.mul(10,29))

#사용5(함수)
#필요한 함수만 가져온다. 나누기 함수
from pkg.calculations import div as d
print("ex5: ", int(d(100,10)))

#사용6
import pkg.prints as p
import builtins

p.print1
p.print2
print(dir(builtins))