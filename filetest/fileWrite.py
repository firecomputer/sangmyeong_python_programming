outFp = None
outStr = ""

outFp = open('C:\\Users\\박재혁\\Desktop\\sangmyeong_python_programming\\filetest\\data2.txt', 'w', encoding="cp949")

while True:
    outStr = input('내용 입력:')
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print(" ---정상적으로 파일에 씀 ---")