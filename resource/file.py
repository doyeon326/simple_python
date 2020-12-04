#파일 읽기, 쓰기
#읽기 모드 : r, 쓰기 모드 (기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# ..: 상대경로, / : 절대경로
#기타 : http://docs.python.org/3.7/library/functions/html#open

#파일 읽기
#예제1
f = open('./resource/review.text','r')
content = f.read()
print(content)

f.close