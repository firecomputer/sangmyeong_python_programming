import random

def getNumber():
    return random.randrange(1, 46)

lotto = []
num = 0

print('**로또를 추첨합니다. **\n');

while True:
    num = getNumber()
    
    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >= 6:
        break

print('추첨된 로또번호 ==> ', end = '')
lotto.sort()
for i in range(0, 6):
    print('%d '% lotto[i], end = '')