inFp=None
inStr=""

inFp=open("C:\\Users\\botis\\Documents\\sangmyeong_python_programming\\Kim Jaeheyon\\FileTest\\data1.txt", encoding="UTF8")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inFp.close()