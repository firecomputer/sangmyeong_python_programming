outFp = None
outStr = ""

fname = input('파일명을 입력하세요')

outFp = open('C:\\Users\\박재혁\\Desktop\\sangmyeong_python_programming\\filetest\\' + fname, 'w', encoding="UTF8")

while True:
    outStr = input('내용 입력:')
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print(" ---정상적으로 파일에 씀 ---")