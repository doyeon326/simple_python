#리스트, 튜플

#리스트 (순서0, 죽복0, 수정0, 삭제0)

#선언

a = []
b = list()
c = [1,2,3,4]
d = [10,100, ['Pen', 'Banana', 'Orange']] #타입이 달라도 가능! 

#인덱싱
print(d[2][2])
print(d[-1][-1])

#슬라이싱
print(d[0:2])

#연산
print(c + d)
print(c * 3)

#리스트 수정, 삭제
c[0] = 77
c[1:2] = [100,1000,1000]
print(c)

del c[1] #삭제
print(c)
print()
print()
print()

#리스트 함수
y = [5, 2, 4, 1, 4]
print(y)
y.append(6)
print(y)
y.sort
print(y)
y.reverse()
print(y)
y.insert(2,7) #y의 2번 인덱스에 7을 넣음! 
print(y)
y.remove(2) #인덱스가 아니라 값을 지움
print(y)
#del 도있음 인덱스로 지움. 
y.pop() #마지막껄 꺼낸다
print(y) #LIFO

ex = [88,77]
y.append(ex) #리스트 자체를 추가
y.extend(ex) #원소를 추가

#튜플 (순서0, 중복0, 수정x, 삭제x)
#중요 데이터는 튜플에다가 써 넣으면 추후 삭제를 방지한다

a = () 
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

#인덱싱은 리스트와 같음
print(c[2])
print(c[3])
print(d[2][2])

#슬라이싱도 가능
print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

#튜플 함수
z = (5, 2, 1, 3, 4)
print(3 in z)
print(z.index(3)) #3이 있는곳의 인덱스를 반환한다. 
print(z.count(1)) #1이 몇개가 있는지? 