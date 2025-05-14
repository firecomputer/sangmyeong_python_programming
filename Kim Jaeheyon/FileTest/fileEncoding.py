import random

inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0

secuYN = input("1. 암호화, 2. 암호 해석 중 선택: ")
inFname = input("입력 파일명을 입력하세요: ")
outFname = input("출력 파일명을 입력하세요: ")
seed = input("암호화 키를 입력하세요: ")

random.seed(seed)

if secuYN == "1":
    secu = 1
elif secuYN == "2":
    secu = -1

inFp = open(inFname, 'r', encoding="UTF8")


inList = []

while True:
    inStr=inFp.readline()
    if not inStr:
        break
    inList.append(inStr)
inFp.close()

outFp = open(outFname, 'w', encoding="UTF8")

for inStr in inList:
    outStr=""
    for i in range(0, len(inStr)):
        ch=inStr[i]
        chNum=ord(ch)
        chNum=chNum+(secu*random.randint(1,100))
        ch2=chr(chNum)
        outStr=outStr+ch2
    outFp.write(outStr)
outFp.close()
print('%s-->%s 변환 완료' % (inFname, outFname))