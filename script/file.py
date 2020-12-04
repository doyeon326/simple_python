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
    line = f.readline()

    while line:
        print(line, end="\n")
        line = f.readline()