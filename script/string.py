#문자열
#문자열 연산, 슬라이싱, 문자열

str1 = "I am Boy."
str2 = 'NiceMan'

print(len(str1), len(str2)) #길이 확인

escape_str1 = "Do you have a \"big collection\"" #escape
print(escape_str1)
escape_str2 = "Tab\tTab\t"
print(escape_str2)

#Raw String
raw_s1 = r'C:\Programs\Test\Bin' #잇는 그대로 출력
print(raw_s1) 

#멀티라인
multilin = \
""" 
문자열 
안녕! 
후후 
"""

print(multilin)

#문자열 연산
str_01 = '*'
str_02 = 'abc'
str_03 = "def"
str_04 = "Niceman"

print(str_01 * 100)
print(str_02 + str_03)
print('a' in str_04) # a가 포함되어있나? return true / false

#문자열 형 변환
print(str(77) + 'a') 

# 문자열 함수
a = "niceman"
b = "orange"

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))

print(a[0:3]) #nic
print(a[0:len(a)]) #niceman
print(a[:3]) #nic

print(b[0:3:2]) #2개씩 건너뛰면서 출력
