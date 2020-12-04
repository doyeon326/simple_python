#딕셔너리, 집합 자료형

#딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

#key, Value (Json) -> MongoDB

#선언
a = {'name': 'Kim','Phone':'000-777-7777','birth':960326}
b = {0: "Hello Python", 1: "Hello Coding"}
c = {'arr': [1,2,3,4,5]} #매우 유연한 구조

#출력
print(a['name'])
print(a.get('name')) #없으면 none
print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,3,4]
a['rahnk2'] = (1,2,3,)
print(a)

#keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])
print(a.values()) #리스트로 형변환을 해서 사용하면 인덱스로 꺼낼수 있다. 

print(a.items()) # 키밸류를 한쌍으로 가져옴
print('name' in a) #name 이 a에 있나? 


print()
print()
print()

#집합(sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 7, 7])

print(type(a))

t = tuple(b)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union)

print(s1 - s2)
print(s1.difference(s2))

#추가 & 제거 
s3 = set([7, 8, 9, 15])

s3.add(18)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))
