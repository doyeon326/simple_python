# section02-1
#print 구문의 이해

print('Hello python!')
print("Hello python!")

print() #줄바꿈

#Seperator 옵션 사용
print('T','E','S', sep='')
print('2019','03','26', sep='-')
print('doyeon326','gmail.com', sep='@')

#end 옵션 사용
print('Welcome to', end='')
print('the black parade', end='')

#format 사용 [], {}, ()
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} and {b}".format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunki',7))

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price {1: 4.2f}".format(776, 6534.123))
print("Test1: {a:5d}, Price {b: 4.2f}".format(a=776, b=6534.123))

"""
Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨소리
\b : 백 스페이스
\000 : 널 문자
"""

print('you')
print('\'you\'')
print("""'you\n'""")
print("\t\t'you'")
