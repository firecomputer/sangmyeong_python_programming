inFp, outFp = None, None
inStr=""

sceFile = input("소스 파일명을 입력하세요")
tgtFile = input('타겟 파일명을 입력하세요')

inFp = open(sceFile, 'r')
outFp = open(tgtFile, 'w')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('---%s 파일이 %s파일으로 정상적으로 복사되었음---'%(sceFile, tgtFile))