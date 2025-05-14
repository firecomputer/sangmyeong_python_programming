
a = int(input('수식 계산은 1, 두 수 사이의 합 계산은 2'))
if a == 1:
    b = (input('수식을 입력하세요'))
    z = eval(b)
    print(z)


elif a == 2:
    c = int(input('첫번째 수를 입력'))
    d = int(input('두번째 수를 입력'))
    print((c*d + d**2)/2)
