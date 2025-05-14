inFp=None
inStr=""

inFp=open("C:\\Users\\botis\\Documents\\sangmyeong_python_programming\\Kim Jaeheyon\\FileTest\\data1.txt", encoding="UTF8")

inList=inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()