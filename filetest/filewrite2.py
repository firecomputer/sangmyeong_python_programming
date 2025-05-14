inFp, outFp = None, None
inStr=""

inFp = open('C:\\Windows\\win.ini', 'r')
outFp = open('C:\\Users\\박재혁\\Desktop\\sangmyeong_python_programming\\filetest\\data3.txt', 'w')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('--- 파일이 정상적으로 복사되었음---')