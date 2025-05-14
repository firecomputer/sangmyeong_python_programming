inFp=None
inStr=""

inFp=open("C:\\Users\\botis\\Documents\\sangmyeong_python_programming\\Kim Jaeheyon\\FileTest\\data1.txt", encoding="UTF8")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(inStr,end="")

inFp.close()