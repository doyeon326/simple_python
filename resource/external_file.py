#파이썬 외부 파일 처리
#파이썬 Excel, CSV 파일 읽기 및 쓰기

#CSV : MIME - text/csv

import csv
#예제1
with open('resource/sample1.csv', 'r', encoding="utf-8", errors = "ignore") as f:
    reader = csv.reader(f)
    
    #next(reader) 첫줄 스킵

    #확인
    print(reader)
    print(type(reader))

    for c in reader:
        print(c)

    #예제1
with open('resource/sample4.csv', 'r', encoding="utf-8", errors = "ignore") as f:
    reader = csv.reader(f, delimiter = '|')
    
    #next(reader) 첫줄 스킵

    #확인
    print(reader)
    print(type(reader))

    for c in reader:
        print(c)  

#예제 3
with open('resource/sample4.csv', 'r', encoding="utf-8", errors = "ignore") as f:
    reader = csv.DictReader(f)
    
    #확인
    
    for c in reader:
        for k, v in c.items():
            print(k, v)

        print("--------")

#예제4
w = [[1,2,3,],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('resource/sample5.csv','w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)
