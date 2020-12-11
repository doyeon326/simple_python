#파일 읽기, 쓰기
#읽기 모드 : r, 쓰기 모드 (기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# ..: 상대경로, / : 절대경로
#기타 : http://docs.python.org/3.7/library/functions/html#open

#파일 읽기
#예제1
import os
cwd = os.getcwd()
print(cwd)
f = open('resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
#반드시 close 리소스 반환
f.close()
print("-------------------")
#예제2
with open('resource/review.txt','r') as f:
    #with문은 close()를 생략해도 된다
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))


print("-------------------")

#예제3
with open('resource/review.txt','r') as f:
    for c in f:
        print(c.strip()) #양쪽 공백을 제거해준다.

print("-------------------")
#예제4
with open('resource/review.txt','r') as f:
    content = f.read()
    print(">", content)
    content = f.read() #내용없음 
    print(">", content)
print("-------------------")
#예제5
with open('resource/review.txt','r') as f:
    #둔장단위로 읽어온다. 
    line = f.readline()

    while line:
        print(line, end="\n")
        line = f.readline()
print("-------------------")
#예제6
with open('resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end= '*****')
print("-------------------")
#예제7

with open('resource/score.txt','r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('Average: {:6.3}'.format(sum(score)/len(score)))


#파일 쓰기 

#예제1
with open('resource/text1.txt','w') as f:
    f.write("Niceman\n")

#예제2
with open('resource/text1.txt','a') as f:
    f.write("Goodman\n")

#예제3
from random import randint

with open('resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(0,50))) #random
        f.write('\n')

#예제4
with open('resource/text3.txt','w') as f:
    list = ['Kim\n','Park\n','Cho\n']
    f.writelines(list)


#예제5
with open('resource/text4.txt','w') as f:
    print('Test Contexs1!', file=f)
    print('Test Contests2!', file=f)